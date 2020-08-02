#POM  page object module

"""
配置文件，配置信息如url中的ip，端口等配置进行封装。
测试数据修改比较多，把数据抽离出来
common公共方法，数据参数化，表格跟数据库的操作，包括后期做的一些密码处理、校验
测试用例test_case 每个接口请求的接口
运行测试用例的模块
report报告模块，生成对应的html、xml、allure模块
log模块 ，生成日志方便后期定位解决
ci/cd持续继承
"""
"""
模块化思想，结构：
common   //python package
test_case //python package
testdata //python package
run_case //dir
report //dir
log //dir
"""

"""
场景：
1.独立完成
按照模块化思想完成
2.合作完成，你是主导
前期：
需求、人员、计划安排>>搭建初步的框架，告知测试人员>>公共方法先自己写好,其他人写的方法要先说明>>测试用例根据人员按照模块划分
3.辅助完成
了解代码结构>>根据分配的任务编写>>好的改进意见可以提出
"""

"""
参数化

"""
