def get_loss(w1, w2, w3, w4):
    y = 10 * w1
    try:
        y //= w2
    except:
        ...  # return "деление на ноль"
    else:
        y = y - 5 * w2 * w3 + w4
    return y


if __name__ == '__main__':
    print(get_loss(10, 20, 30, 40))
    print(get_loss(10, 0, 30, 40))
