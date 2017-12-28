import requests
from lxml import etree


class Spider(object):
    def __init__(self, url, head):
        self.url = url
        self.text = ''
        self.head = head
        self.href_list = []

    def get_resp(self):
        resp = None
        try:
            resp = requests.get(self.url)
            print(resp)
            return resp.content
        except Exception as e:
            print(e)
            return None


def main():
    url = "https://www.csdn.net/"

    pass

if __name__ == '__main__':
    main()
