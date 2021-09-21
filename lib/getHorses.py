from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
import os

#import time
from time import sleep
  
def findAndClick(dri,by, paramBy, error, final_bet = False, user = '', bet = '', timer = 0):
  try: 
    sleep(1)
    element = dri.find_element(by, paramBy)
    element.click()
  except:
    print(error)


def findAndInputData(dri,by, paramBy, data, error, refresh = False):
  try:
    sleep(1)
    element = dri.find_element(by, paramBy)
    element.send_keys(data)
  except:
    print(error)
def get():
  # create webdriver object
  driver = webdriver.Chrome()
    
  # get the website
  driver.get("https://tipstrr.com/tipster/usvaluetippertelegram/tips")
    
  # sleep for some time
  sleep(3)
    
  findAndClick(driver,By.XPATH, '//*[@id="page-header"]/div/site-header/header/div/p/a[1]', 'Error >> Click no botão login')

  # set username
  findAndInputData(driver, By.XPATH, '//*[@id="login-form-login-username"]', 'joaosarti@gmail.com', 'Error >> Digitando username')    
  # set password
  findAndInputData(driver, By.XPATH, '//*[@id="login-form-login-password"]', '975314', 'Error >> Digitando password')
  # get element through text

  findAndClick(driver,By.XPATH, '//*[@id="login-form-login-submit"]', 'Error >> Click no botão login')
  sleep(2.5)
  driver.refresh()
  sleep(2.5)
  # open the file in the write mode
  file = open(os.path.abspath("")+"/cavalos.csv", "w", encoding='UTF8')
  writer = csv.writer(file)
  for element in driver.find_elements(By.XPATH, '//tip-card[@followbuttonclickid="click:follow_button_tips_active"]'):
    stake = element.find_element(By.XPATH, './/span[contains(@class,"block lg:inline lg:mr-6 lg:w-auto w-p50")][3]').text
    stake = stake.replace("Stake:", "")
    stake = stake.strip()
    print(stake)
    valor = 0.5
    if int(stake) == 1:
      valor = 0.5
    elif int(stake) == 2:
      valor = 0.6
    else:
      valor = 0.7

    corrida = element.find_element(By.XPATH, './/span[contains(@class,"block w-full truncate text-lg")]').text
    corrida = corrida[6:]
    print(corrida)

    cavalo = element.find_element(By.XPATH, './/span[contains(@class,"mb-4 block w-full text-2xl 2xl:text-4xl mt-4")]["1"]').text
    cavalo = cavalo.replace("Winner", "")
    cavalo = cavalo.replace("Each way", "")
    cavalo = cavalo[1:]
    print(cavalo)
    if(cavalo.strip()):
      writer.writerow([cavalo+" "+corrida, valor])

    print('____________________________________')

  file.close()
  # sleep for some time
  sleep(2)
  driver.quit()

get()