# 아버지의 키와 어머니의 키를 알면 이들의 2세의 키를 대강 예측할 수 있는 방법이 있습니다.
# 두 명의 키의 평균을 구하는 것입니다. 두 사람의 키가 자연수로 주어질 때 2세의 예상 키를 출력하는 프로그램을 만드세요.
import sys

a = list(map(int, sys.stdin.readline().split()))
print(int(sum(a) / len(a)))