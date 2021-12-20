#1부터 n개까지 별 찍기(오른쪽 정렬)
a=int(input("별 숫자를 입력해주세요: "))
for i in range(1,a+1):
    print(" "*i,"*"*i)