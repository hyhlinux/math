import os
import requests
from lxml import etree

base_dir = "/tmp"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36"}


class MZITUSpider(object):
    """docstring for MZITUSpider"""

    def __init__(self, domain=""):
        super(MZITUSpider, self).__init__()
        self.domain = domain

    def run(self):
        if not self.domain:
            return None
        home_resp = requests.get(self.domain, headers=headers)
        if not home_resp:
            return None
        all_uid_link_list = self.parse_home(home_resp.text)
        for uid_link in all_uid_link_list:
            if not uid_link or len(uid_link) == 1:
                continue
            uid_home = self.get_uid_page(uid_link[1])
            child_link_list = self.pare_uid_child_page(uid_home)
            if not child_link_list:
                continue
            for link in child_link_list:
                child_link = "{}/{}".format(uid_link[1], link)
                img_links = self.parse_img_from_child_page(child_link)
                if not img_links:
                    continue
                print("page:{} img_link:{}".format(child_link, img_links))
                for img_link in img_links:
                    if not img_link:
                        continue
                    self.download_img(img_link)

    def parse_home(self, body=None):
        tree = etree.HTML(body)
        a_list = [(a.text, a.attrib.get('href')) for a in tree.xpath(
            "//div[contains(@class, 'all')]//li//a") if not a]
        return a_list

    def get_uid_page(self, url=""):
        if not url:
            return None
        src_html = requests.get(url, headers=headers)
        if not src_html:
            return None
        return src_html.text

    def pare_uid_child_page(self, html=""):
        if not html:
            return None
        child_tree = etree.HTML(html)
        span_list = child_tree.xpath(
            "//div[contains(@class, 'pagenavi')]//span//text()")
        if span_list and len(span_list) > 2:
            span_list = span_list[1:-1]
        return span_list

    def parse_img_from_child_page(self, url=""):
        if not url:
            return None
        body = requests.get(url, headers=headers)
        if not body:
            return None
        child_tree = etree.HTML(body.text)
        img_link = child_tree.xpath(
            "//div[contains(@class, 'main-image')]//img/@src")
        return img_link

    def download_img(self, url=""):
        if not url:
            return None
        print('dl:', url)
        img = requests.get(url, headers=headers)
        if not img:
            return None
        file_name = url.replace("/", "_", -1)
        with open(os.path.join(base_dir, file_name), 'wb') as f:
            f.write(img.content)


def main():
    all_url = "http://www.mzitu.com/all"
    spider = MZITUSpider(domain=all_url)
    spider.run()
    pass

if __name__ == '__main__':
    main()
