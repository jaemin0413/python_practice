l=[]

while True:
    a=int(input("0이 아닌 숫자를 입력해주세요 "))
    l.append(a)

    if a==0:
        break

s=set(l)

print(s)
