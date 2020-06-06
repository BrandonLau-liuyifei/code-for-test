#练习1
sum=0
for i in ["aaa",1,3,5,7,"bbb"]:
    try:
        type(i)==int
        sum=sum+i
    except:
        print("不是整数")
    else:
        print(i)
    finally:
        print("完成")
print(sum)

# 练习2
import pdb
def list_sort(T):
    """
    >>>list_sort([3,6,8,1])
    [1,3,6,8]
    """
    T.sort()
    print(T)
if __name__=="__main__":
    import doctest
    doctest.testmod()