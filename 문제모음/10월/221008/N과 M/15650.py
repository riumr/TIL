# 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
# 고른 수열은 오름차순이어야 한다.

N, M = map(int, input().split())

# M개를 고른다.
if len(l) == M:
    print(l)
# 오름차순이다. -> 기본적으로 오름차순이라서 추가 조건이 필요 없다.
