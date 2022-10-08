# 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
# 부르트포스 # 백트래킹

import sys

sys.stdin = open("15649.txt")

# 백트래킹 : 아닌 거 같으면 돌아간다.
N, M = map(int, input().split())
l = []
visited = [False] * (N + 1)

# 1부터 N까지 자연수 중에서
def collect(N, M):
    for i in range(1, N + 1):
        # M개를 고른다.
        l.append(i)
        visited[i - 1] = True  # 중복없이
        if len(l) == M:
            print(l)
            l.pop()


collect(N, M)
# 5 3
# 1 2 3
# 1 2 4
# 1 2 5
# 2 3 4
# 2 3 5
# 3 4 5
