## 예제 10

> 아래 코드는 리스트에서 최댓값을 구하는 코드입니다.
> 코드에서 오류를 찾아 원인을 적고, 수정하세요.

## 코드

```python
# 문제 코드
number_list = [1, 23, 9, 6, 91, 59, 29]
max = max(number_list) # 변수이름이 함수이름과 같으면 안 된다.

number_list2 = [2, 5, 100, 20, 50, 10, 91, 82]
max2 = max(number_list2)

if max > max2:
    print("첫 번째 리스트의 최댓값이 더 큽니다.")

elif max < max2:
    print("두 번째 리스트의 최댓값이 더 큽니다.")

else:
    print("첫 번째 리스트의 최댓값과 두 번째 리스트의 최댓값은 같습니다.")

# 수정
number_list = [1, 23, 9, 6, 91, 59, 29]
max1 = max(number_list) # 변수이름을 변경했다.

number_list2 = [2, 5, 100, 20, 50, 10, 91, 82]
max2 = max(number_list2)

if max1 > max2:
    print("첫 번째 리스트의 최댓값이 더 큽니다.")

elif max1 < max2:
    print("두 번째 리스트의 최댓값이 더 큽니다.")

else:
    print("첫 번째 리스트의 최댓값과 두 번째 리스트의 최댓값은 같습니다.")
```

## 느낀점

<aside>
💡 새롭게 알게된 점, 어려웠던 점


</aside>
