def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x

print(my_abs(-99))  #99

'''
可以用abstest.py保存my_abs()这个函数，然后在该文件的当前目录下用
from abstest import my_abs来导入 my_abs()这个函数。   这里from的是去掉.py的文件名
'''
'''
可以定义pass的空函数，让程序跑起来，后面再补全具体内容
'''
def nop():
    if age>= 18:
        pass

# my_abs(1,2)  #TypeError: my_abs() takes 1 positional argument but 2 were given
# my_abs('A') #    if x >= 0:  TypeError: '>=' not supported between instances of 'str' and 'int'

def new_my_abs(x):
    if not isinstance(x, (int, float)):  #内置函数，用于检测数据类型
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x
#new_my_abs('A')   #TypeError: bad operand type

'''
返回多个值
'''
import math
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

x, y = move(100, 100, 60, math.pi / 6)
print(x,y)     #151.96152422706632   70.0
'''
看上去是返回了两个值，但实际上是返回的单一值
'''
r = move(100, 100, 60, math.pi / 6)
print(r)        #(151.96152422706632, 70.0)  返回值其实是一个tuple

def quadratic(a,b,c):
    delta = b*b - 4*a*c
    ans1 = (-b + math.sqrt(delta)) / (2 * a)
    ans2 = (-b - math.sqrt(delta)) / (2 * a)
    return ans1, ans2

print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')


