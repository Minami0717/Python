import sqlite3

con,cur=None,None
data1,data2,data3,data4="","","",""
sql=""

con = sqlite3.connect("C:/sqlite-tools-win32-x86-3390300/sqlite-tools-win32-x86-3390300/naverDB")
cur = con.cursor()

while(True):
    data1=input("사용자ID ==> ")
    if data1 == "":
        break;
    data2=input("사용자이름 ==> ")
    data3=input("이메일 ==> ")
    data4=input("출생연도 ==> ")
    sql="insert into userTable values('"+data1+"','"+data2+"','"+data3+"',"+data4+")"
    cur.execute(sql)

con.commit()
con.close()
