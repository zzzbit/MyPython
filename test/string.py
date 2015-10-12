'''
Created on 2015年3月17日

@author: zhangzhizhi
'''
str="aaabbbccc"
print(str[0])
print(str[2:4])
print(str[2:-1])
print(str[5]+"ggo")

list=[23,'d',3.0,[12,23]]
print(list)
print(list[0:1])
print(list[2:3]+["g"])
print(list[3])

mytuple=('a',12,'45',('12','23'))
print(mytuple)
print(mytuple[-1:])
print(mytuple[3])

if mytuple[2] == 'a':
    print("good")

list.append('34')
print(list)

dict={}
dict['a']='b'
dict['b']='c'
print(dict)
print(dict['a'])

a = 'd'
if a in list:
    print('hi')
else:
    print('he')