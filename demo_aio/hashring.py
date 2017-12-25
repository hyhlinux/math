import hashlib

class HashRing(object):
    def __init__(self, nodes=None, replicas=3):
        """

        """
        self.replicas = replicas
        self.ring = dict()
        self._sorted_keys = []
        if nodes:
            for node in nodes:
                self.add_node(node)

    def add_node(self, node):
        for i in range(0, self.replicas):
            key = self.gen_key('{}:{}'.format(node, i))
            print(key)
            self.ring[key] = node
            self._sorted_keys.append(key)

    def remove_node(self, node):
        for i in range(0, self.replicas):
            key = self.gen_key('{}:{}'.format(node, i))
            del self.ring[key]
            self._sorted_keys.remove(key)

    def get_node(self, key):
        return self.get_node_pos(key)[0]

    def get_node_pos(self, string_key):
        if not self.ring:
            return None, None
        key = self.gen_key(string_key)
        nodes = self._sorted_keys

        for i in range(0, len(nodes)):
            node = nodes[i]
            if key <= node:
                print("string_key:{} key:{}".format(string_key, key))
                print("get node {}-{} ".format(self.ring[node], i))
                return self.ring[node], i
        return self.ring.get(nodes[0], None), 0

    def gen_key(self, key):
        m = hashlib.md5()
        print(key)
        m.update(key.encode('utf8'))
        return m.hexdigest()

    def print_ring(self):
        if not self.ring:
            return None, None
        nodes = self._sorted_keys
        for i in range(0, len(nodes)):
            node = nodes[i]
            print('ring slot:{} is node:{}, hash vale is:{}'.format(i, self.ring[node], node))



def main():
    memcache_server = ['a', 'g', 'z']
    ring = HashRing(memcache_server, 1)
    ring.print_ring()
    server = ring.get_node('0000')
    server = ring.get_node('1111')
    server = ring.get_node('2222')
    server = ring.get_node('3333')
    server = ring.get_node('4444')
    server = ring.get_node('5555')
    server = ring.get_node('6666')
    server = ring.get_node('7777')
    server = ring.get_node('8888')
    server = ring.get_node('9999')
    pass


if __name__ == '__main__':
    main()
