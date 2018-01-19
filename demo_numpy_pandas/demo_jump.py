import jump
import matplotlib.pyplot as plt

hosts = [
    "host1",
    "host2",
    "host3",
]

hostMap = {"{}".format(i): hosts[i] for i in range(len(hosts))}


def pie_host():
    data_map = {}
    for i in range(1000):
        ret = jump.hash(i, len(hosts))
        key = hostMap.get("{}".format(ret), "default")
        data_map[key] = 1 + data_map.get(key, 0)

    def show_pie(labels, sizes):
        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
        ax1.axis('equal')
        plt.show()

    labels = [key for key in data_map.keys()]
    sizes = [v for v in data_map.values()]
    show_pie(labels=labels, sizes=sizes)


def main():
    pie_host()


if __name__ == '__main__':
    main()
