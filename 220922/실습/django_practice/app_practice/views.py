from django.shortcuts import render
import random
from collections import Counter

# Create your views here.
# index 함수를 선언하고 정의


def index(request):  # 요청을 argument로 받는다.
    return render(request, 'index.html')


def template(request):
    context = {'text': 'hello world'}
    return render(request, 'template.html', context)


def todaydinner(request):
    foods = ['짜장', '짬뽕', '피자', '치킨', '해물탕', '전골']
    food_images = [
        'https://cdn.pixabay.com/photo/2021/02/11/02/00/chapaguri-6004034_1280.jpg',
        'https://cdn.pixabay.com/photo/2018/12/03/01/04/spicy-seafood-3852529_1280.jpg',
        'https://cdn.pixabay.com/photo/2020/06/08/16/49/pizza-5275191_1280.jpg',
        'https://cdn.pixabay.com/photo/2015/03/11/00/31/chicken-667935_1280.jpg',
        'https://cdn.pixabay.com/photo/2018/04/26/08/37/food-3351373_1280.jpg',
        'https://cdn.pixabay.com/photo/2016/03/14/07/05/menu-5-wh-cs-division-1255020_1280.jpg'
    ]
    random_food = random.choice(foods)
    if random_food == '짜장':
        random_image = food_images[0]
    elif random_food == '짬뽕':
        random_image = food_images[1]
    elif random_food == '피자':
        random_image = food_images[2]
    elif random_food == '치킨':
        random_image = food_images[3]
    elif random_food == '해물탕':
        random_image = food_images[4]
    elif random_food == '전골':
        random_image = food_images[5]
    context = {'menu': random_food,
               'menu_image': random_image}
    return render(request, 'today-dinner.html', context)


def lotto(request):
    collect_numbers = [3, 11, 15, 29, 35, 44, 10]
    five_number_list = []
    for i in range(5):
        number_list = random.sample(range(1, 45), 6)
        five_number_list.append(number_list)
    context = {'number': five_number_list}
    return render(request, 'lotto.html', context)
