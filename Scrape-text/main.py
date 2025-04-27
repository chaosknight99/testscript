from selenium import webdriver  # tool to instruct the behavior of the browser

import time


def get_driver():
  # set options to make browsing easier
  options = webdriver.ChromeOptions()
  options.add_argument( "disable-infobars")  #flags to disable the browser's info bar
  options.add_argument("start-maximized")  #flags to start the browser maximized
  options.add_argument("disable-dev-shm-usage")  #flags to disable the browser's shared memory usage
  options.add_argument( "no-sandbox")  #flags to disable the browser's sandbox which is a security feature
  options.add_experimental_option("excludeSwitches", ["enable-automation"])  #flags to exclude the browser's automation switch
  options.add_argument("disable-blink-features=AutomationControlled")

  driver = webdriver.Chrome(options)
  driver.get("http://automated.pythonanywhere.com")
  return driver


def clean_text(text):
  """Extract only the temperature from text"""
  output = float(text.split(": ")[1])
  return output
  
def main():
  driver = get_driver()
  time.sleep(2)
  element = driver.find_element(by="xpath",value="/html/body/div[1]/div/h1[2]")
  return clean_text(element.text)


print(main())
