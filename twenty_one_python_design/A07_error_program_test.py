# 7 错误、异常和程序调试
# 7.1 语法错误
"""
关键字、变量名、函数名写错,系统报SyntaxError
脚本不符合逻辑规范
缩进错误
"""
for i in range(3):
    print(i)

# 7.2 异常的处理
"""try:
    <语句(块)>            可能产生异常的语句
except <异常名1>:         要处理的异常1
    < 语句(块) >          异常处理语句
except <异常名1>:         要处理的异常2
    < 语句(块) >          异常处理语句
......
else:
    <语句(块)>            未出发异常，执行该该句
finally:
    < 语句(块) >          始终执行该句，一般为了达到释放资源的目的
"""
"""
情景1：
try:
    <语句(块)>
except <异常名1>:
    < 语句(块) >
"""
def TestTry(index,flag=False):
    stulst = ["Jhon","Jenny","Tom"]
    if flag==False:
        try:
            astu = stulst[index]
        except IndexError:
            print("IndexError")
        return "Try Test Finished"
    else:
        astu = stulst[index]
        return "No Try Test Finished"
print("Right params testing start......")
print(TestTry(1,True))
print(TestTry(1,False))
# print("Error params testing start......")
# print(TestTry(4,True))
# print(TestTry(4,False))

"""
情景1：
try:
    <语句(块)>
except <异常名1>:
    < 语句(块) >
finally:
    < 语句(块) >
"""
def testTryFinally(index):
    stulst = ["Jhon", "Jenny", "Tom"]
    af = open("my text","wt+")
    try:
        af.write(stulst[index])
    except:
        pass
    finally:
        af.close()
        print("file already had been closed!")
print("no IndexError......")
testTryFinally(1)
print("IndexError...")
testTryFinally(4)

"""
dir(__builtins__) 内建异常
except语法
except：     捕获所有异常
except(异常名):    捕获指定异常
except(异常名1，异常名2)：    捕获异常1或异常2
except <异常名> as <数据>：   捕获指定异常及附加的数据
except(异常1，异常名2) as <数据>：捕获异常名1或异常名2及异常附加数据
"""
# 捕获所有异常,程序不会中断
def testTryAll(index,i):
    stulst = ["John","Jenny","Tom"]
    try:
        print(len(stulst[index])/i)
    except:
        print("Error")
print("Try all ... right")
testTryAll(1,2)
print("Try all ... one Error")
testTryAll(1,0)
print("Try all ... one Error")
testTryAll(4,0)
# 捕获部分异常，程序引发了不能被捕获的异常，仍然中断
def testTryOne(index,i):
    stulst = ["John","Jenny","Tom"]
    try:
        print(len(stulst[index])/i)
    except IndexError:
        print("Error")
print("Try One ...... Right")
testTryOne(1,2)
print("Try one ...... one Error")
testTryOne(4,2)
# print("Try one ...... one Error")
# testTryOne(1,0)

# 7.3 手工抛出异常
"""
7.3.1 用raise手工抛异常
raise语句来引发指定的异常，并向异常传递数据，也可以抛出各种预定异常，即使程序在运行过程时根本不会引发该异常
raise 异常名
raise 异常名 附加数据
raise 类名
"""
# 代码抛出异常，没有捕获该异常，所以会中断，导致后面代码不会运行
# def testRaise():
#     for i in range(5):
#         if i ==2:
#             raise NameError
#         print(i)
#     print("end=...")
# testRaise()
# 代码抛出异常，有捕获该异常，所以不会中断运行
def testRaise2():
    for i in range(5):
        try:
            if i==2:
                raise NameError
        except NameError:
            print("Raise a NameError")
        print(i)
    print("end...")
testRaise2()
"""
7.3.2 assert 语句
assert,<条件测试>,<异常附加数据>    #其中异常附加数据是可选的
引发异常前提是后面的条件测试为假，同时抛出异常和捕获异常
使用python -O 来执行会关闭assert语句
"""
def testAssert():
    for i in range(3):
        try:
            assert i<2
        except AssertionError:
            print("Raise a AssertionError")
        print(i)
    print("end=...")
testAssert()

# 7.3.3 自定义异常类（继承于Exception）
"""
class MyError()
    pass
如需要异常类带有一定的提示信息，也可以重载__init__和__str__
"""
class RangeError(Exception):
    def __init__(self,value):
        self.value = value

    def __str__(self):
        return self.value

raise RangeError('Range Error')

# 7.4 用pdb调试程序
"""
python自带的pdb模块，其功能设有断点、但单步执行、查看变量等。
可以使用命令行形式启动，也可以导入模块使用。
常用函数：
pdb模块中的调试语句块的函数及参数原型为：
run(statement[,globals[,locals]])
statement 要调用的语句块，以字符串的形式表示；
globals 可选参数，设置statement运行的全局变量
locals 可选参数，设置statement运行的局部变量
"""

import pdb

pdb.run("""
for i in range(3):
    print(i)
""")
"""
> <string>(2)<module>()
(Pdb) 
(Pdb) help

Documented commands (type help <topic>):
========================================
EOF    c          d        h         list      q        rv       undisplay
a      cl         debug    help      ll        quit     s        unt      
alias  clear      disable  ignore    longlist  r        source   until    
args   commands   display  interact  n         restart  step     up       
b      condition  down     j         next      return   tbreak   w        
break  cont       enable   jump      p         retval   u        whatis   
bt     continue   exit     l         pp        run      unalias  where    

Miscellaneous help topics:
==========================
exec  pdb

(Pdb) exec
<built-in function exec>
(Pdb) n
> <string>(3)<module>()
(Pdb) continue
0
1
2
"""

# 7.4.2 调试函数
"""
runcall(function[,argument,...])
function 函数名
argument 函数的参数
"""
import pdb

def sum(maxinit):
    s = 0
    for i in range(maxinit):
        s+=i
    return s
pdb.runcall(sum,10)

# 7.5 测试程序
"""
python标准库中doctest、unittest模块用于测试
本节使用doctest中的testmod函数和testfile函数进行简单的单元测试
"""
"""7.5.1 使用doctest模块的testmod进行单元测试，
将测试用例写进代码行中
也可以使用python -m doctest py文件执行"""
import pdb
def grade(sum):
    """
    >>> grade(100)
    '优秀'
    >>> grade(90)
    '良'
    >>> grade(65)
    '及格'
    >>> grade(10)
    '不及格
    """
    if sum > 90:
        return "优秀"
    if sum > 80:
        return "良"
    if sum > 65:
        return "及格"
    if sum > 10:
        return "不及格"
if __name__=="__mian__":
    import doctest
    doctest.testmod()
# 使用testfile函数测试，将用例写进txt文件中，进行测试
import pdb
def grade(sum):
    """
    if sum > 90:
        return "优秀"
    if sum > 80:
        return "良"
    if sum > 65:
        return "及格"
    if sum > 10:
        return "不及格"

# 将测试用例写进txt文件中
from test import grade
    >>> grade(100)
    '优秀'
    >>> grade(90)
    '良'
    >>> grade(65)
    '及格'
    >>> grade(10)
    '不及格
    """
"""
执行过程：交互模式下
        import doctest
        doctest.testfile("mytest.txt")
        命令行模式下
        python -m doctest mytest.txt
"""








