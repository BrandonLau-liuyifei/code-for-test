from pythonStudy4.ClassExample import people


from pythonStudy4.ClassExapmle2 import paixu
#实例化类people的一个对象
from pythonStudy4.FangWenKongZhi2Example import paixu2
from pythonStudy4.initExample import people2

p1 = people()   # 实例化people的对象并赋值给变量p1
p2 = people()   # 实例化people的对象并赋值给变量p2

# p1.age = 30
# p1.name = "小明"
# p1.speak()
# p2.age = 15
# p2.name = "阿福"
# p2.speak()
p1.name="思聪"  # 对象和对象的属性和方法归属对象自身，不会相互影响
p1.age=36
p2.name="建林"
p2.age=60
p1.speak()
# 实例化类paixu的对象
o1 = paixu()
list1 = [2,4,1,5,23,13,6,11,0]
o1.suoyinpaixu(list1, 3, 7)
#实例化people2类的对象,构造方法中设置了n和a两个形参，在实例化对象时必须传入两个参数
p3 = people2("马云", 60)
p3.speak()
o2 = paixu2()
o2.set_value(list1, 3, 7)
o2.suoyinpaixu()
o2.suoyinpaixu_public(list1, 3, 7)
