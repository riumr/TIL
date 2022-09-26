from django.shortcuts import render
import random

# Create your views here.
def oddeven(request, number):
    if number % 2 == 0:
        check = "짝수"
    else:
        check = "홀수"
    context = {"number": number, "check": check}
    return render(request, "oddeven.html", context)


def caculate(request, num1, num2):
    plus_result = num1 + num2
    minus_result = num1 - num2
    cross_result = num1 * num2
    divide_result = num1 // num2
    context = {
        "num1": num1,
        "num2": num2,
        "plus_result": plus_result,
        "minus_result": minus_result,
        "cross_result": cross_result,
        "divide_result": divide_result,
    }
    return render(request, "caculate.html", context)


def randompast(request):
    pasts = ["왕", "귀족", "평민", "노비", "돌", "동물", "식물", "괴물"]
    result = random.choice(pasts)
    context = {
        "result": result,
    }
    return render(request, "caculate.html", context)
