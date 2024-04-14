# arr = [30, 40, 12, 11, 10, 20]
# n = 2
# newarr = []
# def Lshift(arr, n):
#     for i in range(len(arr)):
#         index = (i + n) % len(arr)
#         newarr.insert(index, arr[i])
# Lshift(arr, n)
# print(newarr)

def LShift(Arr, n):
    length = len(Arr)
    print(length)
    Arr = Arr[n % length:] + Arr[:n % length] 
    print(Arr)
    return Arr
Arr = [10, 20, 30, 40, 12, 11]
n = 2
print("Original Array:", Arr)
print("Left Shifted Array:", LShift(Arr, n))
