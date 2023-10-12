import requests
import base64

def get_access_token():
    url = 'https://aip.baidubce.com/oauth/2.0/token'
    data = {
        'grant_type': 'client_credentials',  # 固定值
        'client_id': '8GQWCcD7IGNnp0QUaaM3Rc7t',  # 在开放平台注册后所建应用的API Key
        'client_secret': 'emyPLg6NifYylqzb68jPkIW5Ek12YmHs'  # 所建应用的Secret Key
    }
    res = requests.post(url, data=data)
    res = res.json()
    print(res)
    access_token = res['access_token']
    return access_token


#通用文字识别
def general_word():
    #通用文字识别接口url
    general_word_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic"
    #获取执行路径
    # path = os.getcwd()
    # 二进制方式打开图片文件
    f = open('5.jpg', 'rb')
    img = base64.b64encode(f.read())
    print(img)
    params = {"image":img,
              "language_type":"CHN_ENG"}
    access_token = get_access_token()
    request_url = general_word_url + "?access_token=" + access_token
    print(request_url)
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    # print(response)
    # res = response.json()
    if response:
        print(11111111111111,response.json())
        res = response.json()["words_result"]
        print(res)
        file_name = "zbc.txt"
        with open(file_name, 'w', encoding='utf-8') as f:
            for j in res:
                print(j["words"])
                f.write(j["words"]+"\n")


#身份证识别
def idcard():
    idcard_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/idcard"
    # 二进制方式打开图片文件
    f = open('4.jpg', 'rb')
    img = base64.b64encode(f.read())

    params = {"id_card_side":"front","image":img}
    access_token = get_access_token()
    request_url = idcard_url + "?access_token=" + access_token
    print(request_url)
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    if response:
        res = response.json()["words_result"]
        file_name = "菜鸟小白的学习分享.txt"
        with open(file_name, 'w', encoding='utf-8') as f:
            f.write("住址："+res["住址"]["words"]+"\n")
            f.write("出生日期：" + res["出生"]["words"] + "\n")
            f.write("姓名：" + res["姓名"]["words"] + "\n")
            f.write("公民身份号码：" + res["公民身份号码"]["words"] + "\n")
            f.write("性别：" + res["性别"]["words"] + "\n")
            f.write("民族：" + res["民族"]["words"] + "\n")

if __name__ == '__main__':
    #idcard()
    general_word()