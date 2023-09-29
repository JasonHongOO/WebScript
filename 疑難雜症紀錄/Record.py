import time
import math
import random
import os
import re
from concurrent.futures import ThreadPoolExecutor

import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException

# 目錄
# 1 selnium
# 2 字串更新
# 3 正則化，尋找字串
# 4 ThreadPool

# 常用
# c = sys.stdin.read(1)         #等待按鈕



#  ===============================================================================================================================================
#  ===============================================================================================================================================
#  ===============================================================================================================================================
# 1
# chrome_options = Options()
# chrome_options.add_argument("profile_para")
# chrome_options.add_argument('--user-data-dir='+ "Chrome_base_address" + 'User Data/')
# chrome_options.add_argument("--auto-open-devtools-for-tabs")          # 相當於按 F12，查看網頁元素
# chrome_options.add_argument('--headless')                             # 無痕
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)
# uc.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)                    # undetected-chromedriver 用法

# ele = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//input[@name ='Passwd']")))
# ele = WebDriverWait(driver, 5).until(EC.visibility_of_any_elements_located((By.XPATH, "//input[@name ='Passwd']")))         # ele 可以看見
# ele = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//input[@name ='Passwd']")))                # ele 有出現
# ele = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//input[@name ='Passwd']"))).click()     #按鈕可以按

# ele.click() #一般點擊
# driver.execute_script ("arguments[0].click();", ele) # Element 用 JavaScript 強制點擊


# try:
# except NoSuchElementException:
# except TimeoutException as ex:            # driver.set_page_load_timeout(30) 常搭配使用
# else:

# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  #往下滾
# driver.refresh()


#  ===============================================================================================================================================
#  ===============================================================================================================================================
#  ===============================================================================================================================================
# 2
# \r moves the cursor to the beginning of the line

# UP = "\x1B[3A"
# CLR = "\x1B[0K"

# Count = 0
# while Count < 10000:   
#     # print(f"{UP} First String {Count} {CLR}\n Secound String{CLR}\n")
#     # print(f"First {Count}", end='\r')
#     # print(f"\rFirst {Count}", end='')                           
#     Count = Count + 1



#  ===============================================================================================================================================
#  ===============================================================================================================================================
#  ===============================================================================================================================================
# 3
# def extract_numbers(text):
#     numbers = re.findall(r'\d+', text)
#     print(numbers)
#     return int(numbers[0]) if numbers else None

# def extract_chinese_numbers(text):
#     pattern = r'第[一二三四五六七八九十零]+章'
#     matches = re.findall(pattern, (text))
#     print(matches)
#     return matches[0]

# text = "ascine 第第五章 91645 第六章 48653"
# print(extract_numbers(text))
# print(extract_chinese_numbers(text))



#  ===============================================================================================================================================
#  ===============================================================================================================================================
#  ===============================================================================================================================================
# 4
# MaxParallel = 5
# TotalNumber = 10

# ResultRecord = []
# para1 = 1
# para2 = 2
# para3 = 3
# para4 = 4
# with ThreadPoolExecutor(max_workers=MaxParallel) as ex:
#     for ii in range(TotalNumber):
#             ResultRecord.append(ex.submit(para1, para2, para3, para4))

#     print("\n//////////////////////////////////////////////////////////////////////////")
#     print("///////////////////////         結束          ////////////////////////////")
#     print("//////////////////////////////////////////////////////////////////////////")

# for ThreadPoolReturn in ResultRecord:
#     print(ThreadPoolReturn.result())  # ThreadPool 回傳的東西是由使用者決定的，在 Thread 裡面回傳甚麼，外面就會接收到甚麼

#  ===============================================================================================================================================
#  ===============================================================================================================================================
#  ===============================================================================================================================================
# 5


#  ===============================================================================================================================================
#  ===============================================================================================================================================
#  ===============================================================================================================================================
# 6


#  ===============================================================================================================================================
#  ===============================================================================================================================================
#  ===============================================================================================================================================
# 7




def extract_alpha_numeric(text):
    pattern = r'[a-zA-Z0-9]+'
    result = re.findall(pattern, text)[0]
    return result



print(type(extract_alpha_numeric("5sa165sacasc, 歡迎回來")))