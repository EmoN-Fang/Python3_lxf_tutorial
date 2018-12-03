#list。list是一种有序的集合，可以随时添加和删除其中的元素。
classmates = ['Michael', 'Bob', 'Tracy']
print(classmates)  #['Michael', 'Bob', 'Tracy']
print(len(classmates)) # 3
print(classmates[2]) # Tracy
print(classmates[-1]) # Tracy
#print(classmate[-4])  #Error
classmates.append('Adam')
print(classmates) #['Michael', 'Bob', 'Tracy', 'Adam']
classmates.insert(1, 'Jack')
print(classmates) #['Michael', 'Jack', 'Bob', 'Tracy', 'Adam']
print(classmates.pop()) #Adam
print(classmates)  #['Michael', 'Jack', 'Bob', 'Tracy']
classmates.pop(1) #Jack
print(classmates) #['Michael', 'Bob', 'Tracy']