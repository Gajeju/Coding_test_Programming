n = int(input())
is_leap = -1

if n % 400 == 0:
    is_leap = 1
elif n % 4 == 0 and n % 100 != 0:
    is_leap = 1
else:
    is_leap = 0

print(is_leap)


# https://www.acmicpc.net/problem/2753