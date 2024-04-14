from functools import reduce
def sumfun(a, b):
    return a%b
    

lis=[2,4,6,8,12,10]
total=reduce(sumfun,lis)
print(total)

# def even_odd(a):
#     if a%2==0:
#         return True
#     else:
#         return False

    
# #print(even_odd(24))

# lis=[22,23,24,56,7,3]
# a=list(filter(even_odd,lis))
# print(a)