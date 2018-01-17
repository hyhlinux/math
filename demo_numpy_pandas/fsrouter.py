import requests
import matplotlib.pyplot as plt
import pandas as pd


last = 0

def get_hash_map(url="http://172.16.1.104:4004/stats?which=app"):
    resp = requests.get(url)
    data = resp.json()
    hash_map = data.get("hostGroupMap", {}).get("default", {}).get("HashMap", {})
    return hash_map


def get_diff(val):
    global last
    ret = val - last
    last = val
    return ret


def diff_sum(ret=None):
    diff_sum_map = {}
    for key in ret:
        diff_sum_map[key[0]] = key[2] + diff_sum_map.get(key[0], 0)
    return diff_sum_map


def show_pie(labels, sizes):
    # print(diff_map)
    # print(labels, sizes)
    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    # explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
    ax1.axis('equal')
    plt.show()


def to_cvs(ret_list=None, columns=['host_name', 'hash', 'diff']):
    if not ret_list:
        return
    df = pd.DataFrame(ret_list, columns=columns)
    print(df)
    df.to_csv("hash_host.csv", sep=',', encoding='utf-8', index=True)
    return


def get_request_count(url="http://172.16.1.104:4004/stats"):
    resp = requests.get(url)
    data = resp.json()
    # request_map = data.get("hostGroupStatsMap", {}).get("default", {}).get("HostMap", {})
    request_map = data.get("hostGroupStatsMap", {}).get("default", {})
    return request_map


def app_pie(url=""):
    hash_map = get_hash_map(url)
    hash_map_sort = sorted(hash_map.items(), key=lambda d: int(d[0]))
    ret_list = [(k[1], k[0], get_diff(int(k[0])))  for k in hash_map_sort]
    to_cvs(ret_list)
    diff_map = diff_sum(ret_list)
    for k, v in diff_map.items():
        print(k, v)
    labels = [key for key in diff_map.keys()]
    sizes = [v for v in diff_map.values()]
    show_pie(labels, sizes)
    return


def request_pie(url=""):
    # url = "http://192.168.6.14:4004/stats?which="
    request_map = get_request_count(url)
    print(request_map)
    if not request_map:
        return
    for k, v in request_map.items():
        print(k, v)
    request_labels = [key for key in request_map.keys()]
    request_sizes = [v for v in request_map.values()]
    show_pie(request_labels, request_sizes)
    return


def main():
    url = "http://192.168.0.96:4004/stats?which=app"
    # url = "http://172.16.1.104:4004/stats?which=app"
    app_pie(url)
    # url = url[:-3]
    # request_pie(url)


if __name__ == '__main__':
    main()
