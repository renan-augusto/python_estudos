import random 

class MinhaLista(list):
  'uma subclasse de lists que implementa o método escolha'
  
  def escolha(self):
    'retorna item da lista escolhida uniformemente de modo aleatório'
    return random.escolha(self)
  