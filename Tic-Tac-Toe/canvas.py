def welcome_text():
    print("Welcome to Tic-Tac-Toe")


class Canvas:

    def __init__(self):


        self.responses = [" "," "," "," "," "," "," "," "," "]

        self.horizontal_line = "---------"

    def edit_response(self, character, position):
        self.responses[position - 1] = character




    def spot_empty(self, position):
        if self.responses[position] == " ":
            return True
        else:
            return False



    def check_winner(self):
        combinations = [[0,3,6],[1,4,7],[2,5,8],
                        [0,1,2],[3,4,5],[6,7,8],
                        [0,4,8],[2,4,6]]
        for i in combinations:
            if self.responses[i[0]] == self.responses[i[1]] and self.responses[i[1]] == self.responses[i[2]]:
                if self.responses[i[0]] == 'X' or self.responses[i[0]] == 'x':
                    return 'Player 1'
                elif self.responses[i[0]] == 'O' or self.responses[i[0]] == 'o':
                    return 'Player 2'
        return False

    def isfull(self):
        if " " in self.responses:
            return False
        else:
            return True




    def print_canvas(self):

        i = 0
        while i < 9:
            if i not in [2,5,8]:
                print(self.responses[i] + " | ", end="")
                i = i+1
            elif i == 8:
                print(self.responses[i] )
                i = i+1

            else:
                print(self.responses[i])
               # print("\n")
                print(self.horizontal_line)
                i += 1
