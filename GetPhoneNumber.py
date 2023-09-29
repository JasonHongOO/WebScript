from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


# old methon
    # driver.switch_to.new_window('tab')
    # driver.get('https://tempsmss.com/receive-sms/')

def GetPhoneNumber(driver,profile_name,profile_para,thread_ID):
    PhoneList = []

    WebID = 0
    if(WebID == 0) : driver.execute_script("window.open('https://tempsmss.com/receive-sms/', '_blank')")
    elif(WebID == 1) : driver.execute_script("window.open('https://temp-number.com/countries/Netherlands', '_blank')")

    
    time.sleep(15)
    driver.switch_to.window(driver.window_handles[1])
    
    if(WebID == 0) : Target = WebDriverWait(driver, 10).until(EC.visibility_of_any_elements_located((By.XPATH, "//h2[@class = 'wp-block-post-title has-large-font-size']")))
    elif(WebID == 1) : Target = WebDriverWait(driver, 10).until(EC.visibility_of_any_elements_located((By.XPATH, "//div[@class = 'box']//h4[@class = 'card-title']")))


    for ID, ele in enumerate(Target):
        if(WebID == 1) : 
            if(ID == 0) : continue
        PhoneList.append(ele.text)

    driver.close()
    driver.switch_to.window(driver.window_handles[0])

    # PhoneList = ['+33644628720', '+3584573988754', '+46726412582', '+4520381045', '+447893932873', '+3197010518402', '+33644629080', '+46726412584', '+3584573988759', '+67074112938', '+33644628718', '+3197010518401', '+3584573988796', '+46726412561', '+33644628723', '+3584573988752', '+33644628733', '+4520389339', '+46726412570', '+67074113003', '+3197010521040', '+4520381075', '+46726412573', '+32468799054', '+3197010526115', '+33644628717', '+3197010518403', '+3584573988745']

    return PhoneList