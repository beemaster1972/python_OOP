class Player:

    def __init__(self, name, old, score):
        self.name, self.old, self.score = name, old, score

    def __bool__(self):
        return self.score > 0

    def __repr__(self):
        return f'{self.name} возраст {self.old} счёт {self.score}'


lst_in = list((list(map(str.strip, input().split(';'))) for _ in range(4)))
players = [Player(x[0], int(x[1]), int(x[2])) for x in lst_in]
players_filtered = filter(lambda x: bool(x), players)
print(*players)
print(*players_filtered)
