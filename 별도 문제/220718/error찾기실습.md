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

## 예제 04

> 아래 코드는 문자열을 입력받아 단어별로 나누는 코드입니다.
코드에서 오류를 찾아 원인을 적고, 수정하세요.

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

## 예제 05

> 아래 코드는 숫자의 길이를 구하는 코드입니다.
코드에서 오류를 찾아 원인을 적고, 수정하세요.

## 코드

```python
# 문제 코드
number = 22020718
print(len(number)) # TypeError : number의 자료형인 int는 len함수의 argument가 될 수 없다.

# 수정
numbers = 22020718
print(len(str(number))) # int를 str로 바꿨다.
```

## 느낀점

<aside>
💡 새롭게 알게된 점, 어려웠던 점

</aside>

## 예제 06

> 아래 코드는 1부터 N까지의 숫자에 2를 곱해서 변수에 저장하는 코드입니다.
코드에서 오류를 찾아 원인을 적고, 수정하세요.
> 

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

## 예제 07

> 아래 코드는 평균을 구하는 논리적으로 오류가 있는 코드입니다. 
코드에서 오류를 찾아 원인을 적고, 수정하세요.
> 

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

## 예제 08

> 아래 코드는 문자열에서 모음의 개수를 찾는 코드입니다. 
코드에서 오류를 찾아 원인을 적고, 수정하세요.
> 

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

## 예제 09

> 아래 코드는 과일의 개수를 구하는 논리적 오류가 있는 코드의 일부분 입니다.
코드에서 오류를 찾아 원인을 적고, 수정하세요.
> 

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

## 예제 10

> 아래 코드는 리스트에서 최댓값을 구하는 코드입니다.
코드에서 오류를 찾아 원인을 적고, 수정하세요.
> 

## 코드

```python
# 문제 코드
number_list = [1, 23, 9, 6, 91, 59, 29]
max = max(number_list)

number_list2 = [2, 5, 100, 20, 50, 10, 91, 82]
max2 = max(number_list2)

if max > max2:
    print("첫 번째 리스트의 최댓값이 더 큽니다.")

elif max < max2:
    print("두 번째 리스트의 최댓값이 더 큽니다.")

else:
    print("첫 번째 리스트의 최댓값과 두 번째 리스트의 최댓값은 같습니다.")

# 수정

```

## 느낀점

<aside>
💡 새롭게 알게된 점, 어려웠던 점

</aside>

## 예제 11

> 아래 코드는 영화의 장르id를 장르 이름으로 바꿔서 영화 정보를 출력하는 코드입니다.
코드에서 오류를 찾아 원인을 적고, 수정하세요.
> 

## 코드

```python
# 문제 코드
from pprint import pprint

def movie_info(movie, genres):
    genres_names = []
    genre_ids = movie["genre_ids"]
    for genre_id in genre_ids:
        for genre in genres:
            if genre_id == genre["id"]:
                genre_name = genre["name"]
                genres_names.append(genre_name)

    new_movie_info = {
        "genre_names": genres_names,
        "id": movie["id"],
        "overview": movie["overview"],
        "title": movie["title"],
        "vote_average": movie["vote_average"],
    }

if __name__ == "__main__":
    movie = {
        "adult": False,
        "backdrop_path": "/tXHpvlr5F7gV5DwgS7M5HBrUi2C.jpg",
        "genre_ids": [18, 80],
        "id": 278,
        "original_language": "en",
        "original_title": "The Shawshank Redemption",
        "overview": "촉망받는 은행 간부 앤디 듀프레인은 아내와 그녀의 정부를 살해했다는 누명을 쓴다. 주변의 증언과 살해 현장의 그럴듯한 증거들로 그는 종신형을 선고받고 악질범들만 수용한다는 지옥같은 교도소 쇼생크로 향한다. 인간 말종 쓰레기들만 모인 그곳에서 그는 이루 말할 수 없는 억압과 짐승보다 못한 취급을 당한다. 그러던 어느 날, 간수의 세금을 면제받게 해 준 덕분에 그는 일약 교도소의 비공식 회계사로 일하게 된다. 그 와중에 교도소 소장은 죄수들을 이리저리 부리면서 검은 돈을 긁어 모으고 앤디는 이 돈을 세탁하여 불려주면서 그의 돈을 관리하는데...",
        "popularity": 67.931,
        "poster_path": "/3hO6DIGRBaJQj2NLEYBMwpcz88D.jpg",
        "release_date": "1995-01-28",
        "title": "쇼생크 탈출",
        "video": False,
        "vote_average": 8.7,
        "vote_count": 18040,
    }

    genres_list = [
        {"id": 28, "name": "Action"},
        {"id": 12, "name": "Adventure"},
        {"id": 16, "name": "Animation"},
        {"id": 35, "name": "Comedy"},
        {"id": 80, "name": "Crime"},
        {"id": 99, "name": "Documentary"},
        {"id": 18, "name": "Drama"},
        {"id": 10751, "name": "Family"},
        {"id": 14, "name": "Fantasy"},
        {"id": 36, "name": "History"},
        {"id": 27, "name": "Horror"},
        {"id": 10402, "name": "Music"},
        {"id": 9648, "name": "Mystery"},
        {"id": 10749, "name": "Romance"},
        {"id": 878, "name": "Science Fiction"},
        {"id": 10770, "name": "TV Movie"},
        {"id": 53, "name": "Thriller"},
        {"id": 10752, "name": "War"},
        {"id": 37, "name": "Western"},
    ]

    pprint(movie_info(movie, genres_list)) # 매개변수가 잘못됐다.

# 수정

from pprint import pprint

def movie_info(movie, genres):
    genres_names = []
    genre_ids = movie["genre_ids"]
    for genre_id in genre_ids:
        for genre in genres:
            if genre_id == genre["id"]:
                genre_name = genre["name"]
                genres_names.append(genre_name)

    new_movie_info = {
        "genre_names": genres_names,
        "id": movie["id"],
        "overview": movie["overview"],
        "title": movie["title"],
        "vote_average": movie["vote_average"],
    }

pprint(new_movie_info) # 해당 dictionary로 매개변수를 바꿨다.
```

## 느낀점

<aside>
💡 새롭게 알게된 점, 어려웠던 점

</aside>