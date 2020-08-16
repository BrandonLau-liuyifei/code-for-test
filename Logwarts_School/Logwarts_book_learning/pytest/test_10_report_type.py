"""
pytest 报告
    生成html报告
    '--html=../report/report.html'
    pytest.main(['../test_case/test_case_01.py','--html=../report/report.html'])
    生成xml报告
    '--junitxml=../report/report.xml'
    pytest.main(['../test_case/test_case_01.py', '--junitxml=../report/report.xml'])
    生成allure结果数据
    '--alluredir=../report/reportallure'    生成结果目录
    pytest.main(['../test_case/test_case_01.py', '--alluredir=../report/reportallure'])
    生成allure结果html文件，
    allure generate ./allure报告数据生成的地址/ -o ./reporthtml/ --clean 生成报告
    pytest报告使用详见/Users/mac/PycharmProjects/songqin_test_course/interface_test/interface_test_whole_02/run_case/run_all_case.py
"""