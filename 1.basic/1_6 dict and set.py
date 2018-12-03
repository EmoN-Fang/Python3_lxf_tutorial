#查找同学成绩，用list实现，需要就先在names中找到对应的位置，再从scores取出对应的成绩，list越长，耗时越长。
names = ['Michael', 'Bob', 'Tracy']
scores = [95, 75, 85]

#用dict实现，dict的支持，dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度。
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Michael'])

#多次对一个key放入value，后面的值会把前面的冲掉：
d['Jack'] = 90
print(d['Jack']) #90
d['Jack'] = 88
print(d['Jack']) #88

#print(d['Thomas']) #不存在 会报error

print("Thomas" in d)  # False
print(d.get('Thomas')) # None
print(d.get('Thomas', -1))  #-1

#要删除一个key，用pop(key)方法，对应的value也会从dict中删除：
print(d.pop('Bob'))   #75
print(d)  #{'Michael': 95, 'Tracy': 85, 'Jack': 88}

'''
和list比较，dict有以下几个特点：
1.查找和插入的速度极快，不会随着key的增加而变慢；
2.需要占用大量的内存，内存浪费多。
而list相反：
1.查找和插入的时间随着元素的增加而增加；
2.占用空间小，浪费内存很少。
*所以，dict是用空间来换取时间的一种方法。
dict可以用在需要高速查找的很多地方。
需要牢记的第一条就是dict的key必须是不可变对象，因为dict根据key来计算value的存储位置
'''

#要保证hash的正确性，作为key的对象就不能变。在Python中，字符串、整数等都是不可变的，因此，可以放心地作为key。而list是可变的，就不能作为key：
key = [1, 2, 3]
#d[key] #unhashable type: 'list'

'''
set
set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。
要创建一个set，需要提供一个list作为输入集合：
'''
s = set([1,2,3,])
print(s)  #{1, 2, 3} 传入的参数[1, 2, 3]是一个list，而显示的{1, 2, 3}只是告诉你这个set内部有1，2，3这3个元素，显示的顺序也不表示set是有序的

#重复元素在set中自动被过滤：
s = set([1, 1, 2, 2, 3, 3])
print(s)  #{1, 2, 3}

#通过add(key)方法可以添加元素到set中，可以重复添加，但不会有效果：
s.add(4)
print(s)  #{1, 2, 3, 4}
s.add(4)
print(s)  #{1, 2, 3, 4}

#通过remove(key)方法可以删除元素：
s.remove(4)
print(s)  #{1, 2, 3}

#set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作：
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print(s1 & s2)   #{2, 3}
print(s1 | s2)   #{1, 2, 3, 4}

#str是不变对象，而list是可变对象
#对于可变对象，比如list，对list进行操作，list内部的内容是会变化的，比如：
a = ['c', 'b', 'a']
a.sort()
print(a) #['a', 'b', 'c']

#而对于不可变对象，比如str，对str进行操作呢, a.replace是生成了一个新的值而不是原地修改，但可通过b= 赋值
a = 'abc'
print(a.replace('a', 'A'))  #Abc
b = a.replace('a', 'A')
print(b)  #Abc
print(a)    #abc

'''
所以，对于不变对象来说，调用对象自身的任意方法，也不会改变该对象自身的内容。相反，这些方法会创建新的对象并返回，这样，就保证了不可变对象本身永远是不可变的
'''

aa = (1, 2, 3)
bb = (1, [2, 3])

s = set(aa)
print(s)  #{1, 2, 3}  aa不可修改所以出现了
g = set(bb)
print(g)  #没出现任何东西