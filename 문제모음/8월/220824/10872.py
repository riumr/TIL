# 0보다 크거나 같은 정수 N이 주어진다. 이때, N!을 출력하는 프로그램을 작성하시오.
# 구현 # 조합론 # 재귀

import sys
sys.stdin = open("10872.txt")
input = sys.stdin.readline

# N! = N*N-1...1
N = int(input())
n = 1
for i in range(N, 1, -1):
    n *= i
print(n)
