import uiautomator2 as u2
from time import sleep
d = u2.connect("输入设备号或手机IP")  # 连接手机

d.app_start("com.ss.android.ugc.aweme")  # 启动APP

def position(video_no):
    while True:
        if d.xpath('//*[@content-desc="视频{}"]'.format(video_no)).exists:  # 判断指定的视频是否存在
            d.xpath('//*[@content-desc="视频{}"]'.format(video_no)).click()  # 如果存在就点击
            break
        else:
            d.swipe_ext("up", 0.5)  # 如果不存在就从下往上滑动


if __name__ == "__main__":
    d(resourceId="com.ss.android.ugc.aweme:id/title").click()  # 点击抖音号名称
    position(10)  # 调用position 找到第10个视频
    for i in range(15):
        """从第10个视频开始往下点赞15个视频"""
        d(resourceId="com.ss.android.ugc.aweme:id/api").click()  # 点赞/点心
        sleep(1)
        d.swipe_ext("up", 0.5)  # 点完一个就滑动
    sleep(1)
    d.app_stop("com.ss.android.ugc.aweme")  # 关闭APP