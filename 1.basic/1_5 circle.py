# -*- coding: utf-8 -*-
# For.. in
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)

#range()可以生成整数序列，再通过list()函数可以转换为list。
print(list(range(5))) #[0, 1, 2, 3, 4]

#就可以生成0-101的整数序列，range从0开始，不包括其自己
sum = 0
for x in range(101):
    sum = sum + x
print(sum)

#while
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)

# hello, Adam!
L = ['Bart', 'Lisa', 'Adam']
for name in L:
    print("Hello,", name + "!")  # ,会有空格  +不会有空格
#另一种写法
for name in L:
    print("hello, {}!".format(name))

#break语句可以提前退出当前循环体，即结束循环：
n = 1
while n <= 100:
    if n > 10: # 当n = 11时，条件满足，执行break语句
        break # break语句会结束当前循环
    print(n)
    n = n + 1
print('END')

#用continue可以提前结束本轮循环，并直接开始下一轮：
n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0: # 如果n是偶数，执行continue语句
        continue # continue语句会直接继续下一轮循环，后续的print()语句不会执行
    print(n)
