import numpy as np
import random as rnd


class Cell:

    def __init__(self, around_mines: int, mine: bool):
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = False


class GamePole:

    def init(self, N, M):
        total_mines_count = 0
        for i in range(N):
            row_mines_count = 0
            for j in range(N):
                mine = bool(rnd.randint(0, 1)) if total_mines_count < M and row_mines_count < N//5 and\
                       bool(rnd.randint(0, 1)) else False
                total_mines_count += 1 if mine else 0
                row_mines_count += 1 if mine else 0
                self.pole[i][j] = Cell(0, mine)
        for i in range(N):
            for j in range(N):
                self.pole[i][j].mines_around = self.set_mines_arround(i, j)

    def __init__(self, N, M):
        self.pole = np.zeros((N, N), dtype=Cell)
        self.dimension = N
        self.total_mines = M
        self.init(self.dimension, self.total_mines)

    def set_mines_arround(self, x: int, y: int):
        if self.pole[x][y].mine:
            return 0
        sub_matrix = [self.pole[i][j].mine for j in range(max(0, y-1), min(self.dimension, y+2))
                      for i in range(max(0, x-1), min(self.dimension, x+2))]
        return sum(sub_matrix)

    def show(self):

        for i in range(self.dimension):
            for j in range(self.dimension):
                # cell = self.pole[i][j].around_mines if self.pole[i][j].fl_open else '#'
                cell = '#' if self.pole[i][j].mine else self.pole[i][j].mines_around

                print(cell, end=' ')
            print()


if __name__ == '__main__':
    pole_game = GamePole(10, 12)
    pole_game.show()
