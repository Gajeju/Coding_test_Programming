n = [int(input()) for _ in range(2)]

b1 = n[1] % 10
b10 = n[1] % 100 // 10
b100 = n[1] // 100

print(n[0] * b1)
print(n[0] * b10)
print(n[0] * b100)
print(n[0] * n[1])



# https://www.acmicpc.net/problem/2588