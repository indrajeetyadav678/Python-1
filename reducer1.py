# Note :- map(), filter() and reduce() is also a higher order function 
#because it take a function as an argument


import functools

def greatest(a,b):
    if a>b:
        return a
    return b

lis=[22,23,24,56,7,3]
a=functools.reduce(greatest, lis)   
#here is list type cast is no required because from this function we get one value

print(a)

def smallest(a,b):
    if a<b:
        return a
    return b

print(functools.reduce(smallest, lis))

print(functools.reduce(lambda a, b: a+b , lis))
 # reduce is use for getting output in an one value  from iterable list
#=========================== map() =========================
lis1=[3,5,7,9,2,10]
newarr= map(lambda a: a**2, lis1 )
print(list(newarr))

def cube(v):
    return v**3

print((map(cube, lis1)))
print(list(map(cube, lis1)))
 # map() is use for creating a new list of function performing  value
 # in map() we perform a operation on every single element of list 
# ===================== filter() =====================

# filter () function is use to create a new list of filter elemnt in any list

lis2 =[3,5,6, 8, 9,112, 30,45]

newar =filter(lambda x : x%2==0 , lis2)
print (list(newar))

def stringfun(x):
    if x[0]=='a':
        return True
    else:
        return False
    
s=['aman', 'mohan', 'amit', 'ashok','gopal', 'rohan'] 
print(list(filter(stringfun, s)))

