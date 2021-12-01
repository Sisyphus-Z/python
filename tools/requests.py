import os
import sys

import requests

#r = requests.get('http://httpbin.org/get')

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

headers1={
"Host": "acgdd.cyou",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0",
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
"Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
"Accept-Encoding": "gzip, deflate, br",
"Connection": "keep-alive",
"Referer": "https://acgtt.cyou/",
# "Cookie": "lailu=xz_7kY0; stime=2021_12_01_09_39_07; suourl=sssss.cyou; pages=MTYzODMyMjc0Mg; YpyW_2132_saltkey=w5gvQ021; YpyW_2132_lastvisit=1638319147; YpyW_2132_lastact=1638326746%09ptl.php%09",
"Upgrade-Insecure-Requests": "1",
"Sec-Fetch-Dest": "document",
"Sec-Fetch-Mode": "navigate",
"Sec-Fetch-Site": "cross-site",
"Pragma": "no-cache",
"Cache-Control": "no-cache"
}

url1='https://acgdd.cyou/ptl.php'

encoding1="gbk"

r1 = requests.get(url=url1,
                  params=params1,
                  headers=headers1
                  )
print("不使用代理ip访问成功")

print(r1.encoding)
print(r1.content)

with open('before_test.html', 'w', encoding=encoding1) as f:
    f.write(r1.text)



if os.path.exists('proxies.txt')==False:
    print("未找到代理ip文件，退出程序")
    sys.exit()



with open('proxies111.txt', 'r', encoding="utf-8") as f2:
    list1=f2.readlines()
for i in range(0,len(list1)):
    list1[i]=list1[i].replace("\n","")


for i in range(0,len(list1)):
    proxies1 = {
        "https": "http://"+list1[i],
    }

    print("http://"+list1[i],end=" ")

    try:
        r1 = requests.get(url=url1,
                  params=params1,
                  headers=headers1,
                  proxies=proxies1
                  )
        print("成功")



        with open(str(i)+'test.html', 'w', encoding=encoding1) as f:
            f.write(r1.text)

    except Exception as e:
        print("失败")
        print(e)



