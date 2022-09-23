# 각 계단에 쓰여 있는 점수가 주어질 때 이 게임에서 얻을 수 있는 총 점수의 최댓값을 구하는 프로그램을 작성하시오.
# DP

import sys
sys.stdin = open('2579.txt')

# 계단의 개수는 300이하이다.
input = sys.stdin.readline
stair = [0]*300
n = int(input())

score = [0]*300  # 점수
for i in range(n):
    score[i] = int(input())

# stair[마지막 밟는 계단]
stair[0] = score[0]
stair[1] = score[0]+score[1]
stair[2] = max(score[0], score[1]) + score[2]


for i in range(3, n):
    stair[i] = max(stair[i-3]+score[i-1], stair[i-2])+score[i]
print(stair[n-1])

# 1 1
# 2 1 2
# 3 (1,2) 3
# 4 #1+3+4 #2+4
# 5 #2+4+5 #3+5
# 6 #3+5+6 #4+6
# 6 1,2,4, 2,3, 2,4, 1,3,5 6
