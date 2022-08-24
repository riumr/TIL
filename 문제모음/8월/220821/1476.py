# 우리가 알고 있는 연도로 몇 년인지 구하는 프로그램을 작성하시오.
# 브루트포스 # 정수론
import sys
sys.stdin = open("1476.txt")
input = sys.stdin.readline

E, S, M = map(int, input().split())
# 15를 넘으면 E가 1이 된다.
# 28을 넘으면 S가 1이 된다.
# 19을 넘으면 M이 1이 된다.
# 모든 수가 1씩 증가한다.
e = 1
s = 1
m = 1
Y = 1
while True:
    if e == E and s == S and m == M:
        break
    Y += 1
    e += 1
    s += 1
    m += 1
    if e > 15:
        e = 1
    if s > 28:
        s = 1
    if m > 19:
        m = 1
print(Y)
