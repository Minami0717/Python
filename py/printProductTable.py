import sqlite3

con,cur=None,None
data1,data2,data3,data4="","","",""
row=None

con = sqlite3.connect("C:/sqlite-tools-win32-x86-3390300/sqlite-tools-win32-x86-3390300/naverDB")
cur = con.cursor()

cur.execute("select*from productTable")

print("제품코드   제품명    가격    재고수량")
print("-------------------------------------")

while(True):
    row=cur.fetchone()
    if row == None:
        break;
    data1=row[0]
    data2=row[1]
    data3=row[2]
    data4=row[3]
    print("%-10s %-6s %-7s %d"%(data1,data2,data3,data4))

con.close()
