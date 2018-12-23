'''
调用函数
'''
a = abs(-100)
print(a)     #100
b = abs(12.34)
print(b)    #12.34
# c = abs(1,2)
# print(c)  #TypeError: abs() takes exactly one argument (2 given)
d = abs(a)
print(d)    #100
# e = abs("a")
# print(d)    #TypeError: bad operand type for abs(): 'str'
f = max(2, 3, 1, -5)
print(f)    #3

'''
数据类型转换
'''
print(int('123'))   #123
print(int(12.34))   #12
print(float('12.34'))   #12.34
print(float('12'))  #12.0
print(str(1.23))    #'1.23'
print(bool(-1))     #True
print(bool(0))      #False
print(bool(''))     #False

"""
函数名可以用引用
"""
f_a = abs
print(f_a(-1))  #1
f_16 = hex
print(f_16(255)) #0xff
print(f_16(10000000)) #0x989680