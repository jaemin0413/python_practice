l=[]

while True:
    n=input("문장을 만들 단어를 입력한 후 stop을 입력하세요 ")
    l.append(n)

    if n.lower()=="stop":
        break

l.remove("stop")

L=" ".join(l)

print (L)
