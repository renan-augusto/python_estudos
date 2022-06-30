from html.parser import HTMLParser
from operator import rshift
from urllib.request import urlopen
class LinkParser(HTMLParser):
  '''Analisador de doc .HTML que mostra valores dos atributos href nas tags de início de âncora'''
  def handle_starttag(self,tag,attrs):
    '''mostra o valor do atributo href, se houver'''
    if tag == 'a':
      for attr in attrs:
        if attr[0] == "href":
          print(attr[1])

#infile = open('C:\workspace\python\conceitos\linksParser.html')
#content = infile.read()
#infile.close()
rsrce = urlopen('http://www.w3.org/Consortium/mission.html')
content = rsrce.read().decode()
linkparser = LinkParser()
linkparser.feed(content)

