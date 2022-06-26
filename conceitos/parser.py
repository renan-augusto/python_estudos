from html.parser import HTMLParser
class LinkParser(HTMLParser):
  '''Analisador de doc .HTML que mostra valores dos atributos href nas tags de início de âncora'''
  def handle_starttag(self,tag,attrs):
    '''mostra o valor do atributo href, se houver'''
    if tag == 'a':
      for attr in attrs:
        if attr[0] == "href":
          print(attr[1])

infile = open('C:\workspace\python\conceitos\linksParser.html')
content = infile.read()
infile.close()
linkparser = LinkParser()
linkparser.feed(content)

