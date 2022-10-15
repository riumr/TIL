# 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
# 고른 수열은 오름차순이어야 한다.

import sys

sys.stdin = open("15650.txt")

N, M = map(int, input().split())

l = []
# M개를 고른다.
def backtracking():
    if len(l) == M and l == sorted(l):
        print(l)
    # 오름차순이다. ->
    for i in range(1, N + 1):
        if i not in l:
            l.append(i)
            backtracking()
            l.pop()


backtracking()
