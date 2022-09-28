# 가장 긴 증가하는 부분 수열
# DP

# 수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열의 길이를 구하는 프로그램을 작성하시오.
# 예를 들어, 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에 가장 긴 증가하는 부분 수열은 A = {10, 20, 30, 50} 이고, 길이는 4이다.
# 첫째 줄에 수열의 크기 N, 둘째 줄에 수열이 주어진다.

import sys

sys.stdin = open("11053.txt")

N = int(input())
A = list(map(int, input().split()))

# 가장 긴 증가하는 부분 수열 : 리스트에서 수가 증가하는 가장 긴 조합

# max함수 활용
l = [1]*N
for i in range(1, N):
    for j in range(i):
        if A[i] > A[j]:
            l[i] = max(l[i], l[j]+1)
print(max(l))
