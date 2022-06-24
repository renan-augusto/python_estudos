def news(url, topics):
    response = urlopen(url)
    html = response.read()
    content = html.decode().lower()
    for topic in topics:
        n = content.count(topic)
        print('{} aparece {} vezes.'.format(topic, n))

print(news("http://www.uol.com.br", ["economia", "corinthians"]))