print('100 + 200 =', 100 + 200)

#Input
name = input('Please enter your name: ')
print('Hello,', name)

# integer and float:
a = 0x0011  #this is integer
b = 1.23e5  #this is float
if a <= 0:
    print(a)
else:
    print(b)

# string and /
print('I\'m \"OK\" and learning\nPython.')  # I'm "OK" and learning (use\ to output the original symbol)
print('\\\n\\')     #\
                    #\
print('\\\t\\')     #\  \
print(r'\\\t\\')    #\\\t\\
print('''line1      
line2
line3''')       #line1
                    #line2
                    #line3   (use '''...''' to write things in several lines)

#Boolen
print(not True or False)  #False
print(5 > 3 or 1 > 3)   #True
print(not 1 > 2)    #True

#Python是动态语言
a = 13
b = a
a = 'XYZ'
print('b =', b)

# Const
print(10/3)  #3.3333333333333335 （结果是浮点数）
print(9/3)  #3.0 （结果仍是浮点数）
print(10//3) #3 结果取整
print(10%3) #1 余数

print(-10//3) #-4
print(-10%3) #2

n = 123
f = 456.789
s1 = 'hello,world'
s2 = 'Hello, \'Adam\''
s3 = r'Hello, "Bart"'
s4 = r'''Hello,
Lisa!'''
print(n,s1,s2,s3,s4,sep = '\n')