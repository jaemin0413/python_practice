n=[]

while True:
    a=int(input("0을 제외한 숫자를 입력해주세요: "))
    n.append(a)
    if a==0:
        break

l=[i*2 for i in n if i%2==1]

print(l)
