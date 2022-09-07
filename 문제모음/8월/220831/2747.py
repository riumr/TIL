# n이 주어졌을 때, n번째 피보나치 수를 구하는 프로그램을 작성하시오.
# 수학 # 구현 # 재귀로 가능

# 피보나치 수 : Fn = Fn-1 + Fn-2 (n ≥ 2)
# 이전의 두 수를 더한다.
# c = a+b
# 1 1 2 3

import sys
sys.stdin = open("2747.txt")

# # n이 주어졌을 때
# n = int(input())

# f0 = 0
# # 첫번째 수
# f1 = 1
# step = 1
# # 두번째 수 result = f0+f1
# # 다음으로 더할 수
# # f0 = f1
# # f1 = result
# # 계산할 때마다 1에서 1씩 증가 : step = 1 미리 선언
# # 반복할 계산
# while step < n:
#     step += 1
#     result = f0+f1
#     # 다음으로 더할 수
#     f0 = f1
#     f1 = result
# if step == 1:
#     result = 1
# print(result)

# 재귀로 구현


def fibo(f0, f1, step):
    if step < n:
        step += 1
        result = f0 + f1
        fibo(f1, result, step)
    else:
        print(step, f1)

# a = 0
# b = 1
# s = 1


n = int(input())
fibo(0, 1, 1)
