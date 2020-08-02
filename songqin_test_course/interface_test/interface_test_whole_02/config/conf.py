# def server_ip():
#     """
#     dev_ip  开发环境的服务器ip地址
#     sit_ip  测试环境的服务器ip地址
#     :return:  不同服务器的ip地址
#     """
#     dev_ip='http://172.0.0.1'
#     sit_ip='http://172.12.126.197'
#     return dev_ip

# def sql_conf():
#     """
#     数据库配置信息
#     :return:
#     """
#     host = '127.0.0.1'
#     port = 3306
#     user = 'root'
#     password = 'Flying123'
#     database = 'flying_01'
#     charset = 'utf-8'
#     return host,user,password,port,charset,database

# 字典参数化
def server_ip():
    """
    dev_ip  开发环境的服务器ip地址
    sit_ip  测试环境的服务器ip地址
    :return:  不同服务器的ip地址
    """
    server_address={
        "dev_ip":"http://172.0.0.1",
        "sit_ip":"http://172.12.126.197"
    }
    return server_address["sit_ip"]

# 字典的参数化
def sql_conf():
    """
    数据库配置信息
    :return:
    """
    host = '127.0.0.1'
    port = 3306
    user = 'root'
    password = 'Flying123'
    database = 'flying_01'
    charset = 'utf-8'
    host, user, password, port, charset, database=['127.0.0.1','root','Flying123',3306,'utf-8','flying_01']
    return host,user,password,port,charset,database