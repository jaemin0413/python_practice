#입력받은 횟수만큼 숫자 더하기
n=int(input("횟수를 입력해주세요: "))
for i in range(n):
    a,b=map(int,input("더할 숫자를 입력해주세요: ").split())
    print(a+b)