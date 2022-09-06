# n이 주어졌을 때, n번째 피보나치 수를 구하는 프로그램을 작성하시오.
# 수학 # 구현 # 재귀로 가능

# 피보나치 수 : Fn = Fn-1 + Fn-2 (n ≥ 2)
# 이전의 두 수를 더한다.
# c = a+b

import sys
sys.stdin = open("2747.txt")

# 이전 첫번째 수는 1
before01 = 1
# 이전 두번째 수는
before02 = 1
# 단계는 0부터 시작
step = 0
n = int(input())
# 단계가 n보다 작으면
while step < n:
    # result의 시작은 0
    result = 0
    # 이전의 수를 더한다
    result = before01+before02
    # 다음에 더할 수는 result이다
    before01 = result
    before02 = before01
    step += 1
print(result)

# 재귀로 구현
# 반복할 argument는 before과 step이다.


# def fibo(before, result, step):
#     # 단계가 n보다 작으면
#     if step < n:
#         result += before
#         before = result
#         step += 1
#         fibo(result, result, step)
#     # 결과출력
#     else:
#         print(result, step)


# if __name__ == '__main__':
#     b = 1
#     r = 1
#     s = 0
#     n = int(input())
#     fibo(b, r, s)
