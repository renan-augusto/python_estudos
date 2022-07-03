class Animal:
  def __init__(self, especie = "animal", linguagem = "emitir sons"):
    self.esp = especie
    self.ling = linguagem
  def setEspecie(self, especie):
    self.esp = especie
  def setLinguagem(self, linguagem):
    self.ling = linguagem
  def fala(self): 
    print("Eu sou um {} e sei {}".format(self.esp.lower(), self.ling.lower()))
  

class Ave(Animal):  #importante lembrar que a classe ave nada mais é que uma subclasse da classe animal
  'representa uma ave'
  def fala(self):
    'exibe sons da ave'
    print('{}!'.format(self.linguagem)*3)
  
  
  