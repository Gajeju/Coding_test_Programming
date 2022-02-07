n = int(input())
n_list = [sum(list(map(int, input().split()))) for _ in range(n)]

print(*n_list, sep='\n')


# https://www.acmicpc.net/problem/10950