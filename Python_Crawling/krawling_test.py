from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = BeautifulSoup(html_doc, 'html.parser')
print('0.-------------------------------------')
print(soup.prettify())
print('1.-------------------------------------')
print(soup.title)
print('2.-------------------------------------')
print(soup.title.name)
print('3.-------------------------------------')
print(soup.title.string)
print('4.-------------------------------------')
print(soup.title.parent.name)
print('5.-------------------------------------')
print(soup.p)
print('6.-------------------------------------')
print(soup.p['class'])
print('7.-------------------------------------')
print(soup.a)
print('8.-------------------------------------')
print(soup.find_all('a'))
print('9.-------------------------------------')
print(soup.find(id='link3'))
print('10.-------------------------------------')
for link in soup.find_all('a'):
    print(link.get('href'))