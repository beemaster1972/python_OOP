class BookStudy:

    def __init__(self, name, author, year):
        self.name = name
        self.author = author
        self.year = year

    def __hash__(self):
        return hash((self.name.lower(), self.author.lower()))

    def __repr__(self):
        return f'"{self.name}" автор: {self.author} год: {self.year}'

    def __eq__(self, other):
        return hash(self) == hash(other)

lst_in = [input().strip() for _ in range(4)]
lst_bs = []
for i, st in enumerate(lst_in):
    name, author, year = tuple(map(str.strip, st.split(';')))
    year = int(year)
    lst_bs.append(BookStudy(name, author, year))

print(*lst_bs)

unique_books = len({x:x for x in lst_bs})
print(unique_books)