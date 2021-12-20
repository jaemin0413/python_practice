#윤년

a=int(input("년도를 입력해주세요: "))
if 0<a<4001:
    if a%4==0 and not a%100==0:
        print("1")
    elif a%400==0:
      print("1")
    else:
        print("0") 
