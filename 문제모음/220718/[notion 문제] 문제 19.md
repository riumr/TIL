## 문제 19

> 양의 정수 number가 주어질 때, 숫자의 길이를 구하시오. 
> **양의 정수 number를 문자열로 변경하는 것은 금지입니다. str() 사용 금지**

## 접근 방법

numbers를 10의 i제곱으로 나눈다.

한번 나눌 때마다 변수에 1을 더한다.

## 코드

```python
i=0
n_len = 0
while numbers>0:
	i+=1
	10square = numbers / 10**i
	n_len+=1
	if numbers/10square < 1:
		break
print(n_len)
```

## 느낀점

<aside>
💡 새롭게 알게된 점, 어려웠던 점


