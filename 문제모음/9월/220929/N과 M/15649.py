# 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
# 부르트포스 # 백트래킹

import sys

sys.stdin = open("15649.txt")

# 백트래킹 : 아닌 거 같으면 돌아간다.
N, M = map(int, input().split())
l = []
visited = [False] * (N + 1)

# 값을 다른 리스트에 저장해놓고, 있으면 다음 수로 넘어가기

# 1부터 N까지 자연수의 수열을 만든다
for i in range(1, N + 1):
    # 판단 리스트가 false면 true로 바꾸고, true면 계속 진행한다.
    if visited[i] == False:
        visited[i] = True
        l.append(i)
        if len(l) == M:
            print(l)
            l.pop()
    else:
        continue
    # 리스트 길이가 M이면 출력한다


# l[0], l[1], l[2]
# l[0], l[1], l[3]
# 5 3
# 1 2 3
# 1 2 4
# 1 2 5
# 2 3 4
# 2 3 5
# 3 4 5


# 1
# 2
# 3 4 5
