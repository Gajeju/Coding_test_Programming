self_list = [True] * 100000

for i in range(10001):
    d_i = i + (i // 10000) + (i % 10000 // 1000) + (i % 1000 // 100) + (i % 100 // 10) + (i % 10)
    self_list[d_i] = False

for i in range(1, 10001):
    if self_list[i] == True:
        print(i)



# 셀프넘버 d(n) = n + 각 자리수
# n 을 d(n) 의 성성자라고 하며 생성자가 없는 수를 셀프넘버 라고 한다
# 10000 보다 작은 셀프넘버 출력
# 브루트포스

# https://www.acmicpc.net/problem/4673