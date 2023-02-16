import sqlite3

con,cur=None,None
data1,data2,data3,data4="","","",""
sql=""

con = sqlite3.connect("C:/sqlite-tools-win32-x86-3390300/sqlite-tools-win32-x86-3390300/naverDB")
cur = con.cursor()

while(True):
    data1=input("제품코드 ==> ")
    if data1 == "":
        break;
    data2=input("제품명 ==> ")
    data3=input("가격 ==> ")
    data4=input("재고수량 ==> ")
    sql="insert into productTable values('"+data1+"','"+data2+"','"+data3+"',"+data4+")"
    cur.execute(sql)

con.commit()
con.close()
