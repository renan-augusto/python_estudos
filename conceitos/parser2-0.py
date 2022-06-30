from urllib.parse import urljoin
from html.parser import HTMLParser

class Collector(HTMLParser):
  #coleta urls de hyperlink em uma lista
  
  def __init__(self, url):
    #inicializa analisador, o url e uma lista
    HTMLParser.__init__(self)
    self.url = url
    self.link = []
    
  def handle_starttag(self, tag, attrs):
    #coleta urls de hyperlink em sua forma absoluta
    if tag == 'a':
      for attr in attrs:
        if attr[0] == 'href':
          #constroi um URL absoluto
          absolute = urljoin(self.url,attr[1])
          if absolute [:4] == 'http': #coleta URL´s http
            self.links.append(absolute)
  
  def getlinks(self):
    #retorna URLs de hyperlink em seu formato absoluto
    return.self.links 
    
