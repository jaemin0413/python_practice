a=0
l=[]

while a<5:
    n=int(input("무작위 숫자를 입력해주세요 "))
    l.append(n)
    a+=1

    if a==5:
        break

l.sort()

print (l)
