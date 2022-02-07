n = int(input())

n_list = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    print(f'Case #{i+1}: {n_list[i][0]} + {n_list[i][1]} = {n_list[i][0] + n_list[i][1]}')

 
# https://www.acmicpc.net/problem/11022