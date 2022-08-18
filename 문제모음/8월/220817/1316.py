# 그룹 단어의 개수를 출력한다.
# 구현
import sys
sys.stdin = open("1316.txt")

counts = 0
N = int(input())
for i in range(N):
    s = input()
    checks = []
    answer = True
    # 그룹단어 : 각 문자가 연속해서 나온다.

    # 문자가 연속되면 저장한다.
    i = 1
    while i < len(s):
        if s[i-1] == s[i]:  # 0,1 1,2 2,3
            save_s = s[i-1]
            checks.append(save_s)
            i += 1
    # 문자가 연속되지 않으면 다른 문자로 건너간다.
        else:
            save_s = s[i]
            # 그 문자가 기존에 있었는지 확인한다.
            if save_s in checks:
                answer = False
            i += 1
    if answer == True:
        counts += 1
print(counts)
