import sys
input = lambda  : sys.stdin.readline().strip()

t = int(input())

for i in range(t):
    func = input()
    n = int(input())
    arr = input()[1:-1].split(',')

    func.replace('RR', '')

    r, f, b = 0, 0, 0

    for j in func:
        if j == 'R':
            r += 1
        elif j == 'D':
            if r % 2 == 0:
                f += 1
            else:
                b += 1
    if f + b <= n:
        arr = arr[f:n-b]

        if r % 2 == 1:
            print('[' + ','.join(arr[::-1]) + ']')
        else:
            print('[' + ','.join(arr) + ']')
    else:
        print('error')

# 새로운 AC
# R - 뒤집기  /  D - 버리기
# 배얼이 비어있는데 D 사용시 에러
# D 사용시 배열의 첨수 수 버리기
# 첫째줄 함수 / 둘째줄 숫자 개수 / 셋째줄 리스트
# 테스트 케이스

# https://www.acmicpc.net/problem/5430