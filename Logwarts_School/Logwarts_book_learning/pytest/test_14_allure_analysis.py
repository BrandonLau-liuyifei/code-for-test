import pytest
"""
    allure安装
win版
    下载allure生成工具，解压，配置其bin文件路径至环境变量中
mac版或linux版
    下载allure生成工具，解压，配置其bin文件路径至环境变量中：
    open -t ~/bash_profile
    变量文件中输入以下：
    #allure
    export PATH="/Users/mac/liuyifei_personal_file/allure-2.7.0/bin:${PATH}"
    执行变量文件生效
    source ~/.bash_profile
    查看allure版本：
    allure --version
mac版也可可使用以下安装方式：
    先安装brew，参见教程 https://www.cnblogs.com/xueqiuqiu/articles/12935959.html
    再安装brew install allure
    查看版本 allure --version
    """
# linux 或 macos版
"""
    生成allure结果数据
    '--alluredir=../report/reportallure'    生成结果目录
    生成allure结果html文件，
    allure generate ./allure报告数据生成的地址/ -o ./reporthtml/ --clean 生成报告 
"""
pytest.main(['../test_case/test_case_01.py', '--alluredir=../report/reportallure'])
"""
    然后在allure结果数据文件路径上层目录打开终端，使用 allure serve allure结果数据文件路径  
    也可使用 allure generate ./allure结果数据文件路径/ -o ./report/ --clean;
    再查看报告,打开页面报告allure open -h 127.0.0.1 -p 8883 ./report/
"""
#win版
"""
    运行命令生成allure数据报告
    pytest.main(['../test_case/test_case_01.py', '--alluredir=../report/reportallure'])
    在报告的目录中，运行 allure generate ./allure报告数据生成的地址/ -o ./reporthtml/ --clean 
"""