# 죄수들의 탈옥이 빈번한 교도소에 새로운 소장이 부임하였습니다.
# 소장은 죄수들이 서로 탈옥 모의를 시도하지 않도록 하기 위해 구역을 둘로 나누려고 합니다.
# 죄수들끼리 서로 볼 수 있는 경우의 정보가 주어지고,
# 같은 구역에 있는 죄수들은 서로 볼 수 없도록 하는 프로그램을 만드세요.
import sys

num, info_num = map(int, sys.stdin.readline().split())
info_list = [list(map(int, sys.stdin.readline().split())) for _ in range(info_num)]

group_a = []
group_b = []

for info in info_list:
    if info[0] in group_a:
        if info[1] in group_a:
            print(0)
            break
        else:
            group_b.append(info[1])
    else:
        group_a.append(info[0])
        group_b.append(info[1])
else:
    print(1)