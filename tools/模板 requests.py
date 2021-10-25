import requests

#r = requests.get('http://httpbin.org/get')

headers1={
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
"Accept-Encoding": "gzip, deflate, br",
"Accept-Language": "zh-CN,zh;q=0.9",
"Cache-Control": "no-cache",
"Connection": "keep-alive",
"Cookie": "BIDUPSID=7766A17CA486F80A029A202D00A2D194; PSTM=1599476753; BAIDUID=7766A17CA486F80A2652D141DA582DAB:FG=1; BD_UPN=12314753; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; delPer=0; BD_CK_SAM=1; BD_HOME=1; PSINO=7; H_PS_645EC=f37dviJS2%2By0kT%2Fkm0y4JJUDv9PjYC0mZC%2FqNX6RMBvGBJd1NOgeCRxlX7o; COOKIE_SESSION=494_0_6_1_6_12_0_0_4_2_0_1_455_0_476_0_1599891387_0_1599890911%7C6%230_0_1599890911%7C1; H_PS_PSSID=7540_32606_1450_7566_7580_7619_32117_32583",
"Host": "www.baidu.com",
"Pragma": "no-cache",
"Sec-Fetch-Dest": "document",
"Sec-Fetch-Mode": "navigate",
"Sec-Fetch-Site": "none",
"Sec-Fetch-User": "?1",
"Upgrade-Insecure-Requests": "1",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36"
}

r1 = requests.get('http://www.baidu.com',headers=headers1)

print(r1.encoding)
print(r1.content)

with open('test.html','w') as f:
    f.write(r1.text)
