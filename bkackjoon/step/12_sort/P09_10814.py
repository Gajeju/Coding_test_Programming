import sys

n = int(sys.stdin.readline())
members = []

for _ in range(n):
    age, name = sys.stdin.readline().split()
    members.append([int(age), name])

members.sort(key=lambda x:x[0])

for member in members:
    print(*member)


# 나이가 이름이 주어진다
# 나이순 정렬, 나이가 같으면 먼저 가입한 사람이 앞에
# https://www.acmicpc.net/problem/10814