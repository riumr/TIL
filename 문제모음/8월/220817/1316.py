# 그룹 단어의 개수를 출력한다.
# 구현
import sys
sys.stdin = open("1316.txt")

input = sys.stdin.readline
counts = 0
N = int(input())
answer = True
for i in range(N):
    check_l = []
    s = input()
    check_l.append(s[0])
    for j in range(1, len(s)):
        # 저장리스트에 없으면 저장
        if s[j] not in check_l:
            check_l.append(s[j])
            answer = True
        # 저장리스트에 있으면
        else:
            # 연속하지 않으면
            if s[j-1] != s[j]:
                answer = False
                break
            else:
                answer = True
    if answer == True:
        counts += 1
print(counts)
