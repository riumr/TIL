# 변환의 과정을 몇 번 거쳐야 Y가 한 자리 수가 되는지 구하라. Y가 3의 배수이면 YES를 출력한다.
# 수학 # 구현 # 문자열 # 재귀

# 변환과정 : 각 자리 수를 모두 더한다.
import sys
sys.stdin = open("1769.txt")
input = sys.stdin.readline

X = int(input())
# 자리 수의 길이
# 자리 수가 한 자리가 될 때까지 반복
len_X = len(str(X))
step = 0
# def one_N(X):
#     if len_X == 1:
#         Y = 0
#     for i in range(len_X-1, -1, -1):
#        Y += (X//10**i)
#        X %= 10**i
#     step += 1
#     X = Y
#     len_X = len(str(X))


def one_N(X):


print(X, "\nYES") if Y % 3 == 0 else print(X, "\nNO")
