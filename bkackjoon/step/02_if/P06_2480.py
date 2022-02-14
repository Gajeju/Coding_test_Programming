a = list(map(int, input().split()))

if a[0] == a[1] == a[2]:
    print(10000 + (a[0] * 1000))
elif a[0] == a[1] or a[0] == a[2] or a[1] == a[2]:
    for i in a:
        if a.count(i) == 2:
            print(1000 + (i * 100))
            break
else:
    print(100 * max(a))





# 주사위 3개 던진다
# 같은 눈 3개 : 10000 + 눈 * 1000
# 같은 눈 2개 : 1000 + 눈 * 100
# 모두 다른 눈 : 가장 큰 눈 * 100

# https://www.acmicpc.net/problem/2480