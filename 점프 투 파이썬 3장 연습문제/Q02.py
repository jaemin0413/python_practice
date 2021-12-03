a=0
b=0

while a<1001:
    if a%3==0:
        print(a, end=" ")
        b+=a
    a+=1

print()
print("1부터 1000까지 3의 배수의 합", b)
