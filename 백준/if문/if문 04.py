#사분면 고르기
a=int(input("x좌표를 입력해주세요"))
b=int(input("y좌표를 입력해주세요"))
if -1000<= a <=1000 and -1000<= b <=1000 :
    if a>0 and b>0:
        print("1")
    elif a<0 and b>0:
        print("2")
    elif a<0 and b<0:
        print("3")
    elif a>0 and b<0:
        print("4")
    