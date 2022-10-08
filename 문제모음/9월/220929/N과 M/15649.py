# 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
# 부르트포스 # 백트래킹

import sys

sys.stdin = open("15649.txt")

# 백트래킹 : 아닌 거 같으면 돌아간다.
N, M = map(int, input().split())
l = []
# 1. 길이가 M이면 출력한다.
def collect():
    if len(l) == M:
        print(" ".join(map(str, l)))
    # 2. 1에서 N까지 추가하도록 한다.
    for i in range(1, N + 1):
        if i not in l:
            l.append(i)
            # 3. # 1 # 2를 반복한다. 반복문과 재귀 중 재귀가 더 간결할 거 같다.
            collect()
            l.pop()


collect()
# 5 3
# 1 2 3
# 1 2 4
# 1 2 5
# 1 3 4
# 1 3 5
# . . .

# 진행
