import requests
targer_url = "https://www.baidu.com/img/bd_logo1.png?where=super "
r = requests.get(targer_url)

with open("a.png","wb") as f:
    f.write(r.content)

#傻吊网图下载器