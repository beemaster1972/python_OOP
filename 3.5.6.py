import re


class Morph:

    def __init__(self, *args):
        self._words = [x.lower() for x in args]


    @property
    def words(self):
        return self._words

    def add_word(self, word):
        if word not in self._words:
            self._words.append(word)

    def get_words(self):
        return tuple(self._words)

    def __eq__(self, other):
        return other.lower() in self._words

    def __str__(self):
        return ' '.join(self._words)


words_lst = ['связь, связи, связью, связей, связям, связями, связях',
             'формула, формулы, формуле, формулу, формулой, формул, формулам, формулами, формулах',
             'вектор, вектора, вектору, вектором, векторе, векторы, векторов, векторам, векторами, векторах',
             'эффект, эффекта, эффекту, эффектом, эффекте, эффекты, эффектов, эффектам, эффектами, эффектах',
             'день, дня, дню, днем, дне, дни, дням, днями, днях']
delimiters = r"[ ,.-;:!?()]+"
dict_words = [Morph(*re.split(delimiters, x)) for x in words_lst]
print(*dict_words, sep='\n')

text = re.split(delimiters, input())
print(text)
count = 0
for __, words in enumerate(dict_words):
    count += len(list(filter(lambda x: words == x, text)))

print(count)

