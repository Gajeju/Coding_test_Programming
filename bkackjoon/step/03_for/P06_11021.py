n = int(input())

n_list = [sum(list(map(int, input().split()))) for _ in range(n)]
for i in range(n):
    print(f'Case #{i+1}: {n_list[i]}')


# https://www.acmicpc.net/problem/11021