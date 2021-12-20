#구구단
a=int(input("숫자를 입력해주세요: "))
for i in range(1,10):
    print("{0}*{1}={2}".format(a,i,a*i))