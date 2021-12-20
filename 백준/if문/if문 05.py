#알람시계
a,b=map(int,input("시간과 분을 입력해주세요: ").split())
if 0<=a<=23 and 0<=b<=59:
    if b>=45:
        print(a,b-45)
    elif a==0 and b<=45:
        print(23,b+15)
    elif b<45:
        print(a-1,b+15)