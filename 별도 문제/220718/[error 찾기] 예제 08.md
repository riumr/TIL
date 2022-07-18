## 예제 08

> 아래 코드는 문자열에서 모음의 개수를 찾는 코드입니다. 
> 코드에서 오류를 찾아 원인을 적고, 수정하세요.

## 코드

```python
# 문제 코드
word = "HappyHacking"

count = 0

for char in word:
    if char == "a" or "e" or "i" or "o" or "u": # if 조건문은 개별적 적용해야 한다.
        count += 1

print(count)

# 수정
word = "HappyHacking"

count = 0

for char in word:
    if char == "a" or 
		if char == "e" or
		if char == "i" or 
		if char == "o" or 
		if char == "u": # 각각 조건문을 적용했다.
        count += 1

print(count)
```

## 느낀점

<aside>
💡 새롭게 알게된 점, 어려웠던 점


</aside>
