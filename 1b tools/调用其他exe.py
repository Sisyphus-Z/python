import os

def main():
    # 改变工作目录
    os.chdir(r"E:\pythonProject2")

    path1 = r"1.exe"

    r_v = os.system(path1)

    print(r_v)


main()