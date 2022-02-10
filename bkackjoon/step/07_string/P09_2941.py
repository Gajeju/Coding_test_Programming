s = input()
croa = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

ln = len(s)

for c in croa:
    ln -= s.count(c)

print(ln)

# https://www.acmicpc.net/problem/2941