n = int(input())

cycle = 1
tmp_n = (n // 10) + (n % 10)
new_n = (n % 10 * 10) + (tmp_n % 10)

while n != new_n:
    tmp_n = (new_n // 10) + (new_n % 10)
    new_n = (new_n % 10 * 10) + (tmp_n % 10)
    cycle += 1

print(cycle)





# 0보다 크고 99보다 작은 정수
# 정수가 10보다 작다면 앞에 0을 붙여 두 자리로 만들고, 각 자리의 숫자를 더한다.
# 주어진 수의 가장 오른쪽 자리 수와 앞에서 구한 합의 가장 오른쪽 수를 이어 붙인다

# https://www.acmicpc.net/problem/1110