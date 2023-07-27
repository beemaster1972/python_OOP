def get_int(val: str) -> bool:
    try:
        n = int(val)
        return True
    except:
        return False


lst_in = input().split()
sum_int = sum(map(int, filter(get_int, lst_in)))
print(sum_int)
