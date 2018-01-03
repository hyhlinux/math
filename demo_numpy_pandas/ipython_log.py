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
