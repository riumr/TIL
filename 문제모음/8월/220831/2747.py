# n이 주어졌을 때, n번째 피보나치 수를 구하는 프로그램을 작성하시오.
# 수학 # 구현 # 재귀로 가능

# 피보나치 수 : Fn = Fn-1 + Fn-2 (n ≥ 2)
# 이전의 두 수를 더한다.
# c = a+b

import sys
sys.stdin = open("2747.txt")


def fibo(number, step):
    if step < n:
        step += 1
        result += number
        fibo(result, step)
    else:
        print(result)


if __name__ == '__main__':
    step = 0
    number = 1
    result = 0
    n = int(input())
    fibo(number, step)
