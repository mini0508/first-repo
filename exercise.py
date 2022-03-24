n = int(input()) 
arr = list(map(int,input().split()))
arr = arr.sort()

result = 0

for i in arr:
    arr[i+1]+=arr[i]
    result = arr[0] + arr[i+1]
print(result)