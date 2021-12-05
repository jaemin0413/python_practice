
def f(*n):
    a=0
    b=0
    for i in n:
        a+=i
    b=a/len(n)
    return(b)
