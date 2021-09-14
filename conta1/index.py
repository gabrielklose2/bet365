import sys
import os
sys.path.append(os.path.abspath('./lib'))
from bot import *

class Conta1:
  username = ""
  password = ""
  pesquisa = ""
  valor = ""

  def setUsername(self, username):
    self.username = username
  
  def getUsername(self):
    return self.username
  
  def setPassword(self, password):
    self.password = password
  
  def getPassword(self):
    return self.password
  
  def setPesquisa(self, pesquisa):
    self.pesquisa = pesquisa
  
  def getPesquisa(self):
    return self.pesquisa
  
  def setValor(self, valor):
    self.valor = valor
  
  def getValor(self):
    return self.valor

  def setAuthentication(self):
    f=open(os.path.abspath('./conta1')+"/account.txt","r")
    lines=f.readlines()
    # username=lines[0]
    # password=lines[1]
    self.setUsername(lines[0].strip())
    self.setPassword(lines[1].strip())
    f.close()
  
  def setBet(self):
    f=open(os.path.abspath("")+"/aposta.txt","r")
    lines=f.readlines()
    # pesquisa=lines[0]
    # valor=lines[1]
    self.setPesquisa(lines[0].strip())
    self.setValor(lines[1].strip())
    f.close()

Bet = Conta1()
Bet.setAuthentication()
Bet.setBet()
toBet(Bet)