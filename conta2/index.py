import sys
import os
import csv
import unicodedata
import re
sys.path.append(os.path.abspath('./lib'))
from bot import *

class Conta1:
  username = ""
  password = ""
  cavalo = ""
  valor = ""

  def setUsername(self, username):
    self.username = username
  
  def getUsername(self):
    return self.username
  
  def setPassword(self, password):
    self.password = password
  
  def getPassword(self):
    return self.password
  
  def setCavalo(self, cavalo):
    self.cavalo = cavalo
  
  def getCavalo(self):
    return self.cavalo
  
  def setValor(self, valor):
    self.valor = valor
  
  def getValor(self):
    return self.valor

  def setAuthentication(self):
    f=open(os.path.abspath('./conta2')+"/account.txt","r")
    lines=f.readlines()
    # username=lines[0]
    # password=lines[1]
    self.setUsername(lines[0].strip())
    self.setPassword(lines[1].strip())
    f.close()

  def removeCaracterEspecial(self, palavra):

    # Unicode normalize transforma um caracter em seu equivalente em latin.
    nfkd = unicodedata.normalize('NFKD', palavra)
    palavraSemAcento = u"".join([c for c in nfkd if not unicodedata.combining(c)])

    # Usa expressão regular para retornar a palavra apenas com números, letras e espaço
    return re.sub('[^a-zA-Z0-9 \\\]', '', palavraSemAcento)

file = open(os.path.abspath("")+"/cavalos.csv")
csvreader = csv.reader(file)
for row in csvreader:
  Bet = Conta1()
  array = row[0].split(';',1)
  cavalo = Bet.removeCaracterEspecial(array[0])
  valor_aposta = Bet.removeCaracterEspecial(array[1])
  Bet.setAuthentication()
  Bet.setCavalo(cavalo.strip())
  Bet.setValor(valor_aposta.strip())
  toBet(Bet)
file.close()

# Bet = Conta1()
# Bet.setAuthentication()
# Bet.setBet()
# toBet(Bet)