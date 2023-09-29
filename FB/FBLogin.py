import time
import random
import sys
from tkinter import messagebox

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import DeleteHistory


# temp block
#-------------------------------------------------------
# //input[@id = 'email']
# //input[@id = 'pass']
# //button[@name = 'login']
# //
# //
# 
#-------------------------------------------------------


def FBLogin(driver,profile_name,profile_para,thread_ID,r_max,r_min):
    def ReadAcc():
        acclist = []
        with open("./FB/Account.txt", mode = 'r', encoding="utf-8") as read_text: 
            for line in read_text:
                line=line.strip('\n')   #去除換行
                line=line.strip('')   #去除開頭、結尾的空白
                acclist.append(line)

        return acclist[0],acclist[1]

    def body(driver,profile_name,profile_para,thread_ID):
        Email, Pass = ReadAcc()
        driver.get("https://zh-tw.facebook.com/")
        EmailField = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, "//input[@id = 'email']")))
        EmailField.click()
        time.sleep(round(random.uniform(r_min, r_max), 2))
        EmailField.send_keys(  Email  )
        time.sleep(round(random.uniform(r_min, r_max), 2))

        PassField = driver.find_element(By.XPATH, "//input[@id = 'pass']")
        PassField.click()
        time.sleep(round(random.uniform(r_min, r_max), 2))
        PassField.send_keys(  Pass  )
        time.sleep(round(random.uniform(r_min, r_max), 2))

        ConfirmBtn = driver.find_element(By.XPATH, "//button[@name = 'login']")
        ConfirmBtn.click()
        time.sleep(round(random.uniform(r_min, r_max), 2))

    # ====================  DeleteHistory  ==================== 
    # DeleteHistory.DeleteHistory(driver,profile_name,profile_para,thread_ID)
    # time.sleep(round(random.uniform(r_min, r_max), 2))

    # ====================  start process  ==================== 
    body(driver,profile_name,profile_para,thread_ID)