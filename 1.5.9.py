import sys

# здесь объявляются все необходимые классы


class ListObject:

    def __init__(self, data=None):
        self.data = data
        self.next_obj = None

    def link(self, obj):
        self.next_obj = obj


# считывание списка из входного потока (эту строку не менять)
lst_in = list(map(str.strip, sys.stdin.readlines()))  # список lst_in в программе не менять
#lst_in = "foo bar baz foo1 bar1 baz1".split()
# здесь создаются объекты классов и вызываются нужные методы
head_obj = ListObject(lst_in[0])
lo = head_obj
for i in range(1, len(lst_in)):
    lo_new = ListObject(lst_in[i])
    lo.link(lo_new)
    lo = lo_new

lo = head_obj
while True:
    print(lo.data)
    if lo.next_obj != None:
        lo = lo.next_obj
    else:
        break

