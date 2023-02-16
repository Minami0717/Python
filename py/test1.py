import bs4
import urllib.request

def getBookInfo(book_tag):
    names = book_tag.find('div',{'class':'goods_name'})
    bookName = names.find('a').text
    auths = book_tag.find('span',{'class':'goods_auth'})
    bookAuth = auths.find('a').text
    bookPub = book_tag.find('span',{'class':'goods_pub'}).text
    bookDate = book_tag.find('span',{'class':'goods_date'}).text
    bookPrice = book_tag.find('em',{'class':'yes_b'}).text
    return [bookName,bookAuth,bookPub,bookDate,bookPrice]

url = 'http://www.yes24.com/24/Category/Display/002001010036?ParamSortTp=05&PageNumber='
pageNumber = 1
totalPrice = 0

while True:
    try:
        bookUrl = url + str(pageNumber)
        pageNumber += 1
        
        htmlObject = urllib.request.urlopen(bookUrl)
        webPage = htmlObject.read()
        bsObject = bs4.BeautifulSoup(webPage,'html.parser')
        tag = bsObject.find('ul',{'class':'clearfix'})
        all_books = tag.findAll('div',{'class':'goods_info'})

        for book in all_books:
            ret_list = getBookInfo(book)
            price = ret_list[-1].replace(',','')
            totalPrice += int(price)
            print(ret_list)
            
    except:
        break

print('** 총 가격 ==>',totalPrice,'원')
