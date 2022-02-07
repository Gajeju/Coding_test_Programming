n_list = [int(input()) for _ in range(3)]


result = 1
for n in n_list:
    result *= n
result = str(result)

for i in range(10):
    print(result.count(str(i)))





# https://www.acmicpc.net/problem/2577