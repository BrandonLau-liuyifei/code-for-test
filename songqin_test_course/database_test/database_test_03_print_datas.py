#获取数据记录fetchone，fetchmany，fetchall
import MySQLdb
conn = MySQLdb.Connect(
    host='127.0.0.1',
    user='root',
    passwd='Flying123',
    db='flying_01',
    charset='utf8'
)
cur=conn.cursor()
#只能打印出数据条数
cur.execute("select * from student")
# 打印一条数据
cur.fetchone()
#打印5条数据
cur.fetchmany(5)
#打印所有数据
cur.fetchall()
#将游标定位到表中的第一条数据
cur.scrolll(0,'absolute')

#逐条打印指定条数
lines=cur.execute("select * from student")
info0=cur.fetchmany(lines)
for i in info0:
    print(i)

#逐条打印指定条数
info1=cur.fetchall()
for ii in info1:
    print(ii)
cur.close()
conn.commit()
conn.close()
