# N의 사이클의 길이를 구하는 프로그램을 작성하시오.
# 구현
import sys
sys.stdin = open("1110.txt")

N = int(input())
second_N = N
circle = 0
while True:
    circle+=1
    if second_N<10:
        # 새로운 수
        new_N = 11*second_N
    else:
        # 새로운 수의 십의 자리 수 : 이전 수의 일의 자리 수
        first_num = second_N%10
        # 새로운 수의 일의 자리 수 : 이전 수의 자리 수의 합의 일의 자리 수
        second_num = (second_N//10+first_num)%10
        # 새로운 수
        new_N = 10*first_num+second_num
    second_N = new_N
    if new_N==N:
        break
print(circle)