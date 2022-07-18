## 예제 06

> 아래 코드는 1부터 N까지의 숫자에 2를 곱해서 변수에 저장하는 코드입니다.
> 코드에서 오류를 찾아 원인을 적고, 수정하세요.

## 코드

```python
# 문제 코드
N = 10
answer = () # append함수는 list의 함수이다.
for number in range(N + 1): # 범위설정이 잘못됐다.
    answer.append(number * 2)

print(answer)

# 수정
N = 10
answer = []
	for number in range(1, N+1): # 범위를 1부터 N+1로 수정했다.
	answer.append(number * 2)

print(answer)
```

## 느낀점

<aside>
💡 새롭게 알게된 점, 어려웠던 점


</aside>
