__author__ = 'stehb'


class Christmas1:

    GIVEN_POINTS = [(3,  3),
                    (4,  3),
                    (12, 3),
                    (13, 3),
                    (21, 3),
                    (6,  8),
                    (7,  8),
                    (10, 8),
                    (14, 8),
                    (15, 8),
                    (18, 8),
                    (6,  16),
                    (11, 16),
                    (16, 16),
                    (20, 16),
                    (3,  21),
                    (4,  21),
                    (9,  21),
                    (10, 21),
                    (15, 21),
                    (10, 21),
                    (20, 21),
                    (21, 21),
                    ]

    ROW_DATA = [
        [7, 3, 1, 1, 7],
        [1, 1, 2, 2, 1, 1],
        [1, 3, 1, 3, 1, 1, 3, 1],
        [1, 3, 1, 1, 6, 1, 3, 1],
        [1, 3, 1, 5, 2, 1, 3, 1],
        [1, 1, 2, 1, 1],
        [7, 1, 1, 1, 1, 1, 7],
        [3, 3],
        [1, 2, 3, 1, 1, 3, 1, 1, 2],
        [1, 1, 3, 2, 1, 1],
        [4, 1, 4, 2, 1, 2],
        [1, 1, 1, 1, 1, 4, 1, 3],
        [2, 1, 1, 1, 2, 5],
        [3, 2, 2, 6, 3, 1],
        [1, 9, 1, 1, 2, 1],
        [2, 1, 2, 2, 3, 1],
        [3, 1, 1, 1, 1, 5, 1],
        [1, 2, 2, 5],
        [7, 1, 2, 1, 1, 1, 3],
        [1, 1, 2, 1, 2, 2, 1],
        [1, 3, 1, 4, 5, 1],
        [1, 3, 1, 3, 10, 2],
        [1, 3, 1, 1, 6, 6],
        [1, 1, 2, 1, 1, 2],
        [7, 2, 1, 2, 5],
    ]


    HORIZ_DATA = [
        [7, 2, 1, 1, 7],
        [1, 1, 2, 2, 1, 1],
        [1, 3, 1, 3, 1, 3, 1, 3, 1],
        [1, 3, 1, 1, 5, 1, 3, 1],
        [1, 3, 1, 1, 4, 1, 3, 1],
        [1, 1, 1, 2, 1, 1],
        [7, 1, 1, 1, 1, 1, 7],
        [1, 1, 3],
        [2, 1, 2, 1, 8, 2, 1],
        [2, 2, 1, 2, 1, 1, 1, 2],
        [1, 7, 3, 2, 1],
        [1, 2, 3, 1, 1, 1, 1, 1],
        [4, 1, 1, 2, 6],
        [3, 3, 1, 1, 1, 3, 1],
        [1, 2, 5, 2, 2],
        [2, 2, 1, 1, 1, 1, 1, 2, 1],
        [1, 3, 3, 2, 1, 8, 1],
        [6, 2, 1],
        [7, 1, 4, 1, 1, 3],
        [1, 1, 1, 1, 4],
        [1, 3, 1, 3, 7, 1],
        [1, 3, 1, 1, 2, 1, 1, 4],
        [1, 3, 1, 4, 3, 3],
        [1, 1, 2, 2, 2, 6, 1],
        [7, 1, 3, 2, 1, 1],
    ]


    def __init__(self):
        self.grid = [[0 for i in range(25)] for j in range(25)]
        self.givenPoints

        for point in self.GIVEN_POINTS:
            self.grid[point[1]][point[0]] = 1



    def printGrid(self):
        y = 0
        str = ""
        for row in self.grid:
            str = ''.join(' {:d}'.format(i) for i in row)
            print(str)


    def solve(self):
        self.printGrid()
        print "YO"






if __name__ == '__main__':
    puzzle = Christmas1()
    puzzle.solve()

