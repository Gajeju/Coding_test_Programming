n_list = []

while True:
    temp = list(map(int, input().split()))

    if temp[0] == 0 and temp[1] == 0:
        break

    n_list.append(temp)

for c in n_list:
    print(sum(c))

    


# https://www.acmicpc.net/problem/10952