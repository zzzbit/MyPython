# My program
import sys
try:
    file = open("hello.txt","r")
except IOError:
    print("file error")
    sys.exit()
filetext = file.read()
file.close()
print(filetext)

try:
    file = open("hi.txt","w")
except IOError:
    print("file error")
    sys.exit()
print('Please Enter:')
file_text=""
while file_text != "q":
    file_text = input("Enter text:")
    file.write(file_text)
    file.write("\n")
file.close()
    