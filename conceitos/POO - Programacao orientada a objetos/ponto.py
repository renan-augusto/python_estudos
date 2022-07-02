class Point:
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