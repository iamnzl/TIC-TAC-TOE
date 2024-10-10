
from canvas import Canvas, welcome_text

canvas = Canvas()
welcome_text()
canvas.print_canvas()
#
# player1_input = input("Player 1, insert position of x:")
# canvas.edit_response(position=int(player1_input), character="x")
# canvas.print_canvas()
#
# player2_input = input("Player 2, insert position of o:")
# canvas.edit_response(position=int(player2_input), character="o")
# canvas.print_canvas()

play = True
while play:
    if not canvas.isfull():
        #Check if anyone has won
        if canvas.check_winner():
            play = False
            print(f"{canvas.check_winner()} wins")
        else:
            ask_player1 = True
            ask_player2 = True
            while ask_player1:
                player1_input = input("Player 1, insert position of x:")
                if not canvas.spot_empty(int(player1_input) - 1):
                    print("Spot not empty")
                else:
                    canvas.edit_response(position=int(player1_input), character="x")
                    canvas.print_canvas()
                    ask_player1 = False

            if canvas.check_winner():
                play = False
                print(f"{canvas.check_winner()} wins")
                continue
            if canvas.isfull():
                print("It is a Tie")
                play = False
                continue

            while ask_player2:

                player2_input = input("Player 2, insert position of o:")
                if not canvas.spot_empty(int(player2_input) - 1):
                    print("Spot not empty")
                else:

                    canvas.edit_response(position=int(player2_input), character="o")
                    canvas.print_canvas()
                    ask_player2 = False

    else:
        if canvas.check_winner():
            play = False
            print(f"{canvas.check_winner()} wins")
        else:
            print("Its a Tie")