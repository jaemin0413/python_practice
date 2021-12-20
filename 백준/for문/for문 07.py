#계산횟수를 입력받고 케이스별로 나눠서 출력
n=int(input("횟수를 입력해주세요: "))
for i in range(n):
    a,b=map(int,input("더할 숫자를 입력해주세요: ").split())
    print("Case #{0}:".format(i+1),a+b)