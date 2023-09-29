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
import DeleteHistory

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
    UP = "\x1B[3A"
    CLR = "\x1B[0K"   

    def extract_numbers(text):
        numbers = re.findall(r'\d+', text)
        return int(numbers[0]) if numbers else None

    def SkipCaptcha():
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//div[@class ='x9f619 x1ja2u2z x1pq812k x5yr21d xw2csxc x1odjw0f xixxii4 x1rohswg x17qophe x13vifvy xh8yej3 xfk6m8 x1yqm8si xjx87ck']")))

        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.pause(1)
        actions.send_keys(Keys.ENTER)
        actions.pause(1)
        actions.send_keys(Keys.TAB)
        actions.pause(1)
        actions.send_keys(Keys.TAB)
        actions.pause(1)
        actions.send_keys(Keys.ENTER)
        actions.pause(1)
        actions.perform()

        CaptchaConfirm = driver.find_element(By.XPATH, "//div[@class ='x1n2onr6 x1ja2u2z x78zum5 x2lah0s xl56j7k x6s0dn4 xozqiw3 x1q0g3np xi112ho x17zwfj4 x585lrc x1403ito x972fbf xcfux6l x1qhh985 xm0m39n x9f619 xn6708d x1ye3gou xwcfey6 x1r1pt67']")
        CurWeb = driver.current_url
        while True:
            temp = driver.current_url
            if CurWeb == temp:
                CaptchaConfirm.click()
                time.sleep(5)
            else:
                break

    def CheckEmail():
        driver.switch_to.window(driver.window_handles[1])
    
        Count = 0
        while True :
            try:
                TargetMail = driver.find_elements(By.XPATH, "//a[@class='row-link']")

                if(TargetMail[0].text == '"Facebook" <registration@facebookmail.com>'):
                    print(f"{UP}Time : {Count} || Success recive FB emaill{CLR}\n Cur : {TargetMail[0].text}{CLR}\n")
                    break
                else:
                    print(f"{UP}Time : {Count} || Still waiting FB emaill{CLR}\n Cur : {TargetMail[0].text}{CLR}\n")
                    Count += 1

            except NoSuchElementException:
                pass

            time.sleep(1)

        TargetMail[0].click()#點擊信件

        state = 0
        try:
            TargetCode = WebDriverWait(driver, 4).until(EC.visibility_of_any_elements_located((By.XPATH, "//td[@style='font-size:20px;font-family:LucidaGrande, tahoma, verdana, arial, sans-serif;padding:10px;background-color:#f2f2f2;border-left:1px solid #ccc;border-right:1px solid #ccc;border-top:1px solid #ccc;border-bottom:1px solid #ccc;']")))
            TargetCode = int(TargetCode[0].text)
        except Exception as e:
            state = 1
            TargetCode = WebDriverWait(driver, 2).until(EC.visibility_of_any_elements_located((By.XPATH, "//span[@class='mb_text']")))
            TargetCode = extract_numbers(TargetCode[2].text)
            
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(round(random.uniform(r_min, r_max), 2))
        return TargetCode,state

    def GetFakeEmail():
        driver.switch_to.new_window('tab')
        time.sleep(1)
        driver.get("https://10minutemail.net/?lang=zh-tw")
        item = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, "//input[@id='fe_text']")))
        value = item.get_attribute("value")
        time.sleep(1)
        driver.switch_to.window(driver.window_handles[0])
        return value

    def generate_random_string(min_len = 8,max_len = 15):
        length = random.randint(min_len , max_len)
        characters = string.ascii_letters + string.digits
        random_string = ''.join(random.choice(characters) for _ in range(length))
        return random_string
    
    def ReadName():
        Name = []
        with open("./FB/En_Name.txt", mode = 'r', encoding="utf-8") as read_text: 
            for line in read_text:
                line=line.strip('\n')   #去除換行
                line=line.strip('')   #去除開頭、結尾的空白
                Name.append(line)
        
        return Name
    
    def AccountRecord(Email,Password):
        with open("./Account.txt" , mode = 'a') as write_text: 
            write_text.write(Email + '\t' + Password + '\n')
        
        return 0
    
    #==================== Initial ====================
    DeleteHistory.DeleteHistory(driver,profile_name,profile_para,thread_ID)
    NameList = ReadName()
    TempEmail = GetFakeEmail()
    time.sleep(2)
    

    #==================== Sign Up Account Btn ====================
    SignUpBtn = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, "//a[@class='_42ft _4jy0 _6lti _4jy6 _4jy2 selected _51sy']")))
    SignUpBtn.click()
    time.sleep(round(random.uniform(r_min, r_max), 2))

    #==================== Name ====================
    Lastname = WebDriverWait(driver, 4).until(EC.presence_of_element_located((By.XPATH, "//input[@name='lastname']")))
    Lastname.click()
    time.sleep(round(random.uniform(r_min, r_max), 2))
    Lastname.send_keys(  random.choice(NameList)  )
    time.sleep(round(random.uniform(r_min, r_max), 2))

    Firstname = driver.find_element(By.XPATH, "//input[@name='firstname']")
    Firstname.click()
    time.sleep(round(random.uniform(r_min, r_max), 2))
    Firstname.send_keys(  random.choice(NameList)  )
    time.sleep(round(random.uniform(r_min, r_max), 2))

    #==================== Email ====================
    EmailField = driver.find_element(By.XPATH, "//input[@name='reg_email__']")
    EmailField.click()
    time.sleep(round(random.uniform(r_min, r_max), 2))
    EmailField.send_keys(TempEmail)
    time.sleep(round(random.uniform(r_min, r_max), 2))

    EmailField = driver.find_element(By.XPATH, "//input[@name='reg_email_confirmation__']")
    EmailField.click()
    time.sleep(round(random.uniform(r_min, r_max), 2))
    EmailField.send_keys(TempEmail)
    time.sleep(round(random.uniform(r_min, r_max), 2))

    #==================== PassWord ====================
    PasswordField = driver.find_element(By.XPATH, "//input[@name='reg_passwd__']")
    PasswordField.click()
    time.sleep(round(random.uniform(r_min, r_max), 2))
    Temp_password = generate_random_string(10,20)
    PasswordField.send_keys(Temp_password)
    time.sleep(round(random.uniform(r_min, r_max), 2))

    #==================== Sign Up Account Btn ====================
    BirthdayYear_num = random.randint(1980, 2010)
    BirthdayYear = driver.find_element(By.XPATH, "//select[@name='birthday_year']//option[@value='" + str(BirthdayYear_num) + "']")
    BirthdayYear.click()
    time.sleep(round(random.uniform(r_min, r_max), 2))

    BirthdayMonth_num = random.randint(1, 12)
    BirthdayMonth = driver.find_element(By.XPATH, "//select[@name='birthday_month']//option[@value='" + str(BirthdayMonth_num) + "']")
    BirthdayMonth.click()
    time.sleep(round(random.uniform(r_min, r_max), 2))

    if(BirthdayMonth_num == 2) : BirthdayDay_num = random.randint(1, 28)
    else : BirthdayDay_num = random.randint(1, 30)
    BirthdayDay = driver.find_element(By.XPATH, "//select[@name='birthday_day']//option[@value='" + str(BirthdayDay_num) + "']")
    BirthdayDay.click()
    time.sleep(round(random.uniform(r_min, r_max), 2))

    #==================== Gender ====================
    Gender_num = random.randint(1, 2)
    GenderBtn = driver.find_element(By.XPATH, "//span[@class='_5k_2 _5dba']//input[@value='" + str(Gender_num) + "']")
    GenderBtn.click()
    time.sleep(round(random.uniform(r_min, r_max), 2))

    #==================== Submit ====================
    SubmitBtn = driver.find_element(By.XPATH, "//button[@type='submit'][@name='websubmit']")
    SubmitBtn.click()
    time.sleep(round(random.uniform(r_min, r_max), 2))

    #==================== Waiting Validation Email ====================

    state = 0
    try:
        state = 1

        BlockState = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, "//div[@class ='x9f619 x1n2onr6 x1ja2u2z x78zum5 xdt5ytf x1iyjqo2 x2lwn1j'][.//span[text() = '我們需要更多資料']]//div[@class='x9f619 x1n2onr6 x1ja2u2z x78zum5 xdt5ytf x193iq5w xeuugli x1iyjqo2 xs83m0k x150jy0e x1e558r4 xjkvuk6 x1iorvi4 xdl72j9']")))
        BlockState.click()
        time.sleep(round(random.uniform(r_min, r_max), 2))
        SkipCaptcha()
        ResendEmail = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, "//div[@class ='x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz xt0b8zv x1qq9wsj x1s688f']")))
        ResendEmail.click()
        time.sleep(round(random.uniform(r_min, r_max), 2))

    except Exception as e:
        state = 0
        print("fail : ",e)

    TargetCode,state = CheckEmail()
    print(TargetCode)



    #====================  Input Validation Code ====================
    if state == 0:
        CodeField = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//input[@id = 'code_in_cliff']")))
        CodeField.click()   
        time.sleep(round(random.uniform(r_min, r_max), 2))  
        CodeField.send_keys(TargetCode)
        time.sleep(round(random.uniform(r_min, r_max), 2))

        Confirm = driver.find_element(By.XPATH, "//button[@name = 'confirm']")
        CodeField.click()   
        time.sleep(round(random.uniform(r_min, r_max), 2))  
    
    elif state == 1:
        CodeField = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//input[@class ='x1i10hfl xggy1nq x1s07b3s x1kdt53j x1a2a7pz xjbqb8w x76ihet xwmqs3e x112ta8 xxxdfa6 x9f619 xzsf02u x1uxerd5 x1fcty0u x132q4wb x1a8lsjc x1pi30zi x1swvt13 x9desvi xh8yej3 x15h3p50 x10emqs4']")))
        CodeField.click()   
        time.sleep(round(random.uniform(r_min, r_max), 2))  
        CodeField.send_keys(TargetCode)
        time.sleep(round(random.uniform(r_min, r_max), 2))

        try:
            Confirm = driver.find_element(By.XPATH, "//div[@class = 'x1n2onr6 x1ja2u2z x78zum5 x2lah0s xl56j7k x6s0dn4 xozqiw3 x1q0g3np xi112ho x17zwfj4 x585lrc x1403ito x972fbf xcfux6l x1qhh985 xm0m39n x9f619 xn6708d x1ye3gou xtvsq51 x1r1pt67']")
            Confirm.click()   
            time.sleep(round(random.uniform(r_min, r_max), 2))  
        except Exception as e:
            print("找不到確認鍵")
        
    

    time.sleep(10)
    c = sys.stdin.read(1) 
    c = sys.stdin.read(1) 

    

    return 0
