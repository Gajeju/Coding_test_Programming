y, x = map(int, input().split())
chess = [list(input()) for _ in range(y)]

cnts = []

for i in range(y-7):
    for j in range(x-7):
        start = chess[i][j]
        cnt = 0
        for k in range(i,i+8):
            for l in range(j,j+8):
                if (k+l-i-j) % 2 == 0 and start != chess[k][l]:
                    cnt += 1
                elif (k+l-i-j) % 2 == 1 and start == chess[k][l]:
                    cnt += 1
        if cnt > 32:
            cnt = 64 - cnt
        cnts.append(cnt)

print(min(cnts))



# M * N 단위 정사각형으로 이루어져 있는 보드
# 어떤건 검은색 나머지는 흰색
# 잘라서 8 * 8 체스판으로 만들기
# 다시 칠해야 하는 최소 개수

# https://www.acmicpc.net/problem/1018