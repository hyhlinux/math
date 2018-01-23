import jump
import binascii
import matplotlib.pyplot as plt

hosts = [
    "host1",
    "host2",
    "host3",
    "host4",
    "host5",
    "host6",
    "host7",
    "host8",
    "host9",
    "host10",
]

hostMap = {"{}".format(i): hosts[i] for i in range(len(hosts))}


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


def pie_host_del():
    data_map = {}
    for i in range(10000):
        fid = bytes("/b/apk/Y29tLm1vYmlsZS5sZWdlbmRzXzExNTIxMzMxX2U4ZGIzOTM{:0>5}".format(i), encoding='utf-8')
        ret = jump.hash(binascii.crc32(fid) & 0xffffffff, len(hosts))
        # ret = jump.hash(i, len(hosts))
        print("{},{},{},{}".format(i, fid, ret, hosts[ret]))
        key = hostMap.get("{}".format(ret), "default")
        data_map[key] = 1 + data_map.get(key, 0)
    if not data_map:
        return
    for k, v in data_map.items():
        print(k, v)
    labels = [key for key in data_map.keys()]
    sizes = [v for v in data_map.values()]
    show_pie(labels=labels, sizes=sizes)


def main():
    pie_host_del()
    # pie_host()


if __name__ == '__main__':
    main()
