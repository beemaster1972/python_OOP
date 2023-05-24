#Playing with digits 6 kyu


def is_square(n):
    return False if n < 0 else pow(n, 1 / 2) == int(pow(n, 1 / 2))  # fix me

print(is_square(-1), is_square(4), is_square(1), is_square(2), is_square(3), is_square(25))

def duplicate_count(text):
    # Your code goes here
    txt = text.lower()
    return len([c for c in txt if txt.count(c) > 1])
