# 변환의 과정을 몇 번 거쳐야 Y가 한 자리 수가 되는지 구하라. Y가 3의 배수이면 YES를 출력한다.
# 수학 # 구현 # 문자열 # 재귀

import sys
sys.stdin = open("1769.txt")
input = sys.stdin.readline

X = int(input())
# 변환과정
# 모든 자리 수를 더한다
