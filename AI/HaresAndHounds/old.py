class game:
    def __init__(self):
        self.board = ["*"] * 11
        self.board[1] = "W0"
        self.board[0] = "W1"
        self.board[3] = "W2"
        self.board[10] = "H"

        self.wolfs  = [1, 0, 3]
        self.hare = 10

    def printState(self):
        row1 = "  " + self.board[1] + " - " + self.board[4] + " - " + self.board[7]
        row2 = self.board[0] + " - " + self.board[2] + " - " + self.board[5] + " - " + self.board[8] + " - " + \
               self.board[10]
        row3 = "  " + self.board[3] + " - " + self.board[6] + " - " + self.board[9]
        state = row1 + "\n" +row2 + "\n" + row3 + "\n"
        print(state)
    def printBoardTutorial(self):
        row1 = "  " + "1" + " - " + "4" + " - " + "7"
        row2 = "0" + " - " + "2" + " - " + "5" + " - " + "8" + " - " + \
               "10"
        row3 = "  " + "3" + " - " + "6" + " - " + "9"
        state = row1 + "\n" +row2 + "\n" + row3 + "\n"
        print(state)
    def moveHare(self, where):
        hareOld = self.hare
        hareNew = where

        #Check if move possible
        if self.board[hareNew] != "*":
            return -1
        if where < 0 or where > 10:
            return -1
        if hareOld == 10 and not(hareNew in [7,8,9]):
            return -1
        if hareOld == 9 and not(hareNew in [6,5,8,10]):
            return -1
        if hareOld == 8 and not(hareNew in [10,7,9,4,5,6]):
            return -1
        if hareOld == 7 and not(hareNew in [10,8,5,4]):
            return -1
        if hareOld == 6 and not(hareNew in [9,8,6,2,3]):
            return -1
        if hareOld == 5 and not(hareNew in [1,4,7,8,9,6,3,2]):
            return -1
        if hareOld == 4 and not(hareNew in [7,8,5,2,1]):
            return -1
        if hareOld == 3 and not(hareNew in [0,2,5,6]):
            return -1
        if hareOld == 2 and not(hareNew in [0,1,3,4,5,6]):
            return -1
        if hareOld == 1 and not(hareNew in [9,2,5,4]):
            return -1
        if hareOld == 0:
            return -1

        self.hare = hareNew
        self.board[hareOld] = "*"
        self.board[hareNew] = "H"
        return 1
    def moveWolf(self, witch, where):
        wolfOld = self.wolfs[witch]
        wolfNew = where

        #Check if move possible
        if where < 0 or where > 10:
            return -1
        if self.board[wolfNew] != "*":
            return -1
        if wolfOld == 0 and not(wolfNew in [1, 2, 3]):
            return -1
        if wolfOld == 1 and not(wolfNew in [2, 4, 5]):
            return -1
        if wolfOld == 2 and not(wolfNew in [1, 3, 4, 5, 6]):
            return -1
        if wolfOld == 3 and not(wolfNew in [2, 5, 6]):
            return -1
        if wolfOld == 4 and not(wolfNew in [5, 7, 7]):
            return -1
        if wolfOld == 5 and not(wolfNew in [5, 6, 7, 8, 9]):
            return -1
        if wolfOld == 6 and not(wolfNew in [5, 8, 9]):
            return -1
        if wolfOld == 7 and not(wolfNew in [8, 10]):
            return -1
        if wolfOld == 8 and not(wolfNew in [7, 9, 10]):
            return -1
        if wolfOld == 9 and not(wolfNew in [8, 10]):
            return -1
        if wolfOld == 10:
            return -1

        self.wolfs[witch] = wolfNew
        self.board[wolfOld] = "*"
        self.board[wolfNew] = "W" + str(witch)
        return 1
    def checkWin(self):
        if self.hare < self.wolfs[0] and self.hare < self.wolfs[1] and self.hare < self.wolfs[2]:
            return "hare"

        return 0

#MAIN

G = game()
while True:
    print("Choose a move from: Wx y or H y")
    G.printBoardTutorial()
    G.printState()
    inpt = input()
    inpt = inpt.split(" ")
    r = 0
    if inpt[0] == "W0":
        r = G.moveWolf(0, int(inpt[1]))
    elif inpt[0] == "W1":
        r = G.moveWolf(1, int(inpt[1]))
    elif inpt[0] == "W2":
        r = G.moveWolf(2, int(inpt[1]))
    elif inpt[0] == "H":
        r = G.moveHare(int(inpt[1]))
    if r == -1:
        print("The move is not possible, please choose another move")
    if G.checkWin() == "hare":
        print("Hare Wins!")



