"""
执行脚本：
命令行进入
cd test_scope/
pytest -v -s test_06_01_scope1.py test_06_02_scope2.py
或python执行见下
"""
import pytest

if __name__ == "__main__":
   pytest.main(['-v','-s'])