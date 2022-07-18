## 예제 03

> 두 수를 Input으로 받아 합을 구하는 코드이다.
코드에서 오류를 찾아 원인을 적고, 수정하세요

## 코드

```python
# 문제 코드
numbers = input().split()
print(sum(numbers)) # 원인 : TypeError. sum함수의 argument는 int이어야 한다.

# 수정
numbers = map(int,input().split() # input을 int로 매핑했다.
print(sum(numbers))
```

## 느낀점

<aside>
💡 새롭게 알게된 점, 어려웠던 점
</aside>