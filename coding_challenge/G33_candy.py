# 원형으로 길게 생긴 사탕 케이스 안에는 1번부터 순차적으로 번호가 적힌 사탕들이 들어가 있습니다.
# 케이스의 폭은 사탕 하나의 크기와 같아서 안에 있는 사탕을 꺼내려면 원형으로 길게 생긴 사탕 케이스를 왼쪽 혹은 오른쪽으로 회전시키면서 사탕을 꺼내야 합니다.
# 또한 사탕을 꺼낼 때에는 케이스에서 오직 첫 번째 위치의 사탕만을 꺼낼 수 있습니다.
# 예를 들어 케이스 안에 각각 1 2 3 4 5번의 사탕이 있는 경우, 이 때 3번 사탕을 꺼낼 수 있는 방법은 다음과 같은 경우들을 예시로 들 수 있을 것입니다.
# 1. 사탕들을 우회전 시켜서 5번 사탕을 왼쪽 끝으로 가도록 보내고,
# 한 번 더 우회전 시켜서 이번에는 4번 사탕이 왼쪽 끝으로 가도록 보내고,
# 마지막으로 한 번 더 우회전 시켜서 비로소 3번 사탕이 왼쪽 끝에 도달할 수 있도록 하여 꺼냅니다.
# 2. 위 예시와는 반대로 두 번의 좌회선 이후에 3번 사탕을 꺼냅니다.
# 위 두 가지 예시는 모두 3번 사탕을 꺼내도록 해주지만, 첫 번째 예시는 3번의 회전이 필요하며 두 번째 예시는 2번의 회전이 필요하다는 차이가 있씁니다.
# 양 쪽 입구에서 사탕을 꺼낼 수 있는 사탕 케이스가 있고,
# 1번부터 N번까지 차례대로 들어가 있는 형태의 사탕의 개수 N과,
# 꺼내고자 하는 사탕의 개수와 번호가 주어졌을 때 좌회전 혹은 우회전을 사용하여 사탕의 위치를 최소 몇 번 회전시켜야 원하는 사탕들을 꺼낼 수 있는지 알아내세요.
# 첫 번째 위치의 사탕을 꺼내는 과정 자체는 개수에 포함하지 않습니다.
# 예를 들어 사탕의 개수가 5개고,
# 꺼내고자 하는 사탕이 차례대로 1번, 3번, 4번이라면 초기 상태인 (1, 2, 3, 4, 5)의 사탕 케이스에서 (사탕 뽑기) - (좌회전) - (사탕 뽑기) - (사탕 뽑기)로 원하는 사탕을 모두 뽑아낼 수 있으므로
# 한 번의 회전만이 필요한 것입니다.
import sys
from collections import deque

def spin_left(de, num):
    cnt = False
    while de[0] != num:
        de.append(de.popleft())
        cnt = True
    return 1 if cnt else 0
    
def spin_right(de, num):
    cnt = False
    while de[0] != num:
        de.appendleft(de.pop())
        cnt = True
    return 1 if cnt else 0

candy_num, output_num = map( int, sys.stdin.readline().split() )
output_list = list(map(int, sys.stdin.readline().split()))
cnt = 0
left = True

de = deque()
for i in range(1,candy_num+1):
    de.append(i)

for output in output_list:
    if de.index(output) >= len(de)//2:
        cnt += spin_right(de, output)
        de.popleft()
    else:
        cnt += spin_left(de, output)
        de.popleft()

print(cnt)
    


