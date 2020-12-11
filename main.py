from reunion.trends import ReunionTrends
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

import time


if __name__ == '__main__':
    #trends = ReunionTrends()
    driver = webdriver.Chrome(ChromeDriverManager().install())

    driver.get('https://www.google.com')
    time.sleep(5)
    driver.close()
