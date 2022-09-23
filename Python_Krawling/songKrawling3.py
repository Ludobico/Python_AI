from bs4 import BeautifulSoup

fp = open('song.xml','r', encoding='utf-8')
openFile = fp.read()
soup = BeautifulSoup(openFile, 'html.parser')

for song in soup.findAll('song'): # 리스트형태로 반환
    print(song['album'])
    print(song.title.string)
    print(song.length.string)
    print()