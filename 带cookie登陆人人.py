import requests

headers = {
    "User-Agent":"Mozilla/5.0 (Linux; Android 5.1.1; Nexus 6 Build/LYZ28E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Mobile Safari/537.36",
    "Cookie":"anonymid=jslnckgr-ilcsor; depovince=GW; _r01_=1; JSESSIONID=abc885_Ve1ptchqXLAPKw; ick_login=a9876885-4bb4-4b2d-99ef-7213a67675c6; _de=4A79E3A64E7252757187CC9196592CFA; ick=628f60bd-a4c7-4bef-b935-7efdee0da2dc; __utma=151146938.721825102.1551178167.1551178167.1551178167.1; __utmc=151146938; __utmz=151146938.1551178167.1.1.utmcsr=renren.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmb=151146938.4.10.1551178167; jebecookies=c820b34a-b82d-43bd-aee9-dcec1fcd66a5|||||; p=408fbe086cb4ed1587f858a81402d4609; first_login_flag=1; ln_uact=13797120611; ln_hurl=http://head.xiaonei.com/photos/0/0/women_main.gif; t=42e31a071ea815711ce4e83b288c03859; societyguester=42e31a071ea815711ce4e83b288c03859; id=579604879; xnsid=d6926026; ver=7.0; loginfrom=null; wp_fold=0; XNESSESSIONID=e1c70f905918; l4pager=0"
     }#可以用字典推导式来搞cookie


r = requests.get("http://www.renren.com/579604879/profile",headers=headers)
#再使用session进行请求登陆之后才能访问的地址
with open("renren.html","w",encoding="utf-8") as f:
    f.write(r.content.decode())