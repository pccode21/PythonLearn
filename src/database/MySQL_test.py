import pymysql
db=pymysql.connect(host='localhost',user='root',password='Lxd05230708',port=3306,db='test')
cursor=db.cursor()
cursor.execute("select * from user")
row1=cursor.fetchone()
print(row1)
db.commit()
cursor.close()
db.close()