m = int(input())
n = int(input())
arr = []

if m == 1:
    m += 1
if n == 1:
    print(-1)
    exit()

for num in range(m, n+1):
    for i in range(2,num):
        if num % i ==0:
            break
    else: arr.append(num)

if arr:
    print(sum(arr))
    print(arr[0])
else:
    print(-1)



# https://www.acmicpc.net/problem/2581