n = int(input())
n_list = list(map(int, input().split()))

m = max(n_list)
n_mani = [n_list[i] / m * 100 for i in range(n)]

print(sum(n_mani) / n)

# https://www.acmicpc.net/problem/1546