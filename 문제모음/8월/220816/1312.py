# A÷B를 했을 때, 소숫점 아래 N번째 수를 출력한다.
# 연산, 조건의 최소화

import sys
sys.stdin = open("1312.txt")
input = sys.stdin.readline

A, B, N = map(int, input().split())

for i in range(N):
    A %= B
    A *= 10
    answer = int(A/B)
print(answer)
