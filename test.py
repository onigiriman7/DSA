# def knapSack(arr):
#     prefix = []
#     suffix = []
#     start = arr[0]
#     stop = arr[len(arr)-1]
#     # for i in range(len(arr)):
#     #     if 
    
# print(knapSack([16, 17 ,4, 3,5, 2]))

# def kaden(arr, n):
#     t = [0]*(len(arr))
#     for i in range(1,len(arr)):
#         t[i] = max(arr[i-1]+t[i-2], t[i-1])
#     #print(t)
#     return t[len(t)-1]

# print(kaden([1,2,3,4,-10],5))

def isEqual(a, b):
    if a==b:
        return 1
    else:
        return 0

def partition(arr, n):
    if n == 0 or n ==1:
        return 0
    return isEqual(arr[n-1] + partition(arr, n-1), partition(arr,n-1))
       
print(partition([1,2,5,2], 4))