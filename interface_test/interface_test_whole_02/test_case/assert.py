"""assert a  判断A为真
assert not a  判断A不为真
assert a in b  判断b包含a
assert a==b 判断a等于b
assert a!=b 判断a不等于b
"""
from interface_test.interface_test_whole_02.common.get_db import get_sql

"""
数据库断言
"""
assert get_sql("select id from user where user='hahahaha'")

