while True:
    li = list(map(int, input().split()))

    if li[0] == li[1] == li[2] == 0:
        break

    hy = max(li)
    li.remove(hy)

    if (hy ** 2) == (li[0] ** 2) + (li[1] ** 2):
        print('right')
    else:
        print('wrong')




# 세 변이 주어지고 직각삼각형인지 판단
# 0 0 0 이 입력되면 종료

# https://www.acmicpc.net/problem/4153