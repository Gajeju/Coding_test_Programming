# 재귀 함수의 종료조건

def recursive_funcction(i):
    # 100번째 출력했을 때 종료되도록 조건 명시
    if i == 100:
        return
    print(i, '번째 재귀 함수에서', i + 1, '번째 재귀 함수를 호출합니다.')
    recursive_funcction(i+1)

recursive_funcction(1)
