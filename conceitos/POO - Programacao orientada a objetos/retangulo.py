class Retangulo:
  def setSize(self, coordx, coordy):
    self.x = coordx
    self.y = coordy
  def calculaPerimetro(self):
    return 2*(self.x + self.y)
  def calculaArea(self):
    return (self.x * self.y)