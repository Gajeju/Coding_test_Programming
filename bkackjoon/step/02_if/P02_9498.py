n = int(input())
result = ''

if 90 <= n <= 100:
    result = 'A'
elif 80 <= n <= 89:
    result = 'B'
elif 70 <= n <= 79:
    result = 'C'
elif 60 <= n <= 69:
    result = 'D'
else:
    result = 'F'
print(result)


# https://www.acmicpc.net/problem/9498