# 우리가 알고 있는 연도로 몇 년인지 구하는 프로그램을 작성하시오.
# 브루트포스 # 정수론
import sys
sys.stdin = open("1476.txt")
input = sys.stdin.readline

E, S, M = map(int, input().split())
# 15를 넘으면 E가 1이 된다.
# 28을 넘으면 S가 1이 된다.
# 19을 넘으면 M이 1이 된다.
if Y > 15:
    E = 1
if Y > 28:
    S = 1
if Y > 19:
    M = 1
print(E, S, M)
