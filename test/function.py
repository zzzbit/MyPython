'''
Created on 2015年3月17日

@author: zhangzhizhi
'''
def myfunc(a):
    print(a*2)
    
myfunc("g")

def change(str):
    str[0] = 'a'
    print(str)
    
mystr = ["whynot",'a']
print(mystr)
change(mystr)
print(mystr)

def myadd(*myvar):
    for var in myvar:
        print(var)

myadd(2,3,4)

sum = lambda a,b:a+b
print(sum(324,4))