from http import client
from urllib.request import urlopen
response = urlopen('http://www.w3c.org/Consortium/facts.html')
type(response)
<class 'http.client.HTTPResponse'>