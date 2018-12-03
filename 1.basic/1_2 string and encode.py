#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
ASCII code 一般只用1个byte，即2^8, 0-255 只能表示英文字母、数字和一些符号
Unicode 一般用2个byte，偏僻的用4个。可以表示中文等任意符号
本着节约的精神， Unicode被转化为1-6个字节。常用的英文字母被编码成1个字节，汉字通常是3个字节，只有很生僻的字符才会被编码成4-6个字节。
如果你要传输的文本包含大量英文字符，用UTF-8编码就能节省空间。
字符	ASCII	    Unicode	            UTF-8
A	    01000001	00000000 01000001	01000001
中	    x	        01001110 00101101	11100100 10111000 10101101
搞清楚了ASCII、Unicode和UTF-8的关系，我们就可以总结一下现在计算机系统通用的字符编码工作方式：
在计算机内存中，统一使用Unicode编码，当需要保存到硬盘或者需要传输的时候，就转换为UTF-8编码。
用记事本编辑的时候，从文件读取的UTF-8字符被转换为Unicode字符到内存里，编辑完成后，保存的时候再把Unicode转换为UTF-8保存到文件：
'''
#python3以unicode形式编码
print('包含中文的str')
#ord()函数获取字符的整数表示：
print(ord('A'))  #65
print(ord('中')) #20013
#chr()函数把编码转化为对应的字符：
print(chr(66))  #B
print(chr(25991)) #文
#可以用十六进制写str
print( '\u4e2d\u6587')  #中文

#用b前缀的单引号或双引号表示byte类型
print('ABC'.encode('ascii')) #b'ABC'
print('中文'.encode('utf-8')) #b'\xe4\xb8\xad\xe6\x96\x87'  对于无法显示为ASCII的字节，用\x##显示
#print('中文'.encode('ascii')) 无法decode 会报错。

#反过来这么做
print(b'ABC'.decode('ascii')) #'ABC'
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')) #'中文'

#如果bytes中只有一小部分无效的字节，可以传入errors='ignore'忽略错误的字节：
print(b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore')) #'中'

#格式化
print('Hi, %s, you have $%d.' % ('Michael', 1000000)) #'Hi, Michael, you have $1000000.'
#常见占位符
#占位符	替换内容
#%d	整数
#%f	浮点数
#%s	字符串
#%x	十六进制整数

#决定是否补0以及整数和小数的位数
print('%2d-%02d' % (3e8, 10))
print('%.3f' % 3.1415926)
print('Age: %s. Gender: %s' % (25, True)) #Age: 25. Gender: True

#多一个%来进行转义
print('growth rate: %d %%' % 7) #'growth rate: 7 %'

#format()
print( 'Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125))  #Hello, 小明, 成绩提升了 17.1%

s1 = 72
s2 = 85
r = (s2 - s1)/s1 *100
print('小明今年的成绩提高了： %f %%' % r)