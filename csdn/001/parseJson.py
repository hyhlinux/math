import requests
import json

url = "http://webh.huajiao.com/User/getUserFeeds?uid=55284312&fmt=jsonp"

def get_json(url):
    try:
        response = requests.get(url)
        json_data = json.loads(response.text)
        return json_data
    except Exception as e:
        print(e)
        return dict(err="{}".format(e))

def main():
    jsData = get_json(url)
    print(jsData)
    for idx in range(len(jsData["data"]["feeds"])):
        print("+" * 50)
        print(idx)
        print(jsData["data"]["feeds"])
        print(len(jsData["data"]["feeds"][idx]["feed"]))
        # print(jsData["data"]["feeds"][idx]["feed"]["watermark"])
        print(jsData["data"]["feeds"][idx].get("feed", {}).get("watermark", ""))
    pass

if __name__ == '__main__':
    main()
