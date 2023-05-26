def queue_time(customers, n):
    if not len(customers):
        return 0
    elif len(customers) <= n:
        return max(customers)
    c = customers.copy()
    res = []
    tills = set()
    i = 0
    while True:

        tills |= set(c[i:n-len(tills)+i])
        if i + n >= len(customers):
            res.append(max(tills))
            break
        else:
            res.append(min(tills))
            tills.remove(min(tills))
        i += n
    return sum(res)


# print(queue_time([], 1))
# print(queue_time([2,2,3,3,4,4], 2))
print(queue_time([25, 41, 25, 36, 15, 45, 11, 41, 22, 13, 1, 8, 2, 40, 3, 20, 27, 18, 36, 11],3))


def tower_builder(n_floors):
    len_n = 1+ (n_floors-1)*2
    res = []
    for i in range(1,n_floors+1):
      st = ' '*((len_n -(1+(i-1)*2))//2)+'*'*(1+(i-1)*2)+' '*((len_n -(1+(i-1)*2))//2)
      res.append(st)
    return res
    # build here

#print(*tower_builder(4),sep='\n')


def make_readable(seconds):
  h, m = divmod(seconds, 3600)
  m, s = divmod(m, 60)
  return f'{h:02}:{m:02}:{s:02}'


def array_diff(a, b):
    #your code here
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
    k = sum([pow(int(num), p+i) for i, num in enumerate(str(n))])/n
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
