## 예제 04

> 아래 코드는 문자열을 입력받아 단어별로 나누는 코드입니다.
> 코드에서 오류를 찾아 원인을 적고, 수정하세요.

### Input

```
I'm Tuotur 6
```

### Output

```
["I'm", 'Tutor', '6']
```

## 코드

```python
# 문제 코드
words = list(map(int, input().split())) # valueError : 입력값은 int가 아니라 str이다.
print(words)

# 수정
words = list(input().split()) # int로 매핑하지 않았다.
print(words)
```

## 느낀점

<aside>
💡 새롭게 알게된 점, 어려웠던 점


</aside>