a, b = input().split()

a = "".join(reversed(a))
b = "".join(reversed(b))
print(a if a > b else b)



# 숫자를 거꾸로 읽고 더 큰 수 출력

# https://www.acmicpc.net/problem/2908