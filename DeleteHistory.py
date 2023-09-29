from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def DeleteHistory(driver,profile_name,profile_para,thread_ID):
    driver.switch_to.new_window('tab')

    driver.get('chrome://settings/clearBrowserData')
    result = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, "//settings-ui")))
    result.send_keys(Keys.TAB)
    time.sleep(1)
    result.send_keys(Keys.ENTER)
    time.sleep(1)

    driver.close()
    driver.switch_to.window(driver.window_handles[0])

    return 0