from selenium import webdriver
import time

url = "https://leroymerlin.ru/"

driver = webdriver.Chrome(executable_path= "C:\\Users\\Dell\\PycharmProjects\\web_site_parsing\\chromedriver.exe")

try:
    driver.get(url)
    time.sleep(5)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()

