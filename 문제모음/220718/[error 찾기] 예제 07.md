## 예제 07

> 아래 코드는 평균을 구하는 논리적으로 오류가 있는 코드입니다. 
> 코드에서 오류를 찾아 원인을 적고, 수정하세요.

## 코드

```python
# 문제 코드
number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

total = 0
count = 0

for number in number_list:
    total += number
count += 1 # 들여쓰기를 하지않아 loop에서 벗어났다.

print(total // count) # 부호가 잘못됐다.

# 수정
number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

total = 0
count = 0

for number in number_list:
    total += number
		count += 1 # 들여쓰기를 했다.

print(total / count) # //에서 /로 부호를 바꿨다.

```

## 느낀점

<aside>
💡 새롭게 알게된 점, 어려웠던 점


</aside>
