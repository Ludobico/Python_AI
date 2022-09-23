from bs4 import BeautifulSoup

fp = open('song.xml','rt')
soup = BeautifulSoup(fp, 'html.parser')
print(soup.prettify())
print('------------------------------------------------------------')
for song in soup.find_all('song'): # 리스트형태로 반환
    print(song['album'])
    print(song.title.string)
    print(song.length.string)
    print()
