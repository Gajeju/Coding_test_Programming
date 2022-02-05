n = list(map(int, input().split()))

print((n[0] + n[1]) % n[2])
print(((n[0]%n[2]) + (n[1]%n[2]))%n[2])
print((n[0] * n[1]) % n[2])
print(((n[0]%n[2]) * (n[1]%n[2])) % n[2])




# https://www.acmicpc.net/problem/10430