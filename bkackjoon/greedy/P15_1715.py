import heapq

n = int(input())
card_list = [int(input()) for _ in range(n)]
heapq.heapify(card_list)

cnt = 0
cards = 0
    
while len(card_list) > 1:
    a = heapq.heappop(card_list)
    b = heapq.heappop(card_list)
    cards = a + b
    cnt += cards
    heapq.heappush(card_list, cards)

print(cnt)





# 카드 정렬하기
# 정렬된 두 묶음의 숫자 카드 각 묶음의 카드의 수를 A, B
# 두 묶음을 합치기 위해서는 A+B 번의 비교가 필요하다
# N개의 묶음이 있을때 비교횟수 최소화

# 매번 제일 작은 2개 비교가 필요하다

# https://www.acmicpc.net/problem/1715