#f1을 닫지 않아 저장이 되지 않았기 때문

f1 = open("c:/파이썬연습/test.txt", 'w')
f1.write("Life is too short")
f1.close()

f2 = open("c:/파이썬연습/test.txt", 'r')
print(f2.read())
f2.close()

