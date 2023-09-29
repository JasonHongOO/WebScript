import time
import random
import string

from tkinter import messagebox

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def get_item(driver,profile_name,profile_para,thread_ID):
    def Record(Item):
        with open("./En_Name.txt", mode = 'a', encoding="utf-8") as write_text: 

            for ele in Item:
                write_text.write(ele.text + '\n')

        return 0
    
    # signle
    # Item = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, "//tbody[@class='row-hover']//td[@class='column-1']")))
    
    # mutiple
    Item = WebDriverWait(driver, 2).until(EC.visibility_of_any_elements_located((By.XPATH, "//tbody[@class='row-hover']//td[@class='column-1']")))
    Record(Item)


    
    