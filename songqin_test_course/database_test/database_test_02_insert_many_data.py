import MySQLdb
# Connect() 方法用于创建数据库的连接，里面可以指定参数：用户名，密码，主机等信息
conn = MySQLdb.Connect(
    host='127.0.0.1',
    user='root',
    passwd='Flying123',
    db='flying_01',
    charset='utf8'
)
# 操作数据库需要创建游标
cur = conn.cursor()
#插入1条数据
sql1="insert into student values(%d,%s,$s,%s)"
cur.excute(sql1,[
    (2,'name1','3 year 2 class','9'),
    (2,'name2','3 year 2 class','9'),
    (2,'name3','3 year 2 class','9'),
])

rows=cur.fetchall()
print(rows)

cur.close()
# 向数据库插入一条数据时必须要有这个方法
conn.commit()
conn.close()
