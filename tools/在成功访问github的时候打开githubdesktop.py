from datetime import time
from urllib import request
import time
import webbrowser
import os
main_url = "https://github.com/"

def run():

    os.chdir(r"C:\Users\zbc\AppData\Local\GitHubDesktop")

    path1 = r"GitHubDesktop.exe"

    r_v = os.system(path1)

    print(r_v)

def main():
    while True:
        try:
            print('尝试')
            request.urlopen(url=main_url)
            break
        except Exception as e:
            print('连接失败')
            time.sleep(0.5)
    print('github可连接 !')

    run()



main()






