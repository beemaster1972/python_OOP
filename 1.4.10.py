lst_in = [('tree', 'дерево'),
          ('car', 'машина'),
          ('car', 'автомобиль'),
          ('leaf', 'лист'),
          ('river', 'река'),
          ('go', 'идти'),
          ('go', 'ехать'),
          ('go', 'ходить'),
          ('milk', 'молоко')]


class Translator:

    vocab = dict()

    def add(self, eng, rus):
        if eng in self.vocab and rus not in self.vocab[eng]:
            self.vocab[eng].append(rus)
        elif eng not in self.vocab:
            self.vocab[eng] = [rus]

    def remove(self, eng):
        del self.vocab[eng]

    def translate(self, eng):
        return self.vocab[eng]


tr = Translator()
for st in lst_in:
    eng, rus = st
    tr.add(eng, rus)
tr.remove('car')
print(*tr.translate('go'))
