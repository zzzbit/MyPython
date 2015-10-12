'''
Created on 2015年3月17日

@author: zhangzhizhi
'''
import re
line = "aaabbhsdfk3847sdfaabb"

matchObj = re.search(r'b.*?b', line, re.M|re.I)
if matchObj:
    print(matchObj.group())
    print(matchObj.group(0))
else:
    print("no match")