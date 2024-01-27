def print_maze(maze, n):
    for row in maze:
        for col in range(n):
            print(row[col], end=' ')
        print()

def main():
    satr = ['.'] * int(input())
    makan = [['.'] * len(satr) for _ in range(1000)]
    i, j = 0, 0
    makan[i][j] = '*'

    c = input()

    while c != "END":
        if c == "R" and j < len(satr) - 1:
            j += 1
        elif c == "L" and j - 1 >= 0:
            j -= 1
        elif c == "B":
            i += 1
        makan[i][j] = '*'
        c = input()

    while satr in makan:
        makan.remove(satr)

    print_maze(makan, len(satr))

    if j != len(satr) - 1:
        print("There's no way out!")

if __name__ == "__main__":
    main()
