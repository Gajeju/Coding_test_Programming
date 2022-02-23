def star(n, li):
    out = []
    if n == 3:
        return li
    else:
        for i in li:
            out.append(i * 3)
        for i in li:
            out.append(i + " " * len(li) + i)
        for i in li:
            out.append(i * 3)
        return star(n // 3, out)

if __name__ == "__main__":
    n = int(input())
    first = ['***', '* *', '***']
    final = star(n, first)
    for i in final:
        print(i)


# 재귀적인 패턴으로 별찍기
# n은 3의 거듭재곱이며
# https://www.acmicpc.net/problem/2447