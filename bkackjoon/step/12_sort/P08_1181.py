import sys

n = int(sys.stdin.readline())
words = [input() for _ in range(n)]

# 중복제거
words = list(set(words))

words.sort(key=lambda x:[len(x), x])

for word in words:
    print(word)

# https://www.acmicpc.net/problem/1181