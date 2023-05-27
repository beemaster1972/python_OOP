


# s = ''
# print(len(s), len(s.upper().lower()))


# def validate_hello(greetings):
#     hello = {'hello':'english', 'ciao':'italian', 'salut':'french', 'hallo':'german',
#              'hola':'spanish', 'ahoj':'czech republic', 'czesc':'polish'}
#     return any([key in greetings.lower() for key in hello])

# print(validate_hello('Привет'))


# def create_phone_number(n):
#
#     n_to_str = list(map(str, n))
#     return f'({"".join(n_to_str[:3])}) {"".join(n_to_str[3:6])}-{"".join(n_to_str[6:10])}'
#
#
# print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3]))
# import math
# import os
# import random
# import re
# import sys
# import datetime as dt
#
#
# # Complete the time_delta function below.
# # month = {'jan': (1, 31), 'feb': (2, 28), 'mar': (3, 31), 'apr': (4, 30), 'may': (5, 31), 'jun': (6, 30),
# #          'jul': (7, 31), 'aug': (8, 31), 'sep': (9, 30), 'oct': (10, 30), 'nov': (11, 30), 'dec': (12,31)}
# def time_delta(t1, t2):
#     format_str = "%a %d %b %Y %H:%M:%S %z"
#     time1 = dt.datetime.strptime(t1, format_str)
#     time2 = dt.datetime.strptime(t2, format_str)
#     res = abs(int((time1 - time2).total_seconds()))
#     return str(res)
#
#
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#     t = int(input())
#
#     for t_itr in range(t):
#         t1 = input()
#
#         t2 = input()
#
#         delta = time_delta(t1, t2)
#
#         fptr.write(delta + '\n')
#
#     fptr.close()

# import numpy as np
#
# if __name__ == '__main__':
#     A = list(map(int, input().split()))
#     B = list(map(int, input().split()))
#     print(np.inner(A, B))
#     print(np.outer(A, B), sep='\n')

# if __name__ == '__main__':
#     n = int(input())
#     student_marks = {}
#     for _ in range(n):
#         name, *line = input().split()
#         scores = list(map(float, line))
#         student_marks[name] = scores
#     query_name = input()
#     print(f'{sum(student_marks[query_name])/len(student_marks[query_name]):.2f}')


# def stud_key(lst):
#     return lst[1]
#
#
# if __name__ == '__main__':
#     studs = {}
#     for _ in range(int(input())):
#         name = input()
#         score = float(input())
#         try:
#             studs[score].append(name)
#         except:
#             studs[score] = [name]
#     scores = sorted([score for score in studs.keys()])
#     print(*sorted(studs[scores[1]]), sep='\n')


# if __name__ == '__main__':
#     n = int(input())
#     arr = map(int, input().split())
#     print(sorted(set(arr))[-2])

# from itertools import permutations, product
#
#
# if __name__ == '__main__':
#     x = int(input())
#     y = int(input())
#     z = int(input())
#     n = int(input())
#
#     lst_x = [i for i in range(0, x+1)]
#     lst_y = [j for j in range(0, y+1)]
#     lst_z = [k for k in range(0, z+1)]
#     coords = [coord for coord in product(lst_x, lst_y, lst_z) if sum(coord) != n]
#    # coords = [coord for coord in permutations([lst_x, lst_y, lst_z],3)]# if sum(coord) != n]
#
#     print(*coords)


# from calendar import weekday
# answer = list(map(int, input().split()))
# print(["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"][weekday(answer[2],answer[0],answer[1])].upper())

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
