# coding:utf-8
import requests
from lxml import etree

Url = 'https://www.1905.com/vod/?_t_t_t=0.5723789716139436'

result = requests.get(Url).text

dom = etree.HTML(result)
urls = dom.xpath('//img/@src')
path = 'imgs'
def down_img(url,path):
    arr = url.split('.')
    path = path + '.' + arr[len(arr)-1]
    re = requests.get(url)
    with open(path, 'wb') as f:
        for chunk in re.iter_content(chunk_size=128):
          f.write(chunk)

for i in range(len(urls)):
    if(not urls[i].startswith('http')):
        urls[i] = 'http:'+urls[i]
    down_img(urls[i],'imgs/'+str(i))
