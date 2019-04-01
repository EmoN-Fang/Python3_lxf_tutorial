age = 5
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')


#this is wrong, 不应该先判断>=6
age = 20
if age >= 6:
    print('teenager')
elif age >= 18:
    print('adult')
else:
    print('kid')

#只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False。
x = 0.1
if x:
    print('True')

#input()返回数据默认为str，无法与整数比较，需先转成整数
s = input('birth: ')
birth = int(s)    #要先转换成int
if birth < 2000:
    print('00前')
else:
    print('00后')