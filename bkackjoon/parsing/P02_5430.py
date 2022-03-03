import sys

t = int(sys.stdin.readline())

for _ in range(t):
    func = sys.stdin.readline().rstrip()
    n = int(sys.stdin.readline())
    arr = sys.stdin.readline().rstrip()[1:-1].split(',')

    for f in func:
        if f == 'R':
            arr.reverse()
        elif f == 'D':
            print(arr)
            if arr:
                arr.remove(arr[0])
            else:
                print('error')
                break
    else:
        print("["+",".join(arr)+"]")



# 새로운 AC
# R - 뒤집기  /  D - 버리기
# 배얼이 비어있는데 D 사용시 에러
# D 사용시 배열의 첨수 수 버리기
# 첫째줄 함수 / 둘째줄 숫자 개수 / 셋째줄 리스트
# 테스트 케이스

# https://www.acmicpc.net/problem/5430