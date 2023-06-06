# 4 By 4 Skyscrapers

import numpy as np

from sudoku import *

N = 4


def fill_base_constraint(number, puzzle):
    constraint = puzzle[0][number]
    for i in range(1, N + 1):
        if constraint == N:
            puzzle[i][number] = (puzzle[i][number], str(i)) if puzzle[i][number] else i
        if constraint == 1:
            puzzle[1][number] = str(N)


def solve_puzzle(clues):
    puzzle = np.zeros((N + 2, N + 2), tuple)
    for _ in range(4):
        for j in range(1, N + 1):
            puzzle[0][j] = clues[_ + j - 1 + (N - 1) * _]
            fill_base_constraint(j, puzzle)
        puzzle = np.rot90(puzzle)

    return puzzle


clues = (
    (2, 2, 1, 3,
     2, 2, 3, 1,
     1, 2, 2, 3,
     3, 2, 1, 3),
    (0, 0, 1, 2,
     0, 2, 0, 0,
     0, 3, 0, 0,
     0, 1, 0, 0)
)

outcomes = (
    ((1, 3, 4, 2),
     (4, 2, 1, 3),
     (3, 4, 2, 1),
     (2, 1, 3, 4)),
    ((2, 1, 4, 3),
     (3, 4, 1, 2),
     (4, 2, 3, 1),
     (1, 3, 2, 4))
)

solve = solve_puzzle(clues[0])
for _, row in enumerate(solve):
    print(*row)


class Node:
    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n

    def __repr__(self):
        return f'{self.left.value if self.left else "None"}<-- {self.value if self else "None"} -->' \
               f'{self.right.value if self.right else "None"}'


def pre_order(node):
    if node:
        print(node.value)
        pre_order(node.left)
        pre_order(node.right)


tree = Node(None, None, 1)
tree.left = Node(None, None, 2)
tree.right = Node(None, None, 3)
tree.left.left = Node(None, None, 4)
tree.left.right = Node(None, None, 5)


# print(pre_order(tree))


def level_order(node):
    res = [node]
    while len(res) > 0:
        tmp = res.pop(0)
        if tmp:
            yield tmp.value
            if tmp.left:
                res.append(tmp.left)
            if tmp.right:
                res.append(tmp.right)


def tree_by_levels(node: Node):
    if not node:
        return []
    return [x for x in level_order(node)]


# print(tree_by_levels(None))


# print(tree_by_levels(Node(Node(None, Node(None, None, 4), 2), Node(Node(None, None, 5), Node(None, None, 6), 3), 1)))


def queue_time(customers, n):
    if not len(customers):
        return 0
    elif len(customers) <= n:
        return max(customers)
    elif n == 1:
        return sum(customers)
    c = customers
    res = []
    window = []
    left, right = 0, n
    while True:
        window.extend(c[left:right])
        if right >= len(c):
            res.append(max(window))
            break
        else:
            min_time = min(window)
            res.append(min_time)
            for _ in range(window.count(min_time)): window.remove(min_time)
            window = [x - min_time for x in window]
        left = right
        right = n - len(window) + left
    print(res)
    return sum(res)


# must be 101
# print(queue_time([41, 21, 28, 29, 8, 37, 13, 2, 40, 37, 37, 11, 24, 36, 14, 45, 33, 40], 6))
# # должно быть 121
# print(queue_time([47, 37, 29, 47, 11, 49, 5, 12, 34, 33, 48, 42, 49],4))
# print(queue_time([2,2,3,3,4,4], 2))
# print(queue_time([25, 41, 25, 36, 15, 45, 11, 41, 22, 13, 1, 8, 2, 40, 3, 20, 27, 18, 36, 11], 3))
# print(queue_time([9, 34, 11, 23, 36, 50, 32, 15, 35, 45, 43, 36, 44, 33, 16, 18, 48, 8],3))


def remov_nb(n):
    ans = []
    m, r = (n + 1) // 2, n + 1
    sum_of_seq = sum(range(n + 1))
    l = 1  # if m*r < sum_of_seq - m - r else m
    while l < r:
        prod = l * r
        if prod == sum_of_seq - l - r:
            ans.append((l, r))
            ans.append((r, l))
            l += 1
            r -= 1
        elif prod < sum_of_seq - l - r:
            l += 1
        else:
            r -= 1
    # your code
    return sorted(ans, key=lambda x: x[0])


# for _ in range(100_000):
#     a = remov_nb(_)
#     print(_, a)


def last_digit(n1, n2):
    exponents = {0: 4, 1: 1, 2: 2, 3: 3}
    exponent = n2 % 4
    base_digits = n1 % 10
    return base_digits ** exponents[exponent] % 10


# print(last_digit(3715290469715693021198967285016729344580685479654510946723, 68819615221552997273737174557165657483427362207517952651))


def generate_hashtag(s: str):
    # your code here
    res = '#' + ''.join(map(str.capitalize, s.split()))
    return res if len(res) <= 140 and len(s) else False


# print(generate_hashtag('Codewars Is Nice'))
# import time

def strip_comments(strng, markers):
    ans = strng.split('\n')

    for i, strng in enumerate(ans):

        res = ''
        fl = True
        for j, ch in enumerate(strng):
            if ch not in markers and fl:
                res += ch
            else:
                fl = False
        ans[i] = res.strip()
    return '\n'.join(ans)


# print(strip_comments('apples, pears # and bananas\ngrapes\nbananas !apples', ['#', '!']))


def format_duration(seconds):
    if not seconds:
        return 'now'
    years, days = divmod(seconds, 3600 * 24 * 365)
    days, hours = divmod(days, 3600 * 24)
    hours, minutes = divmod(hours, 3600)
    minutes, seconds = divmod(minutes, 60)
    res = f'{years} {"years" if years > 1 else "year"}' if years > 0 else ''
    res += ', ' if res and days else ''
    res += f'{days} {"days" if days > 1 else "day"}' if days > 0 else ''
    res += ', ' if res and hours else ''
    res += f'{hours} {"hours" if hours > 1 else "hour"}' if hours > 0 else ''
    res += ', ' if res and minutes else ''
    res += f'{minutes} {"minutes" if minutes > 1 else "minute"}' if minutes > 0 else ''
    res += ', ' if res and seconds else ''
    res += f'{seconds} {"seconds" if seconds > 1 else "second"}' if seconds > 0 else ''
    match = list(re.finditer(r'(, )', res))
    if match:
        res = res[:match[-1].regs[1][0]] + ' and ' + res[match[-1].regs[1][1]:]
    return res


# print(format_duration(2075562))


def tower_builder(n_floors):
    len_n = 1 + (n_floors - 1) * 2
    res = []
    for i in range(1, n_floors + 1):
        st = ' ' * ((len_n - (1 + (i - 1) * 2)) // 2) + '*' * (1 + (i - 1) * 2) + ' ' * (
                (len_n - (1 + (i - 1) * 2)) // 2)
        res.append(st)
    return res
    # build here


# print(*tower_builder(4),sep='\n')


def make_readable(seconds):
    h, m = divmod(seconds, 3600)
    m, s = divmod(m, 60)
    return f'{h:02}:{m:02}:{s:02}'


def array_diff(a, b):
    # your code here
    set_a, set_b = set(a), set(b)
    set_c = set_a - set_b
    return [x for x in a if x in set_c]


import re


def pig_it(text):
    # your code here
    words = re.findall(r"[\w]+|[,.?!]", text)
    words = [word[1:] + word[0] + 'ay' if word not in ',.?!' else word for word in words]

    return " ".join(words)


# print(pig_it('Hello, world!'))
"""Playing with digits
Some numbers have funny properties. For example:

89 --> 8¹ + 9² = 89 * 1

695 --> 6² + 9³ + 5⁴= 1390 = 695 * 2

46288 --> 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51

Given a positive integer n written as abcd... (a, b, c, d... being digits) and a positive integer p

we want to find a positive integer k, if it exists, such that the sum of the digits of n taken to the successive powers of p is equal to k * n.
In other words:

Is there an integer k such as : (a ^ p + b ^ (p+1) + c ^(p+2) + d ^ (p+3) + ...) = n * k

If it is the case we will return k, if not return -1.

Note: n and p will always be given as strictly positive integers.
"""


def dig_pow(n, p):
    # your code
    k = sum([pow(int(num), p + i) for i, num in enumerate(str(n))]) / n
    return -1 if k % 1 else k


# print(dig_pow(89, 1))
# print(dig_pow(92, 1))
# print(dig_pow(46288, 3))
# print(dig_pow(41, 5))

# Playing with digits 6 kyu


def is_square(n):
    return False if n < 0 else pow(n, 1 / 2) == int(pow(n, 1 / 2))  # fix me


# print(is_square(-1), is_square(4), is_square(1), is_square(2), is_square(3), is_square(25))


def duplicate_count(text):
    # Your code goes here
    txt = text.lower()
    return len([c for c in txt if txt.count(c) > 1])
