# 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
# 부르트포스 # 백트래킹

import sys

sys.stdin = open("15649.txt")

# 백트래킹 : 아닌 거 같으면 돌아간다.
N, M = map(int, input().split())
l = []


def collect():
    # 길이가 M이면 값을 반환해야한다.
    if len(l) == M:
        print(" ".join(map(str, l)))
    # 1부터 N까지 값을 넣어본다.
    for i in range(1, N + 1):
        if i not in l:
            l.append(i)
            collect()
            # 넣을 값이 없으면 pop을 실행할 수 있다.
            # 중간에 넣기를 멈췄던 값이 있으면 다시 넣는다.
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
# 1
# 2
# 3 print
# 4
# 5
# -5
# -4
#
