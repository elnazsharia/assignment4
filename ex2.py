
board = []
n = int(input("please enter the row"))
m = int(input("please enter the column"))


def check_board(row, column):
    Checkerboard = [["*"] * row for i in range(column)]
    for i in range(len(Checkerboard)):
        for j in range(len(Checkerboard[i])):
            if i % 2 == 0 and j % 2 == 0:
                Checkerboard[i][j] = "#"
            elif i % 2 == 1 and j % 2 == 1:
                Checkerboard[i][j] = "#"

    for place in Checkerboard:
        print(place, end='')
        print('')


check_board(n, m)
