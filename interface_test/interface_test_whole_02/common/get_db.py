"""
conf 配置文件
common 封装方法
"""

import pymysql

from interface_test.interface_test_whole_02.config.conf import sql_conf


def get_sql(sql):
    """
    :param sql: 运行查询的sql语句
    :return: 数据库查询结果
    """
    #创建1个mysql链接
    # host = '127.0.0.1'
    # port = 3306
    # user = 'root'
    # password = 'Flying123'
    # database = 'flying_01'
    # charset = 'utf8'
    host,user,password,port,charset,database=sql_conf()
    db = pymysql.connect(host=host,user=user,password=password,database=database,charset=charset,port=port)
    # 创建创建1个游标
    cursor = db.cursor()
    # 运行sql语句
    cursor.execute(sql)
    #把sql运行的结果数据保存在data里面
    data = cursor.fetchall() #获取查处的所有值
    cursor.close() #游标关闭
    db.close() #数据库关闭
    return data

print(get_sql("SELECT count(goods.goods_id) FROM goods"))

