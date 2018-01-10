# IPython log file

import numpy as np
get_ipython().run_line_magic('pinfo', 'np')
get_ipython().run_line_magic('pinfo2', 'np.sort')
get_ipython().run_line_magic('run', 'demo_np02.py')
_ip
get_ipython().run_line_magic('who', '')
get_ipython().run_line_magic('whos', '')
get_ipython().run_line_magic('who_is', '')
get_ipython().run_line_magic('who_ls', '')
_
__
get_ipython().run_line_magic('logstate', '')
get_ipython().run_line_magic('logstart', '')
x = "foobar"
y = "foo"
x.startswith(y)
get_ipython().run_line_magic('timeit', 'x.startswith(y)')
import request
import requests
import requests
s = requests.Session()

s.get('http://www.mzitu.com/')
r = s.get("http://httpbin.org/cookies")

print(r.text)
s = requests.Session()

s.get('http://www.mzitu.com/')
print(s)

r = s.get("http://httpbin.org/cookies")
print(r.text)
s = requests.Session()

s.get('http://www.mzitu.com/')
print(s)
s.get("")
r = s.get("http://httpbin.org/cookies")
r.headers
print(r.text)
s = requests.Session()

s.get('http://www.mzitu.com/')
print(s)
r = s.get("http://httpbin.org/cookies")
print(r.headers)
print(r.text)
import requests
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36"}
headers
all_url = "http://www.mzitu.com/all"
start_html = requests.get(all_url, headers=headers)
start_html
start_html.text
from lxml import etree
start_html.text
tree = etree.HTML(start_html.text)
tree = etree.HTML(start_html.text)
tree.xpath("//li//a/@href")
tree = etree.HTML(start_html.text)
tree.xpath("//li[contains(@class, 'all')]//a/@href")
tree = etree.HTML(start_html.text)
tree.xpath("//div[contains(@class, 'all')]//li//a/@href")
tree = etree.HTML(start_html.text)
tree.xpath("//div[contains(@class, 'all')]//li//a")
tree = etree.HTML(start_html.text)
[a for a in tree.xpath("//div[contains(@class, 'all')]//li//a")]
tree = etree.HTML(start_html.text)
a_list = [ a for a in tree.xpath("//div[contains(@class, 'all')]//li//a")]
tree = etree.HTML(start_html.text)
a_list = [ a for a in tree.xpath("//div[contains(@class, 'all')]//li//a")]
a = a_list[0]
a
a.text()
a.text
a.text, a.attrib("href")
a.text, a.attrib
a.text, a.attrib.get('href')
tree = etree.HTML(start_html.text)
[ a.text, a.attrib.get('href') for a in tree.xpath("//div[contains(@class, 'all')]//li//a") if not a]
tree = etree.HTML(start_html.text)
# a.text, a.attrib.get('href')
[a for a in tree.xpath("//div[contains(@class, 'all')]//li//a") if not a]
tree = etree.HTML(start_html.text)
# a.text, a.attrib.get('href')
[a.text for a in tree.xpath("//div[contains(@class, 'all')]//li//a") if not a]
tree = etree.HTML(start_html.text)
# a.text, a.attrib.get('href')
[a.text, 1 for a in tree.xpath("//div[contains(@class, 'all')]//li//a") if not a]
tree = etree.HTML(start_html.text)
# a.text, a.attrib.get('href')
[(a.text, 1) for a in tree.xpath("//div[contains(@class, 'all')]//li//a") if not a]
tree = etree.HTML(start_html.text)
# a.text, a.attrib.get('href')
[(a.text, a.attrib.get('href')) for a in tree.xpath("//div[contains(@class, 'all')]//li//a") if not a]
tree = etree.HTML(start_html.text)
# (a.text, a.attrib.get('href'))
[a for a in tree.xpath("//div[contains(@class, 'all')]//li//a") if not a]
start_html.text[:10]
a.text, a.attrib.get('href')
tree = etree.HTML(start_html.text)
# (a.text, a.attrib.get('href')) , 提交代码是只打印标签，测试时看数据。
a_list = [a.text, a.attrib.get('href'))for a in tree.xpath("//div[contains(@class, 'all')]//li//a") if not a]
tree = etree.HTML(start_html.text)
# (a.text, a.attrib.get('href')) , 提交代码是只打印标签，测试时看数据。
a_list = [(a.text, a.attrib.get('href')) for a in tree.xpath("//div[contains(@class, 'all')]//li//a") if not a]
a_list[0]
a_list[1]
for a in a_list:
    print(a[1])
for a in a_list[:2]:
    print(a[1])
def get_child_page(url=""):
    if not url:
        return None
    src_html = requests.get(url, headers=headers)
    return src_html
get_child_page(a_list[0][1])
def get_child_page(url=""):
    if not url:
        return None
    src_html = requests.get(url, headers=headers)
    if not src_html:
        return None
    return src_html.text
get_child_page(a_list[0][1])
def get_child_page(url=""):
    if not url:
        return None
    src_html = requests.get(url, headers=headers)
    if not src_html:
        return None
    return src_html.text
#get_child_page(a_list[0][1])
def get_child_link(html=""):
    if not html:
        return None
    child_tree = etree.HTML(html)
    child_tree.xpath("//span")
for a in a_list[:2]:
    print(a[1])
    body = get_child_page(a[1])
    print(get_child_link(body))
for a in a_list[:2]:
    print(a[1])
    body = get_child_page(a[1])
    print(len(body))
    print(get_child_link(body))
for a in a_list[:2]:
    print(a[1])
    body = get_child_page(a[1])
    print(len(body))
    print(get_child_link(body))
def get_child_page(url=""):
    if not url:
        return None
    src_html = requests.get(url, headers=headers)
    if not src_html:
        return None
    return src_html.text
body = get_child_page(a_list[0][1])
def get_child_link(html=""):
    if not html:
        return None
    child_tree = etree.HTML(html)
    span_list = child_tree.xpath("//div[contains(@class, 'pagenavi')]//span")
    if not span_list and len(span_list) > 2:
        span_list = span_list[1:-1]
    return span_list
get_child_link(body)
def get_child_link(html=""):
    if not html:
        return None
    child_tree = etree.HTML(html)
    span_list = child_tree.xpath("//div[contains(@class, 'pagenavi')]//span//text()")
    if not span_list and len(span_list) > 2:
        span_list = span_list[1:-1]
    return span_list
get_child_link(body)
def get_child_link(html=""):
    if not html:
        return None
    child_tree = etree.HTML(html)
    span_list = child_tree.xpath("//div[contains(@class, 'pagenavi')]//span//text()")
    if span_list and len(span_list) > 2:
        span_list = span_list[1:-1]
    return span_list
get_child_link(body)
for a in a_list[:2]:
    print(a[1])
    body = get_child_page(a[1])
    print(len(body))
    print(get_child_link(body))
for a in a_list[:2]:
    print(a[1])
    body = get_child_page(a[1])
    print(len(body))
    child_link_list = get_child_link(body)
    for link in child_link_list:
        print("new_link:{}/{}".format(a[1], link))
for a in a_list[:2]:
    print(a[1])
    body = get_child_page(a[1])
    print(len(body))
    child_link_list = get_child_link(body)
    for link in child_link_list:
        print("{}/{}".format(a[1], link))
for a in a_list[:2]:
    print(a[1])
    body = get_child_page(a[1])
    print(len(body))
    child_link_list = get_child_link(body)
    for link in child_link_list:
        print("{}/{}".format(a[1], link))
# 获取该用户的所有分页链接
def get_child_link(html=""):
    if not html:
        return None
    child_tree = etree.HTML(html)
    span_list = child_tree.xpath("//div[contains(@class, 'pagenavi')]//span//text()")
    if span_list and len(span_list) > 2:
        span_list = span_list[1:-1]
    return span_list
get_child_link(body)
# 获取该用户某一个分页的具体图片
def parse_img_from_child_page(url=""):
    src_html = requests.get(url, headers=headers)
    child_tree = etree.HTML(src_html.text)
    img_link = child_tree.xpath("//div[contains(@class, 'main-image')]//img/@src")
    return img_link
parse_img_from_child_page(url="http://www.mzitu.com/114525/65")
def download_img(url=""):
    body = requests.get(url, headers=headers)
img = "http://i.meizitu.net/2018/01/02c65.jpg"
img.replace("/", "_", -1)
base_dir = "/tmp"
def download_img(url=""):
    if not url:
            return None
    print('dl:', url)
    img = requests.get(url, headers=headers)
    if not img:
        return None
    file_name = url.replace("/", "_", -1)
    with open(os.path.join(base_dir, file_name), 'wb') as file:
        f.write(img.content)
download_img("http://i.meizitu.net/2018/01/02c65.jpg") 
import os
base_dir = "/tmp"
def download_img(url=""):
    if not url:
            return None
    print('dl:', url)
    img = requests.get(url, headers=headers)
    if not img:
        return None
    file_name = url.replace("/", "_", -1)
    with open(os.path.join(base_dir, file_name), 'wb') as file:
        f.write(img.content)
download_img("http://i.meizitu.net/2018/01/02c65.jpg") 
import os
base_dir = "/tmp"
def download_img(url=""):
    if not url:
            return None
    print('dl:', url)
    img = requests.get(url, headers=headers)
    if not img:
        return None
    file_name = url.replace("/", "_", -1)
    with open(os.path.join(base_dir, file_name), 'wb') as f:
        f.write(img.content)
download_img("http://i.meizitu.net/2018/01/02c65.jpg") 
