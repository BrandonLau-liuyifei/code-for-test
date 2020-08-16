"""
多线程秉性和分布式执行
pytest是pytest分布式执行插件，可以多个cpu或主机执行，这款插件允许用户将测试并发执行（进程级并发），插件是动态执行测试用例的顺序，
为保证各个测试能在独立的线程里正确执行，应保证测试用例的独立性。
安装：pip install pytest-xdist
多个测试cpu并行执行用例，需要在pytest后加 -n参数
pytest -n auto  如果参数auto，会自动检测系统的cpu数目
pytest -n [num] 如果参数为数字，则指定处理器的进程数
"""