# coding:utf-8

AuthSalt = "salt++"


def gen_account(user_name):
    # fab make_account:user_name="http://14845132.xgj.me:27035"
    import hashlib
    import base64
    passwd = hashlib.md5(AuthSalt + user_name).hexdigest()
    return "%s:%s" % (base64.urlsafe_b64encode(user_name).rstrip('='), passwd[:8])


__proxy_hosts = {
    '192.168.0.1': {
        # "[2222:5300:61:9b2::2]": "jp",
        # "[2222:5300:61:9b2::1]": "jp",
    },
}


def gen_proxy_list():
    l = []
    for (k, v) in __proxy_hosts.items():
        for (k1, v1) in v.items():
            user = gen_account("ip://" + k1)
            addr = "http://%s@%s:80" % (user, k)
            l += [addr]
    return l


def print_proxy_list():
    l = gen_proxy_list()
    for addr in l:
        print(addr)

if __name__ == '__main__':
    print_proxy_list()
