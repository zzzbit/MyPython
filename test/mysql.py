'''
Created on 2015年3月17日

@author: zhangzhizhi
'''
import smtplib

message = """From zzz
to you
whlcome
"""
smtpObj = smtplib.SMTP()
smtpObj.sendmail("zzz", "bbb", message)