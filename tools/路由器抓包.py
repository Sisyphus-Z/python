from selenium import webdriver
import time

def main1():

    #装饰器
    def w1(f):
        def w2():
            while 1:
                time.sleep(0.5)

                try:
                    f()
                    break
                except:

                    pass
        return w2




    # 启动Chrome浏览器
    driver = webdriver.Chrome()
    driver.maximize_window()

    # 在浏览器内输入网址，并且打开网址
    driver.get('http://192.168.3.1/')

    #等待浏览器加载完毕
    while 1:
        time.sleep(0.5)
        try:
            x = driver.find_element_by_xpath("//div[@id='copyrightHuawei']")

            break
        except:
            pass

    def denglu():
        @w1
        def f():
            x = driver.find_element_by_xpath("//input[@id='userpassword_ctrl']")
            x.clear()
            x.send_keys('11111111')
        f()

        @w1
        def f():
            x = driver.find_element_by_xpath("//div[@id='loginbtn']")
            x.click()
        f()
        time.sleep(0.4)


    def zhuabao():
        @w1
        def f():
            x = driver.find_element_by_xpath("//li[@id='more']/p[@class='nav_title']")
            x.click()
        f()

        @w1
        def f():
            x = driver.find_element_by_xpath("//div[@id='systemsettingsparent_menuId']")
            x.click()
        f()

        @w1
        def f():
            x = driver.find_element_by_xpath("//li[@id='mirror_menuId']")
            x.click()
        f()

        @w1
        def f():
            x = driver.find_element_by_xpath("//div[@id='mirrir_btn']")
            x.click()
        f()

        time.sleep(10)

        @w1
        def f():
            x = driver.find_element_by_xpath("//div[@id='mirrir_btn']")
            x.click()

        f()

        time.sleep(4)





    denglu()

    zhuabao()

    driver.close()

    driver.quit()



#main1()

