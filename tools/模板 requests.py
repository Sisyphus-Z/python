import requests

#r = requests.get('http://httpbin.org/get')

headers1={
"Host":"acgaa.cyou",
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0",
"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
"Accept-Language":"zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
"Accept-Encoding":"gzip, deflate, br",
"Connection":"keep-alive",
"Referer":"https://acgtt.cyou/",
# "Cookie":"lailu=xz_7kY0; stime=2021_12_01_10_09_38; suourl=sssss.cyou; pages=MTYzODMyNDE4OA; YpyW_2132_saltkey=o3040PSx; YpyW_2132_lastvisit=1638320978; YpyW_2132_lastact=1638326503%09ptl.php%09",
"Upgrade-Insecure-Requests":"1",
"Sec-Fetch-Dest":"document",
"Sec-Fetch-Mode":"navigate",
"Sec-Fetch-Site":"cross-site",
"Pragma":"no-cache",
"Cache-Control":"no-cache"
}


proxies1 = {
    'https':'http://182.34.32.44:13456',
}

params1={
"mb":"ptl",
"pages":"MTYzODMyNjc0MQ",
"t":"eHpfN2tZMA",
"time":"2021_12_01_10_45_56",
"akey":"Sm91bmc",
"alog":"Sm91bmc",
"times":"0",
"suourl":"sssss.cyou"
}

r1 = requests.get('https://www.ip138.com/',
                  params=params1,
                  headers=headers1,
                  proxies=proxies1
                  )

print(r1.encoding)
print(r1.content)

with open('test.html','w',encoding="utf-8") as f:
    f.write(r1.text)
