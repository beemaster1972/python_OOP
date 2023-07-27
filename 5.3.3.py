def input_int_numbers():
    try:
        nums = map(int, input().split())
    except:
        raise TypeError('все числа должны быть целыми')
    return tuple(nums)


while True:
    try:
        print(*input_int_numbers())
        break
    except:
        pass

