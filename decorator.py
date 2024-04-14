def tapper(f):
    def adding(lis):
        total=0
        f(lis)
        for j in lis:
            total+=j
        print(total)
    return adding

lis=[]
@tapper
def add(lis):
    n=int(input("enter the size of list : "))
    for i in range(n):
        a=int(input("enter the value : "))
        lis.append(a)
    print(lis)

add(lis)


