# 현지는 프로그래밍을 좋아하지만 잘 하지는 못합니다.
# 현지는 최근에 반복문에 대해서 공부하고 있습니다.
# 반복문을 공부할 때는 삼각형을 출력해보는 것이 매우 효과적이라는 소리를 듣고 따라서 공부하고 있습니다.
# 따라서 공부에 어려움을 겪고 있는 현지를 위해서 정수 N이 입력되었을 때 크기가 N인 삼각형 피라미드를 출력하는 프로그램을 대신 작성해주고자 합니다.
# 예를 들어 N이 3일 때 삼각형 피라미드는 다음과 같습니다. * ** *** 또한 N이 5일 때 삼각형 피라미드는 다음과 같습니다. * ** *** **** *****

import sys
input = lambda : int(sys.stdin.readline().strip())

n = input()
for i in range(n):
    print('*' * (i+1))