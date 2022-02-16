n = int(input())
arr = list(map(int, input().split()))
cnt = 0

while 1 in arr:
    arr.remove(1)

for num in arr:
    for i in range(2,num):
        if num % i == 0:
            break
    else: cnt += 1

print(cnt)


# https://www.acmicpc.net/problem/1978