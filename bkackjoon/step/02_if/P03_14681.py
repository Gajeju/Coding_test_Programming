n = [int(input()) for _ in range(2)]
quadrant = -1

if n[0] > 0 and n[1] > 0:
    quadrant = 1
if n[0] < 0 and n[1] > 0:
    quadrant = 2
if n[0] < 0 and n[1] < 0:
    quadrant = 3
if n[0] > 0 and n[1] < 0:
    quadrant = 4

print(quadrant)


# https://www.acmicpc.net/problem/14681