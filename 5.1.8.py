def get_number(val:str):
    try:
        return int(val)
    except:
        try:
            return float(val)
        except:
            return val


lst_in = input().split()
print(lst_in)
lst_out = [get_number(x) for x in lst_in]
print(lst_out)