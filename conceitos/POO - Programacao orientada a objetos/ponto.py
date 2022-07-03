class Ponto:
  def __init__(self, coordx = 0, coordy = 0):
    self.x = coordx
    self.y = coordy
  def setx(self, coordx):
    self.x = coordx
  def sety(self, coordy):
    self.y = coordy
  def get(self):
    return (self.x, self.y)
  def getx(self):
    return (self.x)
  def gety(self):
    return (self.y)
  def move(self, dx, dy):
    self.x += dx
    self.y += dy
  def __eq__(self, outro):
    'self == outro quando eles têm as mesmas coordenadas'
    return self.x == outro.x and self.y == outro.y
  def __repr__(self):
    'retorna representacao de string canonica ponto(x,y)'
    return ('Ponto ({},{})'.format(self.x, self.y))
  
  class Vetor(Ponto):
    def __mul__(self, v):
      return self.x*v.x + self.y*v.y
    def __add__(self, v):
      return (self.x + v.x, self.y + v.y)
    def __repr__(self):
      return "Vetor {}".format(self.get())