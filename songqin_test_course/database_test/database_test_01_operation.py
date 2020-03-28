# 加载的第三方的库mysqlclient、mysql-python
#获取数据记录fetchone，fetchmany，fetchall
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
# 创建数据表
cur.execute("create table student(id int ,"
            "name varchar(20),"
            "class varchar(30),"
            "age varchar(10))"
            )
#插入1条数据
cur.excute("insert into student values(2,'tom','3 year 2 class','9')")
cur.excute("insert into student values(2,'brandon','3 year 2 class','8')")
#修改查询的条件
cur.excute("update student set class='3 year 1 class' where name='tom'")
#删除查询条件的数据
cur.excute("delete from student where age='9'")

rows=cur.fetchall()
print(rows)

cur.close()
# 向数据库插入一条数据时必须要有这个方法
conn.commit()
conn.close()




