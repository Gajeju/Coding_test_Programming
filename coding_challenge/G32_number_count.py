# 1부터 N까지의 숫자를 일렬로 늘어놓았을 때,
# 0부터 9까지의 숫자가 각각 몇 번씩 나오는지 알아내는 프로그램을 만드세요.
import sys

n = int(sys.stdin.readline())
n_list = [0] * 10 

for i in range(1, n+1):
    for j in str(i):
        n_list[int(j)] += 1
        
print(*n_list)
