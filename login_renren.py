import requests
session = requests.session()
post_url = "http://www.renren.com/PLogin.do"
post_data = {"email":"13797120611","password":"wuwangsao"
}
headers = {
    "User-Agent":"Mozilla/5.0 (Linux; Android 5.1.1; Nexus 6 Build/LYZ28E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Mobile Safari/537.36"}

session.post(post_url,data=post_data,headers=headers)
#使用session发送post请求，cookie保存在其中


r = session.get("http://www.renren.com/579604879/profile",headers=headers)
#再使用session进行请求登陆之后才能访问的地址
with open("renren.html","w",encoding="utf-8") as f:
    f.write(r.content.decode())