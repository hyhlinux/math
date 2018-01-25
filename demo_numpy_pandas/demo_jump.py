import jump
import binascii
import matplotlib.pyplot as plt

hosts = [
    "host1",
    "host2",
    "host3",
    "host4",
    "host5",
]

health_hosts = hosts[:]
hostMap = {host: 0 for host in hosts}
move_cnt = 0
move_map = {host: 0 for host in hosts}


def show_pie(labels, sizes):
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
    ax1.axis('equal')
    plt.show()


def pie_host():
    data_map = {}
    for i in range(100):
        ret = jump.hash(i, len(hosts))
        key = hostMap.get("{}".format(ret), "default")
        data_map[key] = 1 + data_map.get(key, 0)

    labels = [key for key in data_map.keys()]
    sizes = [v for v in data_map.values()]
    show_pie(labels=labels, sizes=sizes)


def new_hash(key):
    import hashlib
    m = hashlib.md5()
    if isinstance(key, bytes):
        m.update(key)
    else:
        m.update(key.encode('utf-8'))
    # return hashlib.new('md5', string=key).hexdigest()
    return m.hexdigest()


def jump_hash(key, hosts=None, host_die='host1'):
    global health_hosts
    global move_cnt
    if not hosts:
        return None
    ret = jump.hash(binascii.crc32(key) & 0xffffffff, len(hosts))
    if hosts[ret] != host_die:
        return hosts[ret]
    new_key = bytes("{}".format(new_hash(key)), encoding='utf-8')
    health_hosts = hosts[:]
    if host_die in health_hosts:
        health_hosts.remove(host_die)
    move_ret = jump.hash(binascii.crc32(new_key) & 0xffffffff, len(health_hosts))
    move_cnt += 1
    # print('转移: {}->{}  key:{}, new_key:{}, ret:{}: move_ret:{}'.format(hosts[ret], health_hosts[move_ret], key, new_key, ret, move_ret))
    global move_map
    move_map[health_hosts[move_ret]] += 1
    return health_hosts[move_ret]


def jump_hash2(key, hosts=None, host_die='host1'):
    global health_hosts
    global move_cnt
    # if not hosts:
    #     return None
    ret = jump.hash(binascii.crc32(key) & 0xffffffff, len(hosts))
    # if hosts[ret] != host_die:
    #     return hosts[ret]
    health_hosts = hosts[:]
    if host_die in health_hosts:
        health_hosts.remove(host_die)
    move_ret = jump.hash(binascii.crc32(key) & 0xffffffff, len(health_hosts)+1)
    if move_ret >= len(health_hosts):
        move_ret = len(health_hosts)-1
    if move_ret <= 0:
        move_ret = 0
    if hosts[ret] != health_hosts[move_ret]:
        move_cnt += 1
        # print('转移: {}->{} key:{}, ret:{}: move_ret:{}'.format(hosts[ret], health_hosts[move_ret], key, ret, move_ret))
    return health_hosts[move_ret]


def pie_host_del():
    data_map = {}
    for i in range(10000):
        fid = bytes("/b/apk/Y29tLm1vYmlsZS5sZWdlbmRzXzExNTIxMzMxX2U4ZGIzOTM{:0>5}".format(i), encoding='utf-8')
        host_die = 'host1'
        host = jump_hash(fid, hosts, host_die=host_die)
        # print("{},{},{}".format(i, fid, host))
        # key = hostMap.get("{}".format(host), "default")
        data_map[host] = 1 + data_map.get(host, 0)
    if not data_map:
        return
    for k, v in data_map.items():
        print(k, v)
    # labels = [key for key in data_map.keys()]
    # sizes = [v for v in data_map.values()]
    # show_pie(labels=labels, sizes=sizes)
    print('move_cnt:', move_cnt)
    print('move_map:', move_map)
    if host_die in move_map:
        del move_map[host_die]
    labels = [key for key in move_map.keys()]
    sizes = [v for v in move_map.values()]
    show_pie(labels=labels, sizes=sizes)


def main():
    pie_host_del()
    # pie_host()
    # for i in range(10):
    #     print(new_hash("test{}".format(i)))


if __name__ == '__main__':
    main()
