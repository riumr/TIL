# 그룹 단어의 개수를 출력한다.
# 구현
import sys
sys.stdin = open("1316.txt")

s = input()
check_dict = {}
# 그룹단어 : 각 문자가 연속해서 나온다.
# 조건 : 문자가 연속해서 나온다.
for i in range(len(s)):
    if s[i-1] == s[i]:
        s[i-1] = "checked"
# 조건 : 연속하지 않으면 다른 문자로 넘어간다.
    else:

print(answer)
