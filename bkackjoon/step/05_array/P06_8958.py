import sys

n = int(input())

for _ in range(n):
    result = sys.stdin.readline()
    score = 0
    conti = 0
    for s in result:
        if s == 'O':
            conti += 1
            score += conti
        else:
            conti = 0
    print(score)

    



# https://www.acmicpc.net/problem/8958