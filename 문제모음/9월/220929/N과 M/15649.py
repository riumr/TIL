# 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
# 부르트포스 # 백트래킹

import sys
sys.stdin = open('15649.txt')

# 백트래킹 : 아닌 거 같으면 돌아간다.
N, M = map(int, input().split())

# 값을 다른 리스트에 저장해놓고, 있으면 다음 수로 넘어가기

# 1부터 N까지 자연수의 수열을 만든다
l = []
for i in range(1, N+1):
    l.append(i)

# 값을 다른 리스트에 저장하면서 이쪽 리스트에서도 출력한다

for i in range(N):
    for j in range(1, N):
        for k in range(2, N):
            print(l[i], l[j], l[k])
# l[0], l[1], l[2]
# l[0], l[1], l[3]
# 5 3
# 1 2 3
# 1 2 4
# 1 2 5
# 2 3 4
# 2 3 5
# 3 4 5


if len(l) % M == 0:
    print(l)
    i += 1

# 1
# 2
# 3 4 5
