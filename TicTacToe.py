the_board = {'7': ' ', '8': ' ', '9': ' ',
             '4': ' ', '5': ' ', '6': ' ',
             '1': ' ', '2': ' ', '3': ' '}
board_key = []
for key in the_board:
    board_key.append(key)


def make_board(board):
    print(board['7'] + ' | ' + board['8'] + ' | ' + board['9'])
    print('--+---+--')
    print(board['4'] + ' | ' + board['5'] + ' | ' + board['6'])
    print('--+---+--')
    print(board['1'] + ' | ' + board['2'] + ' | ' + board['3'])


def game():
    turn = 'X'
    count = 0

    for i in range(10):
        make_board(the_board)
        print("It is your turn,", turn, "where do you want to go next?? : ")

        move = input()

        if the_board[move] == ' ':
            the_board[move] = turn
            count += 1

        else:
            print("That place is already filled chose again!!")
            continue

        if count >= 5:
            if the_board['7'] == the_board['8'] == the_board['9'] != ' ':
                make_board(the_board)
                print("Game over")
                print(turn, "WON")
                break
            elif the_board['4'] == the_board['5'] == the_board['6'] != ' ':
                make_board(the_board)
                print("Game over")
                print(turn, "WON")
                break
            elif the_board['1'] == the_board['2'] == the_board['3'] != ' ':
                make_board(the_board)
                print("Game over")
                print(turn, "WON")
                break
            elif the_board['7'] == the_board['4'] == the_board['1'] != ' ':
                make_board(the_board)
                print("Game over")
                print(turn, "WON")
                break
            elif the_board['8'] == the_board['5'] == the_board['2'] != ' ':
                make_board(the_board)
                print("Game over")
                print(turn, "WON")
                break
            elif the_board['9'] == the_board['6'] == the_board['3'] != ' ':
                make_board(the_board)
                print("Game over")
                print(turn, "WON")
                break
            elif the_board['7'] == the_board['5'] == the_board['3'] != ' ':
                make_board(the_board)
                print("Game over")
                print(turn, "WON")
                break
            elif the_board['9'] == the_board['5'] == the_board['1'] != ' ':
                make_board(the_board)
                print("Game over")
                print(turn, "WON")
                break

        if count == 9:
            print("Game over")
            print("The match is TIE")

        if turn == 'X':
            turn = "O"
        else:
            turn = "X"

    restart = input("Do you want to play again??(y/n)").lower()
    if restart == "y":
        for key1 in board_key:
            the_board[key1] = ' '

        game()


if __name__ == "__main__":
    game()
