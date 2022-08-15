#import neccesary packages
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time

#create user define function 
def get_geo_Loc():
    options = Options()
    options.add_argument("--use-fake-ui-for-media-stream")
    timeout = 30
    #drive to chrome browser
    driver = webdriver.Chrome(executable_path = '.\chromedriver.exe', options=options)
    driver = webdriver.Chrome()
    driver.get("https://google.co.in/maps")
    wait = WebDriverWait(driver, timeout)
    time.sleep(10)
    #get the url link in the broswer
    get_url = driver.current_url
   
    result = get_url.split("@")
    #print the lat and long of the exact location
    loc = result[1].split(",")
    print("latitude = ",loc[0])
    print("longitude = ",loc[1])

    driver.quit()

#call the function
get_geo_Loc()
