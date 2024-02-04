from telnetlib import EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

控制台url = "https://www.autodl.com/console/instance/list"
租url = "https://www.autodl.com/create"

global username
global password


def xpath_find(driver, xpath):
    try:
        result = WebDriverWait(driver, 5, 0.5).until(EC.presence_of_element_located((By.XPATH, xpath)))
    except :
        print("报错的xpath"+xpath)


    return result
