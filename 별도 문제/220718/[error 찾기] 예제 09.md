## 예제 09

> 아래 코드는 과일의 개수를 구하는 논리적 오류가 있는 코드의 일부분 입니다.
> 코드에서 오류를 찾아 원인을 적고, 수정하세요.

## 코드

```python
# 문제 코드
from pprint import pprint

fruits = [
    "Soursop",
    "Grapefruit",
    "Apricot",
    "Juniper berry",
    "Feijoa",
    "Blackcurrant",
    "Cantaloupe",
    "Salal berry",
]

fruit_count = {}

for fruit in fruits:
    if fruit not in fruit_count:
        fruit_count = {fruit: 1} # dictionary인 fruit_count의 키 값 설정을 해야한다.
    else:
        fruit_count[fruit] += 1

pprint(fruit_count)

# 수정

# ... 

for fruit in fruits:
    if fruit not in fruit_count:
        fruit_count[fruit] = 1 # dictionary인 fruit_count의 키 값을 1로 설정했다.
    else:
        fruit_count[fruit] += 1

pprint(fruit_count)

```

## 느낀점

<aside>
💡 새롭게 알게된 점, 어려웠던 점


</aside>
