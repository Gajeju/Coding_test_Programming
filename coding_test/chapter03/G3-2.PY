# 큰 수의 법칙
# 배열이 있을 때 주어진 수들을 M번 더하여 가장 큰 수를 만드는 법칙
# 배열의 특정한 인덱스에 해당하는 수가 연속해서 K번을 초과하여 더해질 수 없다.

# 배열의 크기 N, 더해지는 횟수 M, K가 주어질 대 결과 출력

n, m, k = map(int, input().split())
array = list(map(int, input().split()))

array.sort(reverse=True)
tot = 0

# while m > 0:
#     if m >= k:
#         tot += (array[0] * k)
#         tot += array[1]
#         m -= k + 1
#     elif m == k:
#         tot += (array[0] * k)
#         m =0
#     else:
#         tot += (array[0] * m)
#         m = 0

# print(tot)h


count = int(m / (k + 1)) * k
count += m * (k+1)

tot += (count) * array[0]
tot += (m - count) * array[1]

print(tot)