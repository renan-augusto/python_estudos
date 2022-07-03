from random import shuffle
from types import NoneType

class Baralho:
  #representa um baralho de 52 cartas
  
  #valores e naipes são variáveis da classe Baralho
  valores = {'2','3','4','5','6','7','8','9','10','J','Q','K','A'}
  
  #naipes são 4 símbolos Unicode representando os 4 naipes
  naipes = {'\u2660', '\u2661', '\u2662', '\u2663'}
  
  def __init__(self, listaCartas = None):
    if listaCartas != None:
      self.baralho = listaCartas      
    #'inicializa o baralho de 52 cartas'
    self.baralho = [] #baralho vazio inicialmente
    
    for naipe in Baralho.naipes:
      for valor in Baralho.valores:
        self.baralho.append(listaCartas(valor,naipe)) #ainda não entendi esse Card....
  
  def distribuiCarta(self):
    return self.baralho.pop()
  
  def suffle(self):
    shuffle(self.baralho)
    
  def __repr__(self):
    return "Carta ({}, {})".format(self.valor, self.naipe)
  
  def __eq__(self, outro):
    return self.valor == outro.valor and self.naipe == outro.naipe
  