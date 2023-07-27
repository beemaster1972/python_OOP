a, b = input().split()
total = 0
new_str = ''
try:
    total = int(a) + int(b)
except:
    try:
        total = float(a)+float(b)
    except:
        total = a + b
finally:
    print(total)