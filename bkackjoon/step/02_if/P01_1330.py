n = list(map(int, input().split()))

if n[0] > n[1]:
    print('>')
elif n[0] < n[1]:
    print('<')
else:
    print('==')

# https://www.acmicpc.net/problem/1330