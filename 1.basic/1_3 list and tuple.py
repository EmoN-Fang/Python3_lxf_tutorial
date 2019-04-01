'''
list: []    list是一种有序的集合，可以随时添加和删除其中的元素。
'''
classmates = ['Michael', 'Bob', 'Tracy']
print(classmates)  #['Michael', 'Bob', 'Tracy']
print(len(classmates)) # 3
#索引
print(classmates[2]) # Tracy
print(classmates[-1]) # Tracy
#print(classmate[-4])  #Error
#插入
classmates.append('Adam')
print(classmates) #['Michael', 'Bob', 'Tracy', 'Adam']
classmates.insert(1, 'Jack')
print(classmates) #['Michael', 'Jack', 'Bob', 'Tracy', 'Adam']
#删除
print(classmates.pop()) #Adam
print(classmates)  #['Michael', 'Jack', 'Bob', 'Tracy']
classmates.pop(1) #Jack
print(classmates) #['Michael', 'Bob', 'Tracy']
#更改
classmates[1] = 'Sarah'
print(classmates) #['Michael', 'Sarah', 'Tracy']

#不同类型
L = ['Apple', 123, True]
s = ['python', 'java', ['asp', 'php'], 'scheme']
print(len(s))   #4
#和这个一样：
p = ['asp', 'php']
s = ['python', 'java', p, 'scheme']
print(s[2][1])  #php

'''
tuple:()    tuple和list非常类似，但是tuple一旦初始化就不能修改，比如同样是列出同学的名字：
'''
t = (1, 2)
print(t)   #(1,2)
# t[1] = 3  #TypeError: 'tuple' object does not support item assignment
print('t[1]=',t[1])
t = ()
print(t)   #()
t = (1)
print(t)  #1 !!! 这里（）变成了一种运算符号，所以没有变成tuple
t = (1,)
print(t) #(1,) 在显示只有1个元素的tuple时，也会加一个逗号,，以免误解成数学计算意义上的括号。

#一个可变的tuple
t = ('a', 'b', ['A', 'B'])
t[2][0] = 'X'
t[2][1] = 'Y'
print(t)  #('a', 'b', ['X', 'Y']) tuple的元素确实变了，但其实变的不是tuple的元素，而是list的元素。
        # tuple一开始指向的list并没有改成别的list，所以，tuple所谓的“不变”是说，tuple的每个元素，指向永远不变。指向一个list，就不能改成指向其他对象，但指向的这个list本身是可变的！


#作业
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]

print(L[0][0])