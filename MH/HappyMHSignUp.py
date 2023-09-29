import time
import random
import string

from tkinter import messagebox

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def Sign_Up(driver,profile_name,profile_para,thread_ID,loot_cnt,name_list,r_max,r_min):
    def check_success():
        driver.get("https://m.happymh.com/user")
        user_name = driver.find_element(By.XPATH, "//p[@m-text = 'user.detail.username']")
        if (user_name.text == name): return 0
        else: return 1

    def write_account(acc_txt):
        with open("./MH/Account.txt" , mode = 'a') as write_text: 
            write_text.write(acc_txt + '\n')
            return 0

    def generate_random_string():
        max_len = 15
        min_len = 8
        length = random.randint(min_len , max_len)
        characters = string.ascii_letters + string.digits
        random_string = ''.join(random.choice(characters) for _ in range(length))
        return random_string
    
    #==================== email block ====================
    random_email = generate_random_string() + "@gmail.com"
    email_Field = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, "//input[@id = 'email']")))
    time.sleep(round(random.uniform(r_min, r_max), 2))
    email_Field.click()
    time.sleep(round(random.uniform(r_min, r_max), 2))
    email_Field.send_keys(random_email)

    #==================== name block ====================
    name = name_list[loot_cnt]
    email_Field = driver.find_element(By.XPATH, "//input[@id = 'username']")
    time.sleep(round(random.uniform(r_min, r_max), 2))
    email_Field.click()
    time.sleep(round(random.uniform(r_min, r_max), 2))
    email_Field.send_keys(name)

    #==================== icon block ====================
    icon_Field = driver.find_element(By.XPATH, "//i[@class = 'icon icon-plus-circle']")
    time.sleep(round(random.uniform(r_min, r_max), 2))
    icon_Field.click()
    icon_num = random.randint(1, 16)
    icon = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, "//div[@on = 'tap:MIP.setData({tmpCover:"+ str(icon_num) +"})']")))
    time.sleep(round(random.uniform(r_min, r_max), 2))
    icon.click()
    check_btn = driver.find_element(By.XPATH, "//span[@class = 'lightbox-close']")
    time.sleep(round(random.uniform(r_min, r_max), 2))
    check_btn.click()

    #==================== property block ====================
    gender_num = 1
    if (icon_num > 5 and icon_num <=8) or (icon_num > 11 and icon_num <=15):
        gender_num = 2

    property_num = random.randint(1, 3)
    property_btn = driver.find_element(By.XPATH, "//div[@option='" + str(gender_num) + str(property_num) +"']")
    time.sleep(round(random.uniform(r_min, r_max), 2))
    property_btn.click()

    #==================== password block ====================
    password_Field = driver.find_element(By.XPATH, "//input[@id = 'password']")
    time.sleep(round(random.uniform(r_min, r_max), 2))
    password_Field.click()
    time.sleep(round(random.uniform(r_min, r_max), 2))
    password_Field.send_keys("qeadzcwsx789725++")

    #====================  submit ==================== 
    submit_btn = driver.find_element(By.XPATH, "//button[@type = 'submit']")
    time.sleep(round(random.uniform(r_min, r_max), 2))
    submit_btn.click()

    #====================  check sign up success ==================== 
    time.sleep(2)
    check_result = check_success()
    if(check_result == 1):
        messagebox.showinfo(title="Error", message="Sign Up Failure")
        return -1

    #====================  log out ==================== 
    logout_btn = driver.find_element(By.XPATH, "//div[@class = 'logo-out']")
    time.sleep(round(random.uniform(r_min, r_max), 2))
    logout_btn.click()
    time.sleep(round(random.uniform(r_min, r_max), 2))
    logout_confirm_btn = driver.find_element(By.XPATH, "//span[@class = 'lightbox-close confirm']")
    time.sleep(round(random.uniform(r_min, r_max), 2))
    logout_confirm_btn.click()

    #====================  record account string ==================== 
    write_account(random_email)
    print("email : \t" + random_email)
    time.sleep(2)
    return 0
