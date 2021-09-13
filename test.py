import time
import undetected_chromedriver.v2 as uc
from selenium.webdriver.common.by import By

def findAndclick(dri,by, paramBy, error):
  try: 
    time.sleep(2) # sleep for 2 second
    element = dri.find_element(by, paramBy)
    element.click()
  except:
    print(error)

def findAndInputData(dri,by, paramBy, data, error):
  try: 
    time.sleep(2) # sleep for 2 second
    element = dri.find_element(by, paramBy)
    element.send_keys(data)
  except:
    print(error)

def closeModalIdenty(driver, by):
  try: 
    time.sleep(10) # sleep for 10 second
    driver.switch_to.frame(driver.find_element(by, "/html/body/div[4]/iframe"))
    driver.find_element(by, '//*[@id="remindLater"]').click()

    driver.switch_to.default_content()
  except:
    print("closeModalIdenty >>> error")

def logaBet(driver):
  with driver:
    driver.get('https://www.bet365.com') 
    time.sleep(3) # sleep for 3 second
    findAndclick(driver,By.XPATH, '/html/body/div[1]/div/div[3]/div[1]/div/div[2]/div[4]/div[3]/div', 'Click no botão login')

    # set username
    findAndInputData(driver, By.XPATH, '/html/body/div[1]/div/div[3]/div/div[2]/input', 'gabiAmerican', 'Digitando username')
    
    # set password
    findAndInputData(driver, By.XPATH, '/html/body/div[1]/div/div[3]/div/div[3]/input', '135794', 'Digitando password')


    findAndclick(driver, By.XPATH, '/html/body/div[1]/div/div[3]/div/div[4]/div', 'Click no submit do login')
    time.sleep(5) # sleep for 2 second


driver = uc.Chrome()
driver2 = uc.Chrome()
driver3 = uc.Chrome()
driver4 = uc.Chrome()
logaBet(driver)
# logaBet(driver2)
# logaBet(driver3)
# logaBet(driver4)