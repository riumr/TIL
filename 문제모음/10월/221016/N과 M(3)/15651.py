# 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

# 1부터 N까지 자연수 중에서 M개를 고른 수열
# 같은 수를 여러 번 골라도 된다.

import sys

sys.stdin = open("15651.txt")

N, M = map(int, input().split())


l = []


def overlapped():
    if len(l) == M:
        print(" ".join(map(str, l)))
        return  # 재귀오류가 발생하다가 return을 추가하니까 해결됐다.
        # 같은 수를 여러번 골라도 된다.
    for i in range(1, N + 1):
        l.append(i)
        overlapped()
        l.pop()


overlapped()
