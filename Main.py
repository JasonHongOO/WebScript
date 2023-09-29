import os
import time
from concurrent.futures import ThreadPoolExecutor

#drive
import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

#file import
#-------------------------------------------------------
import System.MultiThread
import System.ReadParameter
import MH.HappyMHSignUp
import BookContent
import FB.FBSignUp
import FB.FBLogin
import FB.FBMessage
import GetItem

import Google.GSignUp
import Google.GSignUpV2

import DeleteHistory
#-------------------------------------------------------


# temp block
#-------------------------------------------------------
# C:/Users/JasonHong/AppData/Local/Google/Chrome/'
#-------------------------------------------------------



# global variable
#-------------------------------------------------------
#幾個瀏覽器
browser_num = 1
#web user data 位置
Chrome_base_address = None
#random (max and min)
r_max = 0.5
r_min = 1.0
#task_mode 模式式甚麼    (0 測試 1 註冊 2 book)
task_mode = 0
#multi_web_mode 模式式甚麼    (0 關閉 1 開啟)
multi_web_mode = 1
browser_num_once = 1        #如開啟一次執行幾個網站
#multi_web_delete_mode   自動刪除額外檔案    (0 關閉 1 開啟)
multi_web_delete_mode = 1
#multi_profile_mode
multi_profile_mode = 0
#window_select_profile_mode
window_select_profile_mode = 0
#rest_profile_mode 
rest_profile_mode = 0
#使用者名稱
user_name = None


#URL 清單
web_list = []

#profile 資料
profile_para_list = []
profile_name_list = []
profile_address_list = []

#名子清單
name_list = []

#chapter 數量
chapter_num = 0

#-------------------------------------------------------
def decision_task(driver,profile_name,profile_para,thread_ID):
    global name_list,web_list
    global r_max,r_min
    global chapter_num,browser_num

    if(task_mode == 0):
        GetItem.get_item(driver,profile_name,profile_para,thread_ID)

    elif(task_mode == 1):
        for i in range(len(name_list)):     #或許產生隨機名子
            result = MH.HappyMHSignUp.Sign_Up(driver,profile_name,profile_para,thread_ID,i,name_list,r_max,r_min)
            if(result == -1): return -1
            driver.get(web_list[0]) #重新跳轉註冊頁面

    elif(task_mode == 2):
        BookContent.get_book_content(driver,profile_name,profile_para,thread_ID,chapter_num,browser_num)

    elif(task_mode == 3):
        FB.FBSignUp.Sign_Up(driver,profile_name,profile_para,thread_ID,r_max,r_min)
    elif(task_mode == 4):
        FB.FBMessage.LeaveAMessage(driver,profile_name,profile_para,thread_ID,r_max,r_min)

    elif(task_mode == 5):
        Google.GSignUpV2.Sign_Up(driver,profile_name,profile_para,thread_ID,r_max,r_min)

    elif(task_mode == 9998):
        FB.FBLogin.FBLogin(driver,profile_name,profile_para,thread_ID,r_max,r_min)
    elif(task_mode == 9999):
        DeleteHistory.DeleteHistory(driver,profile_name,profile_para,thread_ID)
    return 0

def open_site(profile_name,profile_para,thread_ID):
    global web_list
    global Chrome_base_address
    global task_mode
    global multi_profile_mode

    #options   
    chrome_options = uc.ChromeOptions()
    chrome_options.add_argument(profile_para) # 輸入相對應的參數，到不同帳號
    print("profile_para : " + profile_para)
    chrome_options.add_argument('--user-data-dir='+ Chrome_base_address + profile_para.split('=')[1])
    print('--user-data-dir = '+ Chrome_base_address + profile_para.split('=')[1])
    # chrome_options.add_argument('--no-sandbox')
    # chrome_options.add_argument('--disable-dev-shm-usage')
    # chrome_options.add_argument("--auto-open-devtools-for-tabs")
    # chrome_options.add_argument('--headless')
    # chrome_options.add_experimental_option('excludeSwitches',['enable-logging'])    #關閉警告訊息

    #驅動 drive
    # if multi_profile_mode == 1 : driver = uc.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)
    if multi_profile_mode == 1 : driver = uc.Chrome(options=chrome_options)
    # elif multi_profile_mode == 0 : driver = uc.Chrome(service=Service(ChromeDriverManager().install()))
    elif multi_profile_mode == 0 : driver = uc.Chrome()
    driver.maximize_window()    #全螢幕

    #開啟目標網站
    driver.get(web_list[0])
    # time.sleep(1.5)

    # decision task
    result = decision_task(driver,profile_name,profile_para,thread_ID)
    if(result == -1) : exit(1)
    # => result 提供額外判斷

    return thread_ID,profile_name,profile_para.split('=')[1],

def start_process():
    global multi_profile_mode
    futures = []
    with ThreadPoolExecutor(max_workers=browser_num_once) as ex:
        for ii in range(browser_num):
            if multi_profile_mode == 0:
                futures.append(ex.submit(open_site,profile_name_list[0],profile_para_list[0],ii))
            elif multi_profile_mode == 1:
                futures.append(ex.submit(open_site,profile_name_list[ii],profile_para_list[ii],ii))

    print("\n//////////////////////////////////////////////////////////////////////////")
    print("///////////////////////         結束          ////////////////////////////")
    print("//////////////////////////////////////////////////////////////////////////")
    for future in futures:
        print(future.result())  #印出執行完的那些 profile 名稱

#////////////////////////////////////////////////////////////////////////////////////////////////////

def prepare_process():
    folder_path = "./Output"
    print("\n============Outpur Folder Checker============")
    if not os.path.exists(folder_path):     # 檢查 Output 文件夾是否存在
        print("Output folder is not exist")
        print("Prepare to crate folder")
        os.makedirs(folder_path)            # 創建 Output 文件夾
        print("Creat folder completed")
    else:
        print("Output folder is already exist")

    print("\n============Folder Clear Checker============")
    files = os.listdir(folder_path)     # 檢查 Output 文件夾中是否存在文件
    if files:
        print("There are files present in the folder")
        for file_name in files:
            file_path = os.path.join(folder_path, file_name)    # 刪除 Output 文件夾中的所有文件
            os.remove(file_path)
        print("Clear folder completed")
    else:
        print("Output is empty")

def remain_process():
    global browser_num
    global task_mode

    if(task_mode == 2):
        content = ""
        for i in range(browser_num):
            with open("./Output/temp"+str(i)+".txt", 'r', encoding='utf-8') as f:
                content = content + f.read()

        with open("./Output/result.txt", 'w', encoding='utf-8') as output:
            output.write(content)

def main():
    global web_list, profile_para_list, profile_name_list, name_list
    global task_mode
    global browser_num, browser_num_once
    global Chrome_base_address
    global multi_web_mode, multi_profile_mode, window_select_profile_mode, rest_profile_mode 
    global user_name, chapter_num

    #process 開始前的準備
    prepare_process()
    browser_num, browser_num_once, task_mode, multi_web_mode, multi_web_delete_mode, multi_profile_mode, window_select_profile_mode, rest_profile_mode, Chrome_base_address, user_name, chapter_num = System.ReadParameter.read_config()
    browser_num, profile_name_list, profile_para_list = System.ReadParameter.read_profile(browser_num,window_select_profile_mode,multi_profile_mode)
    web_list = System.ReadParameter.readURL()
    name_list = System.ReadParameter.read_name()

    #多線程的準備
    if(multi_web_mode == 1):
        print("\n///////////////////////////////////////////////////////////////////////////////////////")
        print("/////////////////////////////  mult-thread 所需檔案準備中  /////////////////////////////")
        print("///////////////////////////////////////////////////////////////////////////////////////")
        System.MultiThread.multi_thread_preparations(browser_num,Chrome_base_address,profile_para_list)
        print("////////////////////////////////////////////////////////////////////////////////////////")
        print("//////////////////////////////    mult-thread 準備完成    //////////////////////////////")
        print("///////////////////////////////////////////////////////////////////////////////////////")

    #確認資料
    print("\n確認輸入資料是某正確")
    print("\n============profile_list============")
    for i in range(len(profile_para_list)):
        print(profile_name_list[i])
        print(profile_para_list[i])
    print("\n============web_list============")
    print(web_list)
    print("\n============name_list============")
    print(name_list)
    print("\n////////////////////////////////////////////////////////////////////////////")
    print("/////////////////////////////  Process Start  /////////////////////////////")
    print("//////////////////////////////////////////////////////////////////////////")
    if rest_profile_mode == 0 : start_process()

    #刪除多線程創建的所有檔案
    if(multi_web_delete_mode == 1):
        print("\n//////////////////////////////////////////////////////////////////////////////////////////")
        print("//////////////////////////////  mult-thread 所需檔案刪除中  //////////////////////////////")
        print("////////////////////////////////////////////////////////////////////////////////////////")
        System.MultiThread.multi_thread_file_delete(browser_num,Chrome_base_address,profile_para_list)
        print("////////////////////////////////////////////////////////////////////////////////////////")
        print("//////////////////////////////    mult-thread 刪除完成    //////////////////////////////")
        print("///////////////////////////////////////////////////////////////////////////////////////")

    #process 結束後剩餘的工作
    remain_process()

main()