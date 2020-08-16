import pytest

class TestFunc():

    def test_case1(self):
        print("test_case1")
        pass

    def test_case2(self):
        print("test_case2")
        pass

    def test_case3(self):
        print("test_case3")
        pass

if __name__ == "__main__":
    pytest.main(['-v','-s','test_06_02_scope2.py'])
