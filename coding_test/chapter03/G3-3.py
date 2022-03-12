# 숫자 카드 게임
# 카드 중에서 가장 높은 숫자가 쓰인 카드 한 장을 뽑는 게임
# N * M 형태로 놓여 있다
# 행 선택
# 행에 포함된 카드 중에서 가장 낮은 숫자의 카드를 뽑아야 한다.
# 입력 n m 이후 카드

import time

start_time = time.time()


# sort 함수 key 옵션 사용 time: 5.8121178150177
# n, m = map(int, input().split())
# cards = [list(map(int, input().split())) for _ in range(n)]
# cards.sort(key=lambda x:min(x), reverse=True)
# print(min(cards[0]))


# min() 함수 사용 예시 time: 5.245570182800293
# n, m = map(int, input().split())
# result = 0
# for i in range(n):
#     data = list(map(int, input().split()))
#     min_value = min(data)
#     result = max(result, min_value)
# print(result)

# 2중반복문 timeL time:  6.367682456970215
n, m = map(int, input().split())
result = 0
for i in range(n):
    data = list(map(int, input().split()))
    min_value = 10001
    for a in data:
        min_value = min(min_value, a)
    result = max(result, min_value)
print(result)


end_time = time.time()
print('time: ', end_time - start_time)
