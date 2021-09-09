import time
import undetected_chromedriver.v2 as uc
from selenium.webdriver.common.by import By

driver = uc.Chrome()
with driver:
  driver.get('https://www.bet365.com') 
  time.sleep(3) # sleep for 1 second
  driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[1]/div/div[2]/div[4]/div[3]/div').click()
  
  time.sleep(1) # sleep for 1 second
  username = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div/div[2]/input')
  username.send_keys("gabiAmerican")

  password = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div/div[3]/input')
  password.send_keys("135794")

  submit_login = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div/div[4]/div')
  submit_login.click()

  time.sleep(3) # sleep for 3 second
  try:
    button_identidade = driver.find_element(By.ID, 'remindLater')
    button_identidade.click()
  except:
    print('Não possui modal de verificação de identidade')
  
  time.sleep(3) # sleep for 3 second
  try:
    button_novas_mensagens = driver.find_element(By.XPATH, '/html/body/div[6]/div[4]')
    button_novas_mensagens.click()
  except:
    print('Não possui modal de verificação de novas_mensagens')

  time.sleep(2) # sleep for 2 second