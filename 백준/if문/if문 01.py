#두 수 비교하기
a,b=map(int,input("숫자 두 개를 입력해주세요: ").split())
if a>b:
    print(">")
elif a<b:
    print("<")
else:
    print("==")