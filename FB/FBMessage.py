import time
import random
import sys
import re
from tkinter import messagebox

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import DeleteHistory
import FB.FBLogin

def LeaveAMessage(driver,profile_name,profile_para,thread_ID,r_max,r_min):
    #留言數量
    TotalMsgNum = 1
    MsgNameList = []
    PostIndexList = []

    def extract_numbers(text):
        numbers = re.findall(r'\d{1,3}(?:,\d{3})*', text)
        number_string = ''.join(numbers)
        return int(number_string.replace(',', '')) if number_string else None

    def ReadWeb():
        web_list = []
        with open("./FB/WEB.txt", mode = 'r', encoding="utf-8") as read_text: 
            for line in read_text:
                line=line.strip('\n')   #去除換行
                line=line.strip('')   #去除開頭、結尾的空白
                web_list.append(line)

        return web_list
    
    def WriteMsbRecord(PostIndex,Name):
        with open("./FB/MessageRecord.txt" , mode = 'a') as write_text: 

            write_text.write('PostIndex : ')
            for Index in PostIndex:
                write_text.write( str(Index) + ', ')
            write_text.write('\n')

            write_text.write('Name : \n')
            for name in Name:
                print("name")
                write_text.write(name + '\n')
            write_text.write('=========================================================\n')
        
        return 0

    def body(driver,profile_name,profile_para,thread_ID,r_max,r_min):
        WebList = ReadWeb()
        for web in WebList:         #不會判斷網站是否重複
            driver.get(web)

            #確認已載入網頁
            WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, "//ul[@class='xuk3077 x78zum5 x1iyjqo2 xl56j7k x1p8ty84 x1na7pl x88anuq']")))

            #滑到底
            for i in range(1):
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(random.uniform(r_min,r_max))
                
            #選出其中一篇文章
            PostList = driver.find_elements(By.XPATH, "//div[@class = 'x9f619 x1n2onr6 x1ja2u2z x78zum5 xdt5ytf x2lah0s x193iq5w xeuugli xsyo7zv x16hj40l x10b6aqq x1yrsyyn']//span[@class = 'x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x xudqn12 x3x7a5m x6prxxf xvq8zen xo1l8bm xi81zsa']")
            
            RandomPostNum = random.randint(0 , 2)           #注意!!! 只少要有 3 篇貼文，不然就出錯
            PostIndex = RandomPostNum
            PostIndexList.append(PostIndex)
            time.sleep(random.uniform(r_min,r_max))

            print("PostIndex : ",PostIndex)

            #確認文章的留言數     
            try:
                PostMsgNumTemp = driver.find_elements(By.XPATH, "//span[@class = 'x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x xudqn12 x3x7a5m x6prxxf xvq8zen xo1l8bm xi81zsa']")
                PostMsgNum = extract_numbers(PostMsgNumTemp[0 + PostIndex * 2].text)
                time.sleep(random.uniform(r_min,r_max))
            except Exception as e:
                PostMsgNum = 0

            print(PostMsgNum)

            if PostMsgNum != 0:
                #查看更多留言
                # PostBtn = Post.find_element(By.XPATH, "//span[@class='x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x xudqn12 x3x7a5m x6prxxf xvq8zen x1s688f xi81zsa'][text() = '查看更多留言']")
                PostBtn = PostList[0]
                # PostBtn.click()
                driver.execute_script ("arguments[0].click();",PostBtn)
                time.sleep(random.uniform(r_min,r_max))

                #選出留言
                    #調成所有留言
                MoreMsgBtn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//span[@class = 'x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x xudqn12 x3x7a5m x6prxxf xvq8zen x1s688f xi81zsa'][text() = '最相關留言']")))
                MoreMsgBtn.click()
                time.sleep(random.uniform(r_min,r_max))

                AllMsgBtn = WebDriverWait(driver, 10).until(EC.visibility_of_any_elements_located((By.XPATH, "//div[@class = 'x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou xe8uvvx x1hl2dhg xggy1nq x1o1ewxj x3x9cwd x1e5q0jg x13rtm0m x87ps6o x1lku1pv x1a2a7pz xjyslct x9f619 x1ypdohk x78zum5 x1q0g3np x2lah0s xnqzcj9 x1gh759c xdj266r xat24cr x1344otq x1de53dj xz9dl7a xsag5q8 x1n2onr6 x16tdsg8 x1ja2u2z x6s0dn4']")))[2]
                AllMsgBtn.click()
                time.sleep(random.uniform(r_min,r_max))

                    #調出更多留言 (目前最多就 2 次)
                Count = 0
                while True:
                    try:
                        ShowPreMsgBtn = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "//span[@class = 'x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x xudqn12 x3x7a5m x6prxxf xvq8zen x1s688f xi81zsa'][text() = '顯示先前的留言']")))
                    except Exception as e:
                        print(e)
                        break

                    if Count == 2:
                        break
                    else:
                        ShowPreMsgBtn.click()
                        time.sleep(random.uniform(r_min,r_max))
                    Count += 1 

                    #選出其中一則留言
                TotalBlockT = WebDriverWait(driver, 2).until(EC.visibility_of_any_elements_located((By.XPATH, "//div[@class = 'x1n2onr6 x1iorvi4 x4uap5 x18d9i69 x1swvt13 x78zum5 x1q0g3np x1a2a7pz']")))
                TotalBlock = TotalBlockT[0].find_element(By.XPATH, "..")

                # AllMsg = TotalBlock.find_elements(By.XPATH, "//div[@class = 'x1r8uery x1iyjqo2 x6ikm8r x10wlt62 x1pi30zi']")      #範圍縮小
                
                    #誰的留言
                WhosMsg = TotalBlock.find_elements(By.XPATH, "//div[@class = 'x1r8uery x1iyjqo2 x6ikm8r x10wlt62 x1pi30zi']//span[@class = 'x3nfvp2']")
                RandomMsgNum = random.sample(range(0, len(WhosMsg)), TotalMsgNum)
                                
                for RandomNum in RandomMsgNum:
                    MsgNameList.append(WhosMsg[RandomNum].text)
                    print("WhosMsg : ",WhosMsg[RandomNum].text)

                    #回覆留言(照片)
                    ReplyMsgBtn = TotalBlock.find_elements(By.XPATH, "//li[@class = 'x1rg5ohu x1emribx x1i64zmx']//div[text() = '回覆']")
                    ReplyMsgBtn[RandomNum].click()
                    time.sleep(random.uniform(r_min,r_max))

                        #上傳照片(只會偵測以點擊"回覆"按鈕後展開的輸入空間)
                    ReplyFeild = TotalBlock.find_elements(By.XPATH, "//input[@class = 'x1s85apg']")
                    ReplyFeild[1].send_keys("C:\\Users\\JasonHong\\Desktop\\College\\海綿\\真的好想好想要.jpg")


                c = sys.stdin.read(1) 

                #頁面挑選、訊息送出
            else :
                print("No one leave message (Skip This Post)")

        WriteMsbRecord(PostIndexList,MsgNameList)


    # ====================  DeleteHistory  ==================== 
    # DeleteHistory.DeleteHistory(driver,profile_name,profile_para,thread_ID)
    # ====================  FB Login  ==================== 
    # FB.FBLogin.FBLogin(driver,profile_name,profile_para,thread_ID,r_max,r_min)
 
    # ====================  start process  ==================== 
    body(driver,profile_name,profile_para,thread_ID,r_max,r_min)



# c = sys.stdin.read(1) 
# c = sys.stdin.read(1) 