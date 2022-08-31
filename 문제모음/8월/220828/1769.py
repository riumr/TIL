# 변환의 과정을 몇 번 거쳐야 Y가 한 자리 수가 되는지 구하라. Y가 3의 배수이면 YES를 출력한다.
# 수학 # 구현 # 문자열 # 재귀

import sys
sys.stdin = open("1769.txt")


def circle(S, C):
    S = str(S)
    if len(S) > 1:
        C += 1
        Y = 0
        for i in S:
            Y += int(i)
        circle(str(Y), C)
    else:
        print(C, "\nYES") if int(S) % 3 == 0 else print(C, "\nNO")


if __name__ == '__main__':
    X = input()
    step = 0
    circle(X, step)
