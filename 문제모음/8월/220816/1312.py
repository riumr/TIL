# A÷B를 했을 때, 소숫점 아래 N번째 수를 출력한다.

import sys
sys.stdin = open("1312.txt")
input = sys.stdin.readline

A, B, N = map(int, input().split())

# 첫째 자리 수
answer = A/B
