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
    print('findAndInputData > '+data)
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
    driver.switch_to.default_content()
    print("closeModalIdenty >>> error")

def closeModalEmail(driver, by):
  try: 
    time.sleep(10) # sleep for 10 second
    driver.switch_to.frame(driver.find_element(by, "/html/body/div[4]/iframe"))
    driver.find_element(by, '//*[@id="RemindMeLater"]').click()

    driver.switch_to.default_content()
  except:
    driver.switch_to.default_content()
    print("closeModalEmail >>> error")

def toBet(bet):
  driver = uc.Chrome()
  with driver:

    driver.get('https://www.bet365.com') 
    time.sleep(3) # sleep for 3 second
    findAndclick(driver,By.XPATH, '/html/body/div[1]/div/div[3]/div[1]/div/div[2]/div[4]/div[3]/div', 'Click no botão login')

    # set username
    findAndInputData(driver, By.XPATH, '//*[contains(@class, "lms-StandardLogin_Username")]', bet.username, 'Digitando username')    
    # set password
    findAndInputData(driver, By.XPATH, '//*[contains(@class, "lms-StandardLogin_Password")]', bet.password, 'Digitando password')

    findAndclick(driver, By.XPATH, '//div[contains(@class, "lms-StandardLogin_LoginButton")]', 'Click no submit do login')

    #fechando modal/iframe email secundario
    closeModalEmail(driver, By.XPATH)
    
    #fechando modal/iframe de confirmacao de identidade
    closeModalIdenty(driver, By.XPATH)
    
    #fechando modal de aviso de novas mensagens
    findAndclick(driver, By.XPATH, '/html/body/div[6]/div[4]', 'Click no fechar da modal de mensagens novas')

    #clicando na lupa para digitar a aposta
    findAndclick(driver, By.XPATH, '//div[contains(@class, "hm-SiteSearchIconLoggedIn_Icon")]', 'Click na lupa para digitar a aposta')
    
    #input de busca da aposta
    findAndInputData(driver, By.XPATH, '//div[contains(@class, "sml-SearchTextInput")] ', bet.pesquisa, 'inserindo termo de busca da aposta')
    
    #clicando na aposta
    findAndclick(driver, By.XPATH, '//div[contains(@class, "ssm-SiteSearchBetOnlyParticipant_Name")]', 'Click na aposta')
    
    
    #clicando no valor da aposta
    findAndclick(driver, By.XPATH, '//div[contains(@class, "qbs-EachWayStakeBox qbs-StakeBox qbs-StakeBox_MouseMode qbs-StakeBox_Empty qbs-StakeBox_Width410")]', 'Click no valor da aposta')
    
    #inserindo o valor da aposta
    findAndInputData(driver, By.XPATH, '//div[contains(@class, "qbs-StakeBox_StakeValue-hidden")]', bet.valor, 'inserindo valor da aposta')
    findAndInputData(driver, By.XPATH, '//div[contains(@class, "qbs-StakeBox_StakeValue-input")]', bet.valor, 'inserindo valor da aposta')
    
    #clicando em fazer aposta
    findAndclick(driver, By.XPATH, '//div[contains(@class, "qbs-BetPlacement")]', 'Fazendo aposta')
    time.sleep(2) # sleep for 2 second

    driver.quit()

def teste():
  print('aaaaaa')