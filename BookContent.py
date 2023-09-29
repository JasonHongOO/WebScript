import math 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_book_content(driver,profile_name,profile_para,thread_ID,chapter_num,browser_num):
    chapter_web = []

    def get_all_web():
        first_item = WebDriverWait(driver, 2).until(EC.visibility_of_any_elements_located((By.XPATH, "//ul[@class='chapterlist']//a")))[0]
        link_url = first_item.get_attribute("href")

        split_parts = link_url.split("/")
        prefix = split_parts[0] + "/" + split_parts[1] + "/" + split_parts[2] + "/" + split_parts[3] + "/" + split_parts[4] + "/"
        chapter_id = int(split_parts[5])

        for i in range(chapter_num):
            chapter_web.append(prefix + str(chapter_id+i))

    def write_chapter(title,content):
        with open("./Output/temp"+str(thread_ID)+".txt" , mode = 'a', encoding='utf-8') as write_text: 
            write_text.write("\n")
            write_text.write("-----------------------------------------------------------------\n")
            write_text.write(title.text + '\n')
            write_text.write("-----------------------------------------------------------------\n")
            write_text.write("\n")

            for element in content :
                write_text.write(element.text + '\n')
                write_text.write("\n")

            write_text.write("\n")
            return 0
    #獲取所有 chapter 的網址
    get_all_web()

    #計算負責的工作區塊
    partition_num = math.ceil(len(chapter_web) / browser_num)
    start_pos = partition_num * thread_ID
    if thread_ID == (browser_num-1) : end_pos = chapter_num
    else : end_pos = start_pos+partition_num       #多一格

    #開始執行
    for i in range(start_pos,end_pos,1):
        driver.get(chapter_web[i])

        chapter_title = WebDriverWait(driver, 2).until(EC.visibility_of_any_elements_located((By.XPATH, "//div[@class='novelread']//h2")))     # first item
        chpater_content = driver.find_elements(By.XPATH, "//div[@class='novelcontent']//p")

        write_chapter(chapter_title[0],chpater_content)

        import re
        pattern = r'第[一二三四五六七八九十零]+章'
        matches = re.findall(pattern, chapter_title[0].text)
        print(f"ID : {thread_ID} || Start/End/Cur = {start_pos}/{end_pos}/{i}     \t|| Totle/Cur = {partition_num}/{i-start_pos+1} || Title = {matches[0]} ")

    return 0