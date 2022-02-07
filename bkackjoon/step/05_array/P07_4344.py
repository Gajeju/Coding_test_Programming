c = int(input())

for _ in range(c):
    n_list = list(map(int, input().split()))
    avg = (sum(n_list[1:])) / n_list[0]
    cnt = 0

    for score in n_list[1:]:
        if score > avg:
            cnt += 1
    print(f'{cnt / n_list[0] *100:.3f}%')





# https://www.acmicpc.net/problem/4344