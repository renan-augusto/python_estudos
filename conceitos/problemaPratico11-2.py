from html.parser import HTMLParser
class MyHTMLParser(HTMLParser):
  def handle_starttag(self, tag, attrs):
    if tag not in {'meta', 'p','br'}:
      print(tag, "Start")    
  def handle_endtag(self, tag):
    if tag not in {'meta', 'p', 'br'}:
      print(tag, "End")
    
    
    
    
#this lines bellow are here to test my code, not as a part of the class  
infile = open('C:\workspace\python\conceitos\linksParser.html')
content = infile.read()
infile.close()
myparser = MyHTMLParser()
myparser.feed(content)

    