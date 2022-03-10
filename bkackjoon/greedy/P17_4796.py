import sys
input = lambda : sys.stdin.readline().strip()

t = 0

while True:
    l, p, v = map(int, input().split())
    
    if l == p == v == 0:
        break

    day = 0
    day += (v // p) * l
    day += v % p if (v % p) < l else l
    t += 1

    print(f'Case {t}: {day}')



# 연속하는 P일 L일 동안만 사용 가능
# 휴가남은 날짜 V
# 최대 캠핑 할 수 있는 일 수 

# https://www.acmicpc.net/problem/4796
