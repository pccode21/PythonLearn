import pymysql
def creatTable(cursor):
    cursor.execute('DROP DATABASE IF EXISTS reptile_db')
    cursor.execute('CREATE DATABASE reptile_db')
    cursor.execute('USE reptile_db')
    sql='''CREATE TABLE IF NOT EXISTS `area`(
        `id` INT NOT NULL AUTO_INCREMENT,
        `code` INT NOT NULL,
        `name` VARCHAR(10) NOT NULL,
        PRIMARY KEY (`id`)
        )ENGINE=InnoDB DEFAULT CHARSET=UTF8MB4;
        '''
    cursor.execute('DROP TABLE IF EXISTS area')
    cursor.execute(sql)
    print('成功创建数据库和表！')
def insertData(conn,cursor):
    sql='''INSERT INTO area(id,code,name) VALUES
        (1,111111,'中国');'''
    try:
        cursor.execute(sql)
        conn.commit()
        print('成功插入数据！')
    except:
        conn.rollback()
if __name__=='__main__':
    conn=pymysql.connect(host='localhost',user='root',password='Lxd05230708',port=3306)
    cursor=conn.cursor()
    creatTable(cursor)
    insertData(conn,cursor)
    cursor.close()
    conn.close()


