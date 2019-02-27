import requests
import json
from pprint import pprint

url = "https://api.douban.com/v2/movie/in_theaters"
headers = {
  "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}
r = requests.get(url=url,headers=headers)
html_str = r.content.decode()
#json.loads把json字符串转化位python类型
ret1 = json.loads(html_str)
print(ret1)
