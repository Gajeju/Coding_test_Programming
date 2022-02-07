n_list = [int(input()) for _ in range(9)]

n_max = max(n_list)
print(n_max, n_list.index(n_max)+1, sep='\n')

# https://www.acmicpc.net/problem/2562