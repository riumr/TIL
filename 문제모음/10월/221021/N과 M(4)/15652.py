# 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

# 1부터 N까지 자연수 중에서 M개를 고른 수열
# 같은 수를 여러 번 골라도 된다.
# 고른 수열은 비내림차순이어야 한다. = 오름차순이어야한다.
# 길이가 K인 수열 A가 A1 ≤ A2 ≤ ... ≤ AK-1 ≤ AK를 만족하면, 비내림차순이라고 한다.

import sys

sys.stdin = open("15652.txt")


N, M = map(int, input().split())


l = []

# 다음 수가 이전 수보다 작지 않다.
def dfs(s):
    if len(l) == M:
        print(" ".join(map(str, l)))
        return
    for i in range(s, N + 1):
        l.append(i)
        dfs(i)
        l.pop()


dfs(1)
