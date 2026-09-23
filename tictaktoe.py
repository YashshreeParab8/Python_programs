board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']


def show():
    print(f"\n {board[0]} | {board[1]} | {board[2]} \n---|---|---\n "
          f"{board[3]} | {board[4]} | {board[5]} \n---|---|---\n "
          f"{board[6]} | {board[7]} | {board[8]} \n")


def win(mark):
    return (
        (board[0] == board[1] == board[2] == mark) or
        (board[3] == board[4] == board[5] == mark) or
        (board[6] == board[7] == board[8] == mark) or
        (board[0] == board[4] == board[8] == mark) or
        (board[2] == board[4] == board[6] == mark) or
        (board[0] == board[3] == board[6] == mark) or
        (board[1] == board[4] == board[7] == mark) or
        (board[2] == board[5] == board[8] == mark)
    )


def full():
    return all(x in ['X', 'O'] for x in board)


def player():
    while True:
        try:
            choice = int(input("your turn (1-9): "))
        except ValueError:
            print("invalid! enter a number 1-9")
            continue
        if choice < 1 or choice > 9:
            print("invalid! enter a number 1-9")
            continue
        if board[choice - 1] not in ['X', 'O']:
            board[choice - 1] = 'X'
            break
        else:
            print("invalid! spot already taken")


def ai():
    print("AI's turn")
    for i in range(9):
        if board[i] not in ['X', 'O']:
            board[i] = 'O'
            print(f"ai chose {i + 1}")
            break


print("=== TIC TAC TOE ===\nYou - 'X'   AI - 'O'\n")

while True:
    show()
    player()

    if win('X'):
        show()
        print("you win!")
        break

    if full():
        show()
        print("draw")
        break

    ai()

    if win('O'):
        show()
        print("ai wins")
        break

    if full():
        show()
        print("draw")
        break