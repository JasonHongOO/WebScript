import time
import random
import string
import sys
import re
from tkinter import messagebox

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import StaleElementReferenceException
import DeleteHistory
import GetPhoneNumber



# temp block
#-------------------------------------------------------
# //input[@name='lastname']
# //input[@name='firstname']
# //input[@name='reg_email__']
# //input[@name='reg_passwd__']
# //select[@name='birthday_year']//option[@value='2021']
# 
#-------------------------------------------------------

def Sign_Up(driver,profile_name,profile_para,thread_ID,r_max,r_min):
    Year = "1990"
    Month = "6"
    Day = "22"
    PassWord = "ta789725"

    def WriteRecord(Info):
        with open("./Google/Account.txt" , mode = 'a', encoding='utf-8') as write_text: 
            write_text.write(Info[0].text + '\n')
            write_text.write(Info[1].text + '\n')
            write_text.write(Info[2].text + '\n')
            write_text.write(Info[3].text + '\n')
            write_text.write(PassWord + '\n')
            write_text.write("\n")
            return 0

    def Check(Xpath):
        try:
                time.sleep(4)
                driver.find_element(By.XPATH, Xpath)
                return 1
        except:
                return 0
        
    def extract_alpha_numeric(text):
        pattern = r'[a-zA-Z0-9]+'
        result = re.findall(pattern, text)[0]
        return result

    def extract_numbers(text):
        numbers = re.findall(r'\d+', text)
        return int(numbers[0]) if numbers else None

    def generate_random_string(min_len = 5,max_len = 5):
        length = random.randint(min_len , max_len)
        characters = string.ascii_lowercase
        random_string = ''.join(random.choice(characters) for _ in range(length))
        return random_string
    
    def ReadPhoneNumber():
        PhoneNumber = []
        with open("./Google/PhoneNumber.txt", mode = 'r', encoding="utf-8") as read_text: 
            for line in read_text:
                line=line.strip('\n')   #去除換行
                line=line.strip('')   #去除開頭、結尾的空白
                PhoneNumber.append(line)
        
        return PhoneNumber
    
    def body(driver,profile_name,profile_para,thread_ID,r_max,r_min,PhoneNumberList):
        TerminalCnt = 0
        MaxTerminalCnt = 10

        driver.get("https://www.google.com/intl/zh-TW/account/about/")

        #====================  CreatBtn  ====================
        while True :
            CreatAccBtn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[@class='h-c-header__cta-li-link h-c-header__cta-li-link--secondary button-standard-mobile']")))
            # CreatAccBtn.click()
            driver.execute_script ("arguments[0].click();", CreatAccBtn)
            time.sleep(round(random.uniform(r_min, r_max), 2))

            #====================  Check  ====================          (保險機制)

            break 
            # if(Check("//a[@class='h-c-header__cta-li-link h-c-header__cta-li-link--secondary button-standard-mobile']") == 0) : 
            #     TerminalCnt = 0
            #     break          
            # else :
            #     print(f"CreatBtn Failed {TerminalCnt}", end = '\r')
            #     TerminalCnt = TerminalCnt + 1
            #     if(TerminalCnt == MaxTerminalCnt) : exit(1)




        #====================  Name  ====================
        LastName = generate_random_string()
        FirstName = generate_random_string()

        LastNameField = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//input[@name = 'lastName']")))
        LastNameField.click()
        time.sleep(round(random.uniform(r_min, r_max), 2))
        LastNameField.send_keys(  LastName  )
        time.sleep(round(random.uniform(r_min, r_max), 2))

        FirstNameField = driver.find_element(By.XPATH, "//input[@name = 'firstName']")
        FirstNameField.click()
        time.sleep(round(random.uniform(r_min, r_max), 2))
        FirstNameField.send_keys(  FirstName  )
        time.sleep(round(random.uniform(r_min, r_max), 2))

        #====================  Comfirm  ====================
        ContinueBtn = driver.find_element(By.XPATH, "//span[@class ='VfPpkd-vQzf8d']")
        ContinueBtn.click()
        time.sleep(round(random.uniform(r_min, r_max), 2))






        #====================  Birthday、Gender  ====================
        driver.refresh()
        try :
            YearField = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//input[@id = 'year']")))
            # YearField.click()
            driver.execute_script ("arguments[0].click();", YearField)
            time.sleep(round(random.uniform(r_min, r_max), 2))
            YearField.send_keys(  Year  )
            time.sleep(round(random.uniform(r_min, r_max), 2))

            MonthField = driver.find_element(By.XPATH, "//option[@value = '" + Month + "']")
            MonthField.click()
            time.sleep(round(random.uniform(r_min, r_max), 2))

            DayField = driver.find_element(By.XPATH, "//input[@name = 'day']")
            DayField.click()
            time.sleep(round(random.uniform(r_min, r_max), 2))
            DayField.send_keys(  Day  )
            time.sleep(round(random.uniform(r_min, r_max), 2))

            GenderField = driver.find_element(By.XPATH, "//select[@id = 'gender']/option[@value = '2']")
            GenderField.click()
            time.sleep(round(random.uniform(r_min, r_max), 2))

            #====================  Comfirm  ====================
            ContinueBtn_2 = driver.find_element(By.XPATH, "//span[@class ='VfPpkd-vQzf8d'][text() = '繼續']")
            ContinueBtn_2.click()
            time.sleep(round(random.uniform(r_min, r_max), 2))

        except TimeoutException as ex:
            print(f"Birthday、Gender : {ex}")
            c = sys.stdin.read(1) 
            c = sys.stdin.read(1) 




        #====================  EmailSelect  ====================

        try :
            EmailSelect = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@id = 'selectionc0']")))
            # EmailSelect = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@id = 'selectionc0']")))
            EmailSelect.click()
            time.sleep(round(random.uniform(r_min, r_max), 2))

            #====================  Comfirm  ====================
            ContinueBtn_3 = driver.find_element(By.XPATH, "//span[@class ='VfPpkd-vQzf8d'][text() = '繼續']")
            ContinueBtn_3.click()
            time.sleep(round(random.uniform(r_min, r_max), 2))

        except Exception as e:
            print("跳出來 : 要手動輸入 Email")
            EmailField = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@name = 'Username']")))
            driver.execute_script ("arguments[0].click();", EmailField)
            time.sleep(round(random.uniform(r_min, r_max), 2))
            EmailField.send_keys(  FirstName + LastName  )
            time.sleep(round(random.uniform(r_min, r_max), 2))


            # actions = ActionChains(driver)
            # actions.send_keys(Keys.TAB)
            # actions.pause(1)
            # actions.send_keys(FirstName + LastName)
            # actions.pause(1)
            # actions.perform()
            # time.sleep(round(random.uniform(r_min, r_max), 2))
            #====================  Comfirm  ====================
            ContinueBtn_3 = driver.find_element(By.XPATH, "//span[@class ='VfPpkd-vQzf8d'][text() = '繼續']")
            ContinueBtn_3.click()
            time.sleep(round(random.uniform(r_min, r_max), 2))



        #====================  PassWord  ====================
        PassWordField = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//input[@name ='Passwd']")))
        PassWordField.click()
        time.sleep(round(random.uniform(r_min, r_max), 2))
        PassWordField.send_keys(  PassWord  )
        time.sleep(round(random.uniform(r_min, r_max), 2))

        PassWordField_2 = driver.find_element(By.XPATH, "//input[@name ='PasswdAgain']")
        PassWordField_2.click()
        time.sleep(round(random.uniform(r_min, r_max), 2))
        PassWordField_2.send_keys(  PassWord  )
        time.sleep(round(random.uniform(r_min, r_max), 2))

            #====================  Comfirm  ====================
        ContinueBtn_4 = driver.find_element(By.XPATH, "//span[@class ='VfPpkd-vQzf8d'][text() = '繼續']")
        ContinueBtn_4.click()
        time.sleep(round(random.uniform(r_min, r_max), 2))




        #====================  Recovery Email (Option)  ====================  
        try:   
            WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//h1//span[text()='新增備援電子郵件地址']")))
            #上面有出現，才會執行這一步
            SkipBtn = driver.find_element(By.XPATH, "//span[text() = '略過']").click()
            time.sleep(round(random.uniform(r_min, r_max), 2))
        except Exception as e:
            print("Error(Recovery Email) : ",e)
            c = sys.stdin.read(1)
            c = sys.stdin.read(1)
            pass


        #====================  PhoneNumber  ====================
        SkipBtn = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//span[text() = '略過']"))).click()
        time.sleep(round(random.uniform(r_min, r_max), 2))

        #====================  Check Account Info  ====================
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//h1//span[text() = '查看您的帳戶資訊']")))
            #====================  Comfirm  ====================
        driver.find_element(By.XPATH, "//span[@class ='VfPpkd-vQzf8d'][text() = '繼續']").click()
        time.sleep(round(random.uniform(r_min, r_max), 2))

        #====================  Privacy Policy and Terms  ====================
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//h1//span[text() = '隱私權與條款']")))
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//span[text() = '更多選項']"))).click()
        time.sleep(round(random.uniform(r_min, r_max), 2))
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//div[text() = '不要將我的「網路和應用程式活動」儲存到我的 Google 帳戶']"))).click()
        time.sleep(round(random.uniform(r_min, r_max), 2))
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//div[text() = '顯示非個人化廣告']"))).click()
        time.sleep(round(random.uniform(r_min, r_max), 2))
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//div[text() = '不要將我的 YouTube 記錄儲存到 Google 帳戶中']"))).click()
        time.sleep(round(random.uniform(r_min, r_max), 2))

            #====================  Comfirm  ====================
        driver.find_element(By.XPATH, "//span[@class ='VfPpkd-vQzf8d'][text() = '我同意']").click()
        time.sleep(round(random.uniform(r_min, r_max), 2))
        


        #====================  Acount Info Prepare  ====================
        driver.get("https://myaccount.google.com/personal-info")
        driver.refresh()
        c = sys.stdin.read(1) 
        c = sys.stdin.read(1) 
        AccountInfo = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//div[@class='bJCr1d']")))
            
        WriteRecord(AccountInfo)    #1234
        
        
    
    #==================== Initial ====================
    # DeleteHistory.DeleteHistory(driver,profile_name,profile_para,thread_ID) 
    # time.sleep(2)

    # 從文字檔內讀取
    # PhoneNumberList = ReadPhoneNumber()
    #直接開網頁去拿
    PhoneNumberList = GetPhoneNumber.GetPhoneNumber(driver,profile_name,profile_para,thread_ID)
    print(len(PhoneNumberList))
    print(PhoneNumberList)
    body(driver,profile_name,profile_para,thread_ID,r_max,r_min,PhoneNumberList)


    c = sys.stdin.read(1) 
    c = sys.stdin.read(1) 

    

    return 0
