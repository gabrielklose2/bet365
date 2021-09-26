import time
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def registerLog(message, user, bet):
  try:
    file = open(os.path.abspath("")+"/log.txt", "a")
    file.write(message+": "+ user + " - " + bet + "\n")
    file.close()
  except:
    print('registerLog >>> Error')
def elementExist(driver, by, paramBy, timer = 1):
  try:
    element_present = EC.presence_of_element_located((by, paramBy))
    WebDriverWait(driver, timer).until(element_present)
    return True
  except:
    return False

def handleElement(dri,by, paramBy, tentativas = 3):
  exists = elementExist(dri,by, paramBy)
  print("paramBy < " + str(paramBy))
  print("fora do while < " + str(exists))
  count = 0
  while (not exists and count < tentativas):
    count += 1
    exists = elementExist(dri,by, paramBy)
    print("dentro do while > " + str(exists))
  
  return exists

def runBet(dri,by, bet):
  try:
    exists = elementExist(dri,by, '//div[contains(string(), "Aposta Feita")]')
    count = 0
    while (not exists and count < 4):
      count += 1
      findAndClick(dri, by, '//div[contains(@class, "qbs-BetPlacement")]', 'Error >> Fazendo aposta', True, bet.username, bet.cavalo)
      exists = elementExist(dri,by, '//div[contains(string(), "Aposta Feita")]')
    return True
  except:
    return False

def findAndClick(dri,by, paramBy, error, final_bet = False, user = '', bet = '', timer = 0):
  try: 
    time.sleep(timer) # sleep for 3 second
    if(not handleElement(dri,by, paramBy)):
      raise Exception("Error!")
    element = dri.find_element(by, paramBy)
    element.click()
    if(final_bet):
      file = open(os.path.abspath("")+"/log.txt", "a")
      file.write("Success : "+ user + " - " + bet + "\n")
      file.close()
    return True
  except:
    if(final_bet):
      file = open(os.path.abspath("")+"/log.txt", "a")
      file.write("Error : "+ user + " - " + bet + "\n")
      file.close()
    print(error)
    return False


def findAndInputData(dri,by, paramBy, data, error, refresh = False):
  try: 
    if(not handleElement(dri,by, paramBy)):
      raise Exception("Error!")

    element = dri.find_element(by, paramBy)
    element.send_keys(data)
    if(refresh):
      time.sleep(1.5)
      # dri.refresh()
    return True
  except:
    print(error)
    return False

def findAndClearData(dri,by, paramBy, error):
  try: 
    if(not handleElement(dri,by, paramBy)):
      raise Exception("Error!")
    element = dri.find_element(by, paramBy)
    element.clear()
    return True
  except:
    print(error)
    return False

def closeModalIdenty(driver, by):
  try: 
    if(not handleElement(driver,by, "/html/body/div[4]/iframe")):
      raise Exception("Error!")
    driver.switch_to.frame(driver.find_element(by, "/html/body/div[4]/iframe"))
    
    if(not handleElement(driver,by, '//*[@id="remindLater"]')):
      raise Exception("Error!")
    driver.find_element(by, '//*[@id="remindLater"]').click()

    driver.switch_to.default_content()
  except:
    driver.switch_to.default_content()
    print("closeModalIdenty >>> error")

def closeModalEmail(driver, by):
  try: 
    if(not handleElement(driver,by, "/html/body/div[4]/iframe", 1)):
      raise Exception("Error!")
    driver.switch_to.frame(driver.find_element(by, "/html/body/div[4]/iframe"))
    
    if(not handleElement(driver,by, '//*[@id="RemindMeLater"]'), 2):
      raise Exception("Error!")
    driver.find_element(by, '//*[@id="RemindMeLater"]').click()

    driver.switch_to.default_content()
  except:
    driver.switch_to.default_content()
    print("closeModalEmail >>> error")

def runLogin(dri,bet):
  try:
    time.sleep(1)
    exists = True
    count = 0
    while (exists and count < 4):
      count += 1
      time.sleep(3)
      findAndClick(dri,By.XPATH, '/html/body/div[1]/div/div[3]/div[1]/div/div[2]/div[4]/div[3]/div', 'Error >> Click no botão login')
      # set username
      findAndInputData(dri, By.XPATH, '//*[contains(@class, "lms-StandardLogin_Username")]', bet.username, 'Error >> Digitando username')    
      # set password
      findAndInputData(dri, By.XPATH, '//*[contains(@class, "lms-StandardLogin_Password")]', bet.password, 'Error >> Digitando password')

      findAndClick(dri, By.XPATH, '//div[contains(@class, "lms-StandardLogin_LoginButton")]', 'Error >> Click no submit do login')
      time.sleep(3)
      exists = elementExist(dri,By.XPATH, '//*[contains(@class, "lmd-LoginModuleDefault_FailedLogin")]')
      if(exists):
        dri.refresh()
    return exists
  except:
    return False

def clickAposta(dri, bet):
  try:
    exists = False
    count = 0
    while (not exists and count < 3):
      count += 1
      findAndClick(dri, By.XPATH, '//div[contains(@class, "ssm-SiteSearchBetOnlyParticipant_Name")]', 'Error >> Click na aposta')
      exists = elementExist(dri,By.XPATH, '//*[contains(@class, "qbs-EwexBetItem qbs-NormalBetItem")]')
      if(not exists):
        dri.refresh()
      time.sleep(1)
    return exists
  except:
    return False

def toBetFirst(bet, driver):
  try:

    driver.get('https://www.bet365.com/#/HO/') 
    time.sleep(2) # sleep for 3 second
    runLogin(driver, bet)
    time.sleep(3) # sleep for 3 second
    #fechando modal/iframe email secundario
    closeModalEmail(driver, By.XPATH)
    
    #fechando modal/iframe de confirmacao de identidade
    closeModalIdenty(driver, By.XPATH)
    
    #fechando modal de aviso de novas mensagens
    findAndClick(driver, By.XPATH, '/html/body/div[6]/div[4]', 'Error >> Click no fechar da modal de mensagens novas')

    #clicando na lupa para digitar a aposta
    findAndClick(driver, By.XPATH, '//div[contains(@class, "hm-SiteSearchIconLoggedIn_Icon")]', 'Error >> Click na lupa para digitar a aposta')
    
    #input de busca da aposta
    findAndInputData(driver, By.XPATH, '//*[contains(@class, "sml-SearchTextInput")] ', bet.cavalo, 'Error >> inserindo termo de busca da aposta')
    
    #clicando na aposta
    # success = findAndClick(driver, By.XPATH, '//div[contains(@class, "ssm-SiteSearchBetOnlyParticipant_Name")]', 'Error >> Click na aposta')
    # if(not success):
    #   registerLog("Error", bet.username, bet.cavalo)
    #   return False
    if(not clickAposta(driver, bet)): 
      return False
    
    #clicando no valor da aposta
    findAndClick(driver, By.XPATH, '//div[contains(@class, "qbs-EachWayStakeBox qbs-StakeBox qbs-StakeBox_MouseMode qbs-StakeBox_Empty qbs-StakeBox_Width410")]', 'Error >> Click no valor da aposta')
    
    #inserindo o valor da aposta
    findAndInputData(driver, By.XPATH, '//div[contains(@class, "qbs-StakeBox_StakeValue-input")]', bet.valor, 'Error >> inserindo valor da aposta2')
    
    #clicando em fazer aposta
    # findAndClick(driver, By.XPATH, '//div[contains(@class, "qbs-BetPlacement")]', 'Error >> Fazendo aposta', True, bet.username, bet.cavalo)
    runBet(driver,By.XPATH, bet)
    return True
  except:
    # driver.quit()
    return False

def toBetRemaining(bet, driver):
  try:
    time.sleep(2)
    #verificado se a aposta foi feita
    # if(not elementExist(driver, By.XPATH, '//div[contains(string(), "Aposta Feita")]', 2)):
    #   findAndClick(driver, By.XPATH, '//div[contains(@class, "bs-DeleteButton bs-DeleteButton_MouseMode")]', 'Error >> Fechando modal de aposta',)
    findAndClick(driver, By.XPATH, '//div[contains(@class, "qbs-QuickBetHeader_DoneButton")]', 'Error >> click em terminar aposta')
    
    #clicando na lupa para digitar a aposta
    findAndClick(driver, By.XPATH, '//div[contains(@class, "hm-SiteSearchIconLoggedIn_Icon")]', 'Error >> Click na lupa para digitar a aposta')
    
    findAndClearData(driver, By.XPATH, '//*[contains(@class, "sml-SearchTextInput")] ', 'Error >> limpando input de busca da aposta')

    #input de busca da aposta
    findAndInputData(driver, By.XPATH, '//*[contains(@class, "sml-SearchTextInput")] ', bet.cavalo, 'Error >> inserindo termo de busca da aposta', True)

    #clicando na aposta
    success = findAndClick(driver, By.XPATH, '//div[contains(@class, "ssm-SiteSearchBetOnlyParticipant_Name")]', 'Error >> Click na aposta', 1)
    if(not success):
      registerLog("Error", bet.username, bet.cavalo)
      return False

    #clicando no valor da aposta
    findAndClick(driver, By.XPATH, '//div[contains(@class, "qbs-EachWayStakeBox qbs-StakeBox qbs-StakeBox_MouseMode qbs-StakeBox_Empty qbs-StakeBox_Width410")]', 'Error >> Click no valor da aposta')

    #inserindo o valor da aposta
    findAndInputData(driver, By.XPATH, '//div[contains(@class, "qbs-StakeBox_StakeValue-input")]', bet.valor, 'Error >> inserindo valor da aposta2')
      
    #clicando em fazer aposta
    runBet(driver,By.XPATH, bet)
    #verificando se a aposta foi feita
    if(not elementExist(driver, By.XPATH, '//div[contains(string(), "Aposta Feita")]', 2)):
      findAndClick(driver, By.XPATH, '//div[contains(@class, "bs-DeleteButton bs-DeleteButton_MouseMode")]', 'Error >> Fechando modal de aposta',)
    time.sleep(2)
  except:
    # driver.quit()
    return False
