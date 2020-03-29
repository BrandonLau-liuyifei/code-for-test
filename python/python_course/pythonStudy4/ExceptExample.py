

def printlistbyInidex(list1, a, b):
    try:
        for i in range(a, b):
            print(list1[i])
    except:
        print("我被执行了")

def printlistbyInidex2(list1, a, b):
    try:
        for i in  range(a, b):
            print(list1[i])
    except Exception as e:
        print(e)
        print("我被执行了")

def printlistbyInidex3(list1, a, b):
    try:
        for i in  range(a, b):
            print(list1[i])
    finally:
        print("finally后的我被执行了")

def printlistbyInidex4(list1, a, b):
    try:
        for i in range(a, b):
            print(list1[i])
    except Exception as e:

        print(e)
        print("我被执行了")
        raise e  # 再次抛出异常，必须写在except后代码的最后一行
    finally:
        print("finally后的我被执行了")


if __name__ == "__main__":
    list1 = [3, 2, 2, 9]
    # printlistbyInidex2(list1, 0, 7)
    printlistbyInidex4(list1, 0, 6)
    print(list1)