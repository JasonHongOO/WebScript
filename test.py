from selenium import webdriver
import undetected_chromedriver as uc
import time
import math
import random
# # 初始化 Selenium WebDriver
# # driver = webdriver.Chrome()
# driver = uc.Chrome()
# # 打開網頁
# driver.get('https://m.happymh.com/')  # 將網站的 URL 替換為您想要開啟的網站

# # 可以在這裡進行進一步的網頁操作，例如點擊連結、填寫表單等

# time.sleep(1000)
# # 關閉瀏覽器n
# driver.quit()

# import re

# UP = "\x1B[3A"
# CLR = "\x1B[0K"

# print("orders : 1")
# print("orders : 1")

# for i in range(1000000):
#     # print("ok")
#     print(f"{UP}Orders: {i}{CLR}\nOperations: {i+1}{CLR}\n")




# from selenium import webdriver
# 

# proxy = '91.209.11.131:80' #step1:setup your ip
# timeoutSec = 50 #step2:setup your timeout spec(sec)
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--proxy-server=http://' + proxy) 
# driver = webdriver.Chrome(options=chrome_options)
# # driver = webdriver.Chrome()
# # driver.set_page_load_timeout(timeoutSec)
# try:
#     driver.get('https://www.youtube.com/')
# except Exception as e:
#     print(e)
#     print('fail to get request from ip via selenium+proxy')




# import sys
# from selenium import webdriver

# proxy_address = "91.209.11.131:80"
# proxy = webdriver.Proxy()
# proxy.proxy_type = webdriver.common.proxy.ProxyType.MANUAL
# proxy.http_proxy = proxy_address
# proxy.ssl_proxy = proxy_address

# # 创建 WebDriver 对象，并将代理设置为选项
# options = webdriver.ChromeOptions()
# options.add_argument("--proxy-server={}".format(proxy_address))
# driver = webdriver.Chrome(options=options)



# c = sys.stdin.read(1) 
# c = sys.stdin.read(1) 





import tkinter as tk
import pyautogui
import subprocess

# # 创建 tkinter 窗口
# window = tk.Tk()
# window.title("Always On Top Button")

# # 创建按钮
# button = tk.Button(window, text="执行程序")

# # 将窗口置顶
# window.wm_attributes("-topmost", 1)

# # 设置按钮点击事件
# def execute_program():
#     # subprocess.Popen(["python", "C:\\Users\\JasonHong\\Desktop\\main.py"])
#     print("print")

# button.configure(command=execute_program)
# button.pack()

# # 获取屏幕尺寸
# screen_width = window.winfo_screenwidth()
# screen_height = window.winfo_screenheight()

# # 设置按钮初始位置
# button_width = 100
# button_height = 30
# button_x = screen_width - button_width - 10
# button_y = screen_height - button_height - 10

# # 移动按钮到初始位置
# window.geometry(f"{button_width}x{button_height}+{button_x}+{button_y}")


