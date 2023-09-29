from selenium import webdriver

def get_chrome_driver_version():
    # 初始化一個Chrome Driver實例
    driver = webdriver.Chrome()
    
    # 取得Chrome Driver的版本號
    version = driver.capabilities['browserVersion']
    
    # 關閉Chrome Driver
    driver.quit()
    
    return version

if __name__ == "__main__":
    chrome_version = get_chrome_driver_version()
    print(f"Chrome Driver 版本號: {chrome_version}")


