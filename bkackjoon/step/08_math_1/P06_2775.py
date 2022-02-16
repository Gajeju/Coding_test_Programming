t = int(input())

for _ in range(t):
    k = int(input())
    n = int(input())

    tot = []
    tot.append([i+1 for i in range(n)])
    
    for i in range(k):
        room = [] 
        for j in range(0,n):
            room.append(sum(tot[-1][0:j+1]))
        tot.append(room)
    
    print(tot[-1][-1])

    
    



# a층 b호에 살기 위해 a-1층의 1호부터 b호까지의 사람들의 수의 합만큼 사람들을 데려와 살야야 한다
# 현재 빈 집 없음
# 0층부터, 0층의 i호에는 i명이 산다
# k층 n호의 사람 수 구하기

# https://www.acmicpc.net/problem/2775