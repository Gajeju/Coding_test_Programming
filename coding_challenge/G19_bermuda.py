# N차원 공간의 버뮤다 삼각형이 되려면 세 각의 합이 180도가 되어야 합니다.
# 또한, 하나의 각이라도 0도가 되거나 180도가 되면 불가능합니다.
# 세 각의 크기가 주어질 때, 버뮤다 삼각형이 될 수 있는지 없는지 판단하는 프로그램을 만드세요.
import sys

angle_list = list(map(int, sys.stdin.readline().split()))

if sum(angle_list) == 180 and (0 not in angle_list and 180 not in angle_list):
    print('P')
else:
    print('F')