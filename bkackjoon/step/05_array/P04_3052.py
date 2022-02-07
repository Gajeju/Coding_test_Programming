ty = 10     # 입력 횟수 
n_list = [int(input()) for _ in range(ty)]
n_remainder = [n_list[i] % 42 for i in range(ty)]

cnt = 0
for i in range(42):
    if n_remainder.count(i) != 0:
        cnt += 1

print(cnt)


# https://www.acmicpc.net/problem/3052