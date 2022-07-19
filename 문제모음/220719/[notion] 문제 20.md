## 문제 20

> 정수 number가 주어질 때, 각 자릿수의 합을 구해서 출력하세요. 

## 접근 방법

정수 number를 list로 만들고, 다시 정수로 매핑한 후, sum함수로 합을 구한다.

## 코드

```python
number_list = list(number)
number_list_sum - sum(map(int,number_list))
print(number_list_sum)
```

## 느낀점

<aside> 💡 새롭게 알게된 점, 어려웠던 점

</aside>