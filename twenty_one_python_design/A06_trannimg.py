class me:
    name="liuyifei"
    age=28
    weight=75
    tall=172.3
    my_parents="爸爸和妈妈"
    def __init__(self,i=0,j=0,girl="good people",kids="boy"):
        self.i=i
        self.j=j
        self.girl=girl
        self.kids=kids
    def work(self,i):
        self.i=i
        weight=me.weight-0.01*self.i
        print("工作体重会减少到",weight)
    def eat(self,j):
        self.j=j
        weight = me.weight + 0.01 * self.j
        print("吃饭体重会增加到",weight)
    def love(self,girl):
        self.girl=girl
        print("fall in love with a %s" % self.girl)
    def family(self,kids):
        self.kids=kids
        print("会有一个孩子名字叫%s" % self.kids)
        print('未来的家会很好,我和%s和%s和%s生活在一起' % (me.my_parents,self.girl,self.kids))
my_info=me()
print("我是%s,身高%s,体重%s" % (me.name,me.tall,me.weight))
my_info.work(100)
my_info.eat(100)
my_info.love("beautiful and good girl")
my_info.family("liuziyu")

class Ant:
    def __init__(self,x=0,y=0,color="black"):
        self.x=x
        self.y=y
        self.color=color

    def crawl(self,x,y):
        self.x=x
        self.y=y
        print("爬")
        self.info()

    def info(self):
        print("当前位置：(%d,%d)" % (self.x,self.y))

    def attack(self):
        print("用嘴咬")

class fly_Ant(Ant):
    def attack(self):
        print("用嘴咬")
        print("尾巴针")

    def fly(self,x,y):
        self.x=x
        self.y=y
        print("飞")
        self.info()
class Final_Ant(Ant,fly_Ant):

    def jump(self,x,y):
        self.x=x
        self.y=y
        print("最终版的蚂蚁会跳")
        self.info()
    def attack(self):       #方法重载
        print("我变的会拿身子撞击了")


flyant=fly_Ant()
flyant.crawl(3,5)
flyant.fly(6,8)
flyant.attack()
finalant=Final_Ant()
finalant.crawl(8,8)
finalant.fly(3,3)
finalant.jump(3,2)
finalant.attack()




