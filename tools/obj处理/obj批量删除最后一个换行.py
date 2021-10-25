# 目标路径下的所有文件遍历，read读取每个时：
# 先查找最后一个\n的索引，用切片方式按索引删除它（加了xxxxx防止索引越界）
# 再write写入

# 发现python读取时，\r\n会被读取成\n；写入时，\n会被写入成\r\n，不知道是否是因为windows操作系统

import os

base_dir='要处理的文件\\项链'
file_list=os.listdir(base_dir)

for i in file_list:

    with open(base_dir+'\\'+i,'r') as f:
        ff=f.read()

        ff=ff+'xxxxx'
        index=ff.rfind('\n')
        if index != len(ff)-6:
            print('有错误！')
        fff=ff[0:index]+ff[index+1:-5]


    with open(base_dir + '\\' + i, 'w') as f:
        f.write(fff)


