n = int(input())
lst = list(map(int, input().split()))
k = int(input())
lst.sort()
left = 0
right = len(lst)-1

while left < right:
    cur_sum = lst[left]+lst[right]
    if cur_sum == k:
        print(lst[left], lst[right])
        break
    elif cur_sum < k:
        left += 1
    elif cur_sum > k:
        right -= 1
else:
    print('None')

# hash_lst = {x: i for i,x in enumerate(lst)}
# for i, el in enumerate(lst):
#     res = hash_lst.get(k-el, None)
#     if res is not None and i != res:
#         print(el, lst[res])
#         break
# else:
#     print("None")



# import numpy as np
# n = int(input())
# lst = list(map(int, input().split())) # np.random.randint(0, n, size=(1,n))
# print(lst)
# k = int(input())
# cur_sum = sum(lst[:k])
# avrg = [cur_sum/k]
# for i in range(0, len(lst)-k):
#     cur_sum -= lst[i]
#     cur_sum += lst[i+k]
#     avrg.append(cur_sum/k)
# print(*avrg)

# n = int(input())
# lst1 = list(map(int, input().split()))
# lst2 = list(map(int, input().split()))
# print(*(x for y in zip(lst1, lst2) for x in y))

# a, b = map(int, (input() for _ in range(2)))
# print(a+b)
