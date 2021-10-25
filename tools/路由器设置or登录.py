from selenium import webdriver
import time

def main1():
    statue = 9


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


    #判断是登录还是向导
    while 1:
        time.sleep(0.5)
        try:
            x=driver.find_element_by_xpath("//input[@id='userpassword_ctrl']")
            statue =1
            break
        except:
            pass

        try:
            x=driver.find_element_by_xpath("//div[@id='show_welcome']")
            statue =0
            break
        except:
            pass

        try:
            x=driver.find_element_by_xpath("//label[ @ id = 'guide_user_agree_ctrl_checkbox_ctrl']")
            statue =0
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
        time.sleep(1)

    def xiangdao():
        #可能有推荐安装智慧生活
        count =0
        while 1:
            if count>=4:
                break
            time.sleep(1)
            try:
                x = driver.find_element_by_xpath("//div[@id='show_welcome']")
                x.click()
                break
            except:
                count+=1
                pass



        #
        @w1
        def f():
            x=driver.find_element_by_xpath("//label[ @ id = 'guide_user_agree_ctrl_checkbox_ctrl']")
            x.click()
        f()

        #开始配置
        @w1
        def f():
            x=driver.find_element_by_xpath("//div[@id='guidebtnbegin']")
            x.click()
        f()


        @w1
        def f():
            x=driver.find_element_by_xpath("//label[@id='IP_Routed_radioctrl_checkbox_ctrl_checkbox_ctrl']")
            x.click()
        f()

        @w1
        def f():
            x=driver.find_element_by_xpath("//div[@id='nextButton']")
            x.click()
        f()

        @w1
        def f():
            x=driver.find_element_by_xpath("//input[@id='SsidSettings_guide_wifi_name_ctrl']")
            x.clear()
            x.send_keys('!!!!!!!!')
            #!嘿嘿我是第一个感叹号
        f()

        @w1
        def f():
            x=driver.find_element_by_xpath("//input[@id='SsidSettings_guide_wifi_password_ctrl']")

            x.clear()
            x.send_keys('11111111')
        f()

        @w1
        def f():
            x=driver.find_element_by_xpath("//div[@id='SsidSettings_guide_login_setpwd_check_ctrl_checkbox_option']")
            x.click()
        f()


        @w1
        def f():
            x=driver.find_element_by_xpath("//div[@id='wififinishbtn']")
            x.click()
        f()


        #倒数第一步
        @w1
        def f():
            x=driver.find_element_by_xpath("//div[@id='accountfinishbtn']")
            x.click()
        f()

        #等待完成
        @w1
        def f():
            x=driver.find_element_by_xpath("//div[@id='sync_last_btn']")
            x.click()
        f()

    if statue==0:
        xiangdao()

    if statue==1:
        denglu()

    #driver.close()
    #time.sleep(3)
    #driver.switch_to.window(driver.window_handles[0])
    #driver.close()
    #time.sleep(3)
    #driver.quit()