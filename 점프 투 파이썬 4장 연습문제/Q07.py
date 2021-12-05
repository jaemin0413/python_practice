f=open ("c:/파이썬연습/test.txt","r")
a=f.read()
f.close()

a=a.replace("java","python")

f=open("c:/파이썬연습/test.txt","w")
f.write(a)
f.close()
