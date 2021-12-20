#시험점수 입력 후 학점 매기기
a=int(input("시험성적을 입력해주세요: "))
if 90<=a<=100:
    print("A")
elif 80<=a<=89:
    print("B")
elif 70<=a<=79:
    print("C")
elif 60<=a<=69:
    print("D")
elif 0<=a<=59:
    print("F")