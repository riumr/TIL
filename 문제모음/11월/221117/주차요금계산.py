# 주차 요금을 나타내는 정수 배열 fees, 자동차의 입/출차 내역을 나타내는 문자열 배열 records가 매개변수로 주어집니다.
# 차량 번호가 작은 자동차부터 청구할 주차 요금을 차례대로 정수 배열에 담아서 return 하도록 solution 함수를 완성해주세요.

# 차량번호가 포함된 문자열을 찾고, 문자열의 입/출차 내역으로 요금을 계산한 값을 return한다.

records = [
    "16:00 3961 IN",
    "16:00 0202 IN",
    "18:00 3961 OUT",
    "18:00 0202 OUT",
    "23:58 3961 IN",
]

dict_ = {}
inout = []
for i in records:
    inout.append(i.split(" ")[1])
for i in inout:
    dict_[i] = 0
print(dict_)
