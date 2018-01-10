import requests
import matplotlib.pyplot as plt
import pandas as pd


last = 0

def get_hash_map(url="http://172.16.1.104:4004/stats?which=app"):
    data = {
 		11288839448486286693: "d-01.winudf.com",
		6666967547630157160: "d-01.winudf.com",
		16549567120859172415: "d-04.winudf.com",
		12002990505820781658: "d-01.winudf.com",
		7916375373558770949: "d-02.winudf.com",
		4451133326594493219: "d-04.winudf.com",
		17365357814277938146: "d-04.winudf.com",
		10750911147294077240: "d-05.winudf.com",
		10458146926787108284: "d-01.winudf.com",
		12454832026850195165: "d-03.winudf.com",
		239767381301946287: "d-03.winudf.com",
		5528192315630124532: "d-05.winudf.com",
		452996756677201714: "d-02.winudf.com",
		3502165566924052056: "d-02.winudf.com",
		2977716204983640882: "d-01.winudf.com",
		14344554222429636802: "d-03.winudf.com",
		10390044413896638947: "d-04.winudf.com",
		13773539064902090035: "d-05.winudf.com",
		10092989078352289744: "d-05.winudf.com",
		13378005536304911769: "d-05.winudf.com",
		15325594361307077113: "d-03.winudf.com",
		4904457498958676496: "d-04.winudf.com",
		13184936874599904655: "d-01.winudf.com",
		4218835131624438454: "d-01.winudf.com",
		784583097262749752: "d-01.winudf.com",
		8897651215659834605: "d-02.winudf.com",
		14336560970540577641: "d-02.winudf.com",
		14469340804132123322: "d-03.winudf.com",
		5070389339984637017: "d-05.winudf.com",
		3056735848870237707: "d-05.winudf.com",
		13150121062688234526: "d-05.winudf.com",
		3696353760717863724: "d-05.winudf.com",
		17481834308909352631: "d-04.winudf.com",
		11568738635287076629: "d-04.winudf.com",
		8234608672636041183: "d-01.winudf.com",
		12169615549004988701: "d-02.winudf.com",
		13371020549017399961: "d-02.winudf.com",
		11348286291119357192: "d-02.winudf.com",
		16317840089229516113: "d-02.winudf.com",
		18280333195893202206: "d-02.winudf.com",
		10707663742784821561: "d-04.winudf.com",
		5193981502517103491: "d-04.winudf.com",
		7692414431255807895: "d-01.winudf.com",
		9628520333863316297: "d-03.winudf.com",
		11540013013605019730: "d-03.winudf.com",
		17720137207200896767: "d-03.winudf.com",
		10430329369657078618: "d-03.winudf.com",
		3983909878270734083: "d-03.winudf.com",
		18335112364259407429: "d-04.winudf.com",
		15948193272562514287: "d-05.winudf.com",
    }
    return data


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
    request_map = data.get("hostGroupStatsMap", {}).get("default", {}).get("HostMap", {})
    return request_map

def main():
    hash_map = get_hash_map()
    # hash_map_sort = sorted(hash_map.keys(), key=lambda d: d[0])
    hash_map_sort = sorted(hash_map.keys())
    ret_list = [(hash_map[k], k, get_diff(k))  for k in hash_map_sort]
    to_cvs(ret_list)
    diff_map = diff_sum(ret_list)
    for k, v in diff_map.items():
        print(k, v)
    labels = [key for key in diff_map.keys()]
    sizes = [v for v in diff_map.values()]
    show_pie(labels, sizes)
    request_map = get_request_count()
    print(request_map)
    if not request_map:
        return
    for k, v in request_map.items():
        print(k, v)
    request_labels = [key for key in request_map.keys()]
    request_sizes = [v for v in request_map.values()]
    show_pie(request_labels, request_sizes)


if __name__ == '__main__':
    main()
