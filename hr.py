from calendar import weekday
answer = list(map(int, input().split()))
print(["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"][weekday(answer[2],answer[0],answer[1])].upper())

# from itertools import product
#
#
# def square_int(val: str):
#     return int(val) ** 2
#
#
# K, M = map(int, input().split())
# lst, sum_lst = [], []
# s = 0
# for _ in range(K):
#     lst.append(list(map(square_int, input().split()))[1:])
#
# prod_lst = list(product(*lst))
# for el in prod_lst:
#     sum_lst.append(sum(el)%M)
# print(max(sum_lst))

# def is_leap(year):
#     leap = False
#
#     # Write your logic here
#
#     return (year % 100 == 0 and year % 400 == 0) or (year % 4 == 0 and bool(year % 100))
#
#
# year = int(input())
# print(year % 100, year % 400, year % 4)
# print(is_leap(year))
