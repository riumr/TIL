# 프로그래머스

# Finn은 요즘 수학공부에 빠져 있습니다. 수학 공부를 하던 Finn은 자연수 n을 연속한 자연수들로 표현 하는 방법이 여러개라는 사실을 알게 되었습니다.
# 예를들어 15는 다음과 같이 4가지로 표현 할 수 있습니다.
# 1 + 2 + 3 + 4 + 5 = 15
# 4 + 5 + 6 = 15
# 7 + 8 = 15
# 15 = 15
# 자연수 n이 매개변수로 주어질 때, 연속된 자연수들로 n을 표현하는 방법의 수를 return하는 solution를 완성해주세요.

import sys

sys.stdin = open("숫자의표현.txt")

n = int(input())


def solution(n):
    answer = 0
    for i in range(1, n + 1):  # 시작할 수를 점차 큰 수로 넣어준다.
        sum_ = 0
        for j in range(i, n + 1):  # i부터 n까지 더해준다.
            sum_ += j
            if sum_ == n:
                answer += 1
                break  # 조건을 충족하면 진행 중인 for문을 멈춘다.
            elif sum_ > n:
                break  # 같지 않으면 더하지 않고 멈춘다.
    return answer


print(solution(n))


# 다른풀이
# def expressions(num):
#     return len([i for i in range(1,num+1,2) if num % i is 0])
