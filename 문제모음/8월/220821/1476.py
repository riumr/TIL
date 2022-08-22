# 우리가 알고 있는 연도로 몇 년인지 구하는 프로그램을 작성하시오.
# 브루트포스
import sys
sys.stdin = open("1476.txt")
input = sys.stdin.readline

E, S, M = map(int, input().split())
Y = E*15+S*28+M*19
print(Y)
