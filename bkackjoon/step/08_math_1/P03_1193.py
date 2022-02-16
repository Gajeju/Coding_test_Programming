n = int(input())
row = 0
i = 0

# 몇 번째 줄인지 찾기
while i < n:
    row += 1
    i += row
    
i -= n

first = row - i
second = row - first + 1


if row % 2 == 0:
    print(F'{first}/{second}')
else:
    print(F'{second}/{first}')


# 줄의 홀짝 여부




# https://www.acmicpc.net/problem/1193