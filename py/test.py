import bs4
import urllib.request

Url = "https://sports.news.naver.com/kbaseball/index"
htmlObject = urllib.request.urlopen(Url)
webPage = htmlObject.read()
bsObject = bs4.BeautifulSoup(webPage,'html.parser')

tag = bsObject.find('ul',{'class':'main_menu_list'})

print('## 네이버 스포츠의 메뉴 목록 ##')
li_list = tag.find('li',{'class':'main_menu_item'})
menuname = li_list.find('a').text
print(menuname)
