# __author__ ：Nathaniel
# -*- coding: UTF-8 -*-

import unittest


def add(a, b):
    return a + b


def minus(a, b):
    return a - b


def multi(a, b):
    return a * b


def divide(a, b):
    return a / b


class CalculateTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("哈哈")

    def testAdd(self):
        print("加法")
        self.assertEqual(1 + 1, 2)


class StringTestCase(unittest.TestCase):
    def testHello(self):
        print("哈喽")
        self.assertTrue("hello world".endswith("d"))


if __name__=="__main__":
    unittest.main()