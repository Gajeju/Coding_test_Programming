n = int(input())

for i in range(n):
    print(' ' * (n-i-1), end='')
    print('*' * (i+1))
 
# https://www.acmicpc.net/problem/2439