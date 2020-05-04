import copy
from interface import interfacePlayPVP
import time
class Game:
    def __init__(self, ai = None, difficulty = None, algorithm = None):
        w, h = 5, 3;
        self.board = [["*" for x in range(w)] for y in range(h)]
        self.board[1][0] = "W0"
        self.board[0][1] = "W1"
        self.board[2][1] = "W2"
        self.board[1][4] = "H"
        self.difficulty = difficulty
        self.algorithm = algorithm
        self.wolfs = [(1, 0), (0, 1), (2, 1)]
        self.hare = (1, 4)
        self.ai = ai
        self.sameColumnMoves = 0

    def reset(self):
        w, h = 5, 3;
        self.board = [["*" for x in range(w)] for y in range(h)]
        self.board[1][0] = "W0"
        self.board[0][1] = "W1"
        self.board[2][1] = "W2"
        self.board[1][4] = "H"
        self.wolfs = [(1, 0), (0, 1), (2, 1)]
        self.hare = (1, 4)
    def printState(self):
        # Printing the state of the board
        row1 = "    " + self.board[0][1] + " - " + self.board[0][2] + " - " + self.board[0][3]
        row2 = self.board[1][0] + " - " + self.board[1][1] + " - " + self.board[1][2] + " - " + self.board[1][
            3] + " - " + \
               self.board[1][4]
        row3 = "    " + self.board[2][1] + " - " + self.board[2][2] + " - " + self.board[2][3]
        state = row1 + "\n" + row2 + "\n" + row3 + "\n"
        print(state)

    def getWolfPositions(self):
        #Getting the position of the wolves
        return self.wolfs

    def getHarePositions(self):
        #Getting the position of the hare
        return self.hare

    def printBoardTutorial(self):
        row1 = "  " + "      (0,1)" + " - " + "(0,2)" + " - " + "(0,3)"
        row2 = "(1,0)" + " - " + "(1,1)" + " - " + "(1,2)" + " - " + "(1,3)" + " - " + \
               "(1,4)"
        row3 = "  " + "      (2,1)" + " - " + "(2,2)" + " - " + "(2,3)"
        state = row1 + "\n" + row2 + "\n" + row3 + "\n"
        print(state)

    def moveHare(self, where, ai=False):
        hareOld = self.hare
        hareNew = where

        if self.ai == "hare" and ai == False:
            return -1
        if self.board[where[0]][where[1]] != "*":
            return -1
        if self.checkInBounds(hareNew) == -1:
            return -1
        if self.checkIfNeighbor(hareOld, hareNew) == -1:
            return -1
        self.hare = hareNew
        self.board[hareOld[0]][hareOld[1]] = "*"
        self.board[hareNew[0]][hareNew[1]] = "H"

    def moveWolf(self, which, where, ai=False):

        wolfOld = self.wolfs[which]
        wolfNew = where

        if self.ai == "wolf" and ai == False:
            return -1
        if self.board[where[0]][where[1]] != "*":
            return -1
        if self.checkInBounds(wolfNew) == -1:
            return -1
        if self.checkIfNeighbor(wolfOld, wolfNew) == -1:
            return -1
        if self.checkIfLeftRight(wolfOld, wolfNew) == -1:
            return -1

        # checking if the move is on the same column
        # Because at 10 we want game over
        if self.checkIfSameColumn(wolfOld, wolfNew):
            self.sameColumnMoves += 1
        else:
            self.sameColumnMoves = 0
        self.wolfs[which] = wolfNew
        self.board[wolfOld[0]][wolfOld[1]] = "*"
        self.board[wolfNew[0]][wolfNew[1]] = "W" + str(which)

    def movePosition(self, which, where):
        #Moving based on positions
        if "W" in self.board[which[0]][which[1]]:
            return self.moveWolf(int(self.board[which[0]][which[1]].replace("W", "")), where, True)
        if "H" in self.board[which[0]][which[1]]:
            return self.moveHare(where, True)

    def checkWin(self):
        # Checking if the wolves consomed all the same column moves
        if self.sameColumnMoves == 10:
            return "hare"
        # Checking if all the wolves are in the right of the hare
        if self.checkIfLeftRight(self.hare, self.wolfs[0]) == 1 and self.checkIfLeftRight(self.hare, self.wolfs[1]) == 1 \
                and self.checkIfLeftRight(self.hare, self.wolfs[2]) == 1:
            return "hare"
        # checking if hare has possible moves
        ok = 0
        for (i,j) in [(0, 1), (0, 2), (0, 3), (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (2, 1), (2, 2), (2, 3)]:
            if self.checkIfNeighbor(self.hare, (i,j)) == 1:
                if self.board[i][j] == "*":
                    ok = 1
        if ok == 0:
            return "wolf"
        return 0

    def checkInBounds(self, coords):
        # check if some coordinates are in the bounds of the 2d Array
        if coords in [(0, 1), (0, 2), (0, 3), (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (2, 1), (2, 2), (2, 3)]:
            return 1
        else:
            return -1

    def checkIfLeftRight(self, left, right):
        # Checks if left is in the left of right
        if left[1] <= right[1]:
            return 1
        else:
            return -1

    def checkIfNeighbor(self, a, b):
        #Exclude middle edges:
        if self.excludeMiddleEdges(a, b) == -1:
            return -1
        # Checks if a and b are neighbors
        if b in [(a[0] - 1, a[1] - 1), (a[0], a[1] - 1), (a[0] + 1, a[1] - 1), (a[0] - 1, a[1]), (a[0] + 1, a[1]),
                 (a[0] - 1, a[1] + 1), (a[0], a[1] + 1), (a[0] + 1, a[1] + 1)]:
            return 1
        else:
            return -1

    def excludeMiddleEdges(self, a ,b):
        # Excludes the middle edges on the board
        if a == (1,1) and b == (0,2):
            return -1
        if b == (1,1) and a == (0,2):
            return -1
        if a == (1,1) and b == (2,2):
            return -1
        if b == (1,1) and a == (2,2):
            return -1
        if a == (0,2) and b == (1,3):
            return -1
        if b == (0,2) and a == (1,3):
            return -1
        if a == (2,2) and b == (1,3):
            return -1
        if b == (2,2) and a == (1,3):
            return -1
        return 1

    def distanceTillWin(self):
        #Return distance till the goal
        return self.hare[1]

    def possibleMovesHare(self):
        #Returs all the possible moves that the hare on that position can do
        possibleMoves = []
        allMoves = [(0, 1), (0, 2), (0, 3), (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (2, 1), (2, 2), (2, 3)]
        for move in allMoves:
            if self.board[move[0]][move[1]] != "*":
                continue
            if self.checkIfNeighbor(self.hare, move) == -1:
                continue
            possibleMoves.append(move)
        return possibleMoves

    def possibleMovesWolf(self, which):
        #Returs all the possible moves that a wolf on that position can do
        wolfOld = self.wolfs[which]
        possibleMoves = []
        allMoves = [(0, 1), (0, 2), (0, 3), (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (2, 1), (2, 2), (2, 3)]
        for move in allMoves:
            if self.board[move[0]][move[1]] != "*":
                continue
            if self.checkIfNeighbor(wolfOld, move) == -1:
                continue
            if self.checkIfLeftRight(wolfOld, move) == -1:
                continue
            possibleMoves.append(move)
        return possibleMoves

    def makeAIMove(self):
        if self.ai == None:
            return None
        ai = AI(self, self.difficulty, self.algorithm)
        #move = ai.minimax(self, self.ai)
        move = ai.makeMove(self, self.ai)
        self.movePosition(move[1], move[2])

    def getScore(self):
        # Score function based on distance till win
        won = self.checkWin()
        if won == "hare":
            return -99
        if won == "wolf":
            return 99
        return self.distanceTillWin()

    def checkIfSameColumn(self, frm, where):
        # check if a move is on the same column
        if frm[1] == where[1]:
            return True
        return False
class AI:
    def __init__(self, state, difficulty = "medium", algorithm="minimax"):
        self.gameState = state
        if difficulty == "hard":
            self.MAX_DEPTH = 20
        elif difficulty == "medium":
            self.MAX_DEPTH = 7
        else:
            self.MAX_DEPTH = 4
        self.algorithm = algorithm

    def makeMove(self, state, player):
        if self.algorithm == "minimax":
            return self.minimax(state, player)
        else:
            return self.minimaxAlphaBeta(state, player)
    def heuristic(self, state):
        # Heuristic function based on if won or else on distance till the hare win
        won = state.checkWin()
        if won == "hare":
            return -99
        if won == "wolf":
            return 99
        return state.distanceTillWin()

    def minimax(self, state, player, depth=5, frm=(0,0), to=(0,0)):
        if depth == 0 or state.checkWin() == "wolf" or state.checkWin() == "hare":
            return self.heuristic(state), frm, to

        # Getting all the possible moves that we can do
        possibleMoves = []
        if player == "hare":
            harePos = state.getHarePositions()
            for move in state.possibleMovesHare():
                possibleMoves.append((harePos, move))
        else:
            wolfPos = state.getWolfPositions()
            for move in state.possibleMovesWolf(0):
                possibleMoves.append((wolfPos[0], move))
            for move in state.possibleMovesWolf(1):
                possibleMoves.append((wolfPos[1], move))
            for move in state.possibleMovesWolf(2):
                possibleMoves.append((wolfPos[2], move))

        # Finding the best move
        if player == "hare":
            # We want the score to be minimal
            moves = []
            for move in possibleMoves:
                nextState = copy.deepcopy(state)
                nextState.movePosition(move[0], move[1])
                tempScore, tempFrm, tempTo = self.minimax(nextState, "wolf", depth-1, move[0], move[1])
                moves.append((tempScore, move[0], move[1]))
            moves.sort()
        else:
            # We have wolf
            # We want the score to be maximal
            moves = []
            for move in possibleMoves:
                nextState = copy.deepcopy(state)
                nextState.movePosition(move[0], move[1])
                tempScore, tempFrm, tempTo = self.minimax(nextState, "hare", depth-1, move[0], move[1])
                moves.append((tempScore, move[0], move[1]))
            moves.sort(reverse = True)
        #returning the best move
        return moves[0]

    def minimaxAlphaBeta(self, state, player, depth=5, frm=(0, 0), to=(0, 0), alpha = -99, beta = 99):
        if depth == 0 or state.checkWin() == "wolf" or state.checkWin() == "hare":
            return self.heuristic(state), frm, to

        # Getting all the possible moves that we can do
        possibleMoves = []
        if player == "hare":
            harePos = state.getHarePositions()
            for move in state.possibleMovesHare():
                possibleMoves.append((harePos, move))
        else:
            wolfPos = state.getWolfPositions()
            for move in state.possibleMovesWolf(0):
                possibleMoves.append((wolfPos[0], move))
            for move in state.possibleMovesWolf(1):
                possibleMoves.append((wolfPos[1], move))
            for move in state.possibleMovesWolf(2):
                possibleMoves.append((wolfPos[2], move))

        # Finding the best move
        if player == "hare":
            # We want the score to be minimal
            moves = []
            for move in possibleMoves:
                nextState = copy.deepcopy(state)
                nextState.movePosition(move[0], move[1])
                tempScore, tempFrm, tempTo = self.minimaxAlphaBeta(nextState, "wolf", depth - 1, move[0], move[1], alpha, beta)
                beta = min(beta, tempScore)
                moves.append((tempScore, move[0], move[1]))
                if beta <= alpha:
                    break
            moves.sort()
        else:
            # We have wolf
            # We want the score to be maximal
            moves = []
            for move in possibleMoves:
                nextState = copy.deepcopy(state)
                nextState.movePosition(move[0], move[1])
                tempScore, tempFrm, tempTo = self.minimaxAlphaBeta(nextState, "hare", depth - 1, move[0], move[1],alpha, beta)
                alpha = max(alpha, tempScore)
                moves.append((tempScore, move[0], move[1]))
                if beta <= alpha:
                    break
            moves.sort(reverse=True)
        # returning the best move
        return moves[0]


def playTerminalPVP():
    G = Game()
    while True:
        print("Choose a move from: Wx i j or H i j")
        print("To restart type restart")
        G.printBoardTutorial()
        G.printState()
        inpt = input()
        if inpt == "restart":
            G = Game()
            continue
        inpt = inpt.split(" ")
        if len(inpt) != 3:
            print("Wrong input")
            continue
        r = 0
        if inpt[0] == "W0":
            r = G.moveWolf(0, (int(inpt[1]), int(inpt[2])))
        elif inpt[0] == "W1":
            r = G.moveWolf(1, (int(inpt[1]), int(inpt[2])))
        elif inpt[0] == "W2":
            r = G.moveWolf(2, (int(inpt[1]), int(inpt[2])))
        elif inpt[0] == "H":
            r = G.moveHare((int(inpt[1]), int(inpt[2])))
        if r == -1:
            print("The move is not possible, please choose another move")
        if G.checkWin() == "hare":
            print("Hare Win!")
        if G.checkWin() == "wolf":
            print("Wolves Win!")
def playGUIPVP():
    game = Game()
    interfacePlayPVP(game)

def playWolfPVETerminal(difficulty, algorithm):
    G = Game("hare", difficulty, algorithm)
    while True:
        userStartTime = time.time()
        print("Choose a move from: Wx i j or H i j")
        print("To restart type restart")
        G.printBoardTutorial()
        G.printState()
        inpt = input()
        if inpt == "restart":
            G = Game()
            continue
        inpt = inpt.split(" ")
        if len(inpt) != 3:
            print("Wrong input")
            continue
        r = 0
        if inpt[0] == "W0":
            r = G.moveWolf(0, (int(inpt[1]), int(inpt[2])))
        elif inpt[0] == "W1":
            r = G.moveWolf(1, (int(inpt[1]), int(inpt[2])))
        elif inpt[0] == "W2":
            r = G.moveWolf(2, (int(inpt[1]), int(inpt[2])))
        elif inpt[0] == "H":
            r = G.moveHare((int(inpt[1]), int(inpt[2])))
        if r == -1:
            print("The move is not possible, please choose another move")
        if G.checkWin() == "hare":
            print("Hare Win!")
        if G.checkWin() == "wolf":
            print("Wolves Win!")

        endTime = time.time() - userStartTime
        formattedTime = float("{:.2f}".format(endTime))
        print("User move took: " + str(formattedTime))
        print("Your move:")
        G.printState()
        startTime = time.time()
        G.makeAIMove()
        endTime = time.time() - startTime
        formattedTime = float("{:.2f}".format(endTime))
        print("Computer move took: " + str(formattedTime))
        print("Computer move:")
        G.printState()
        print("Current score: " + str(G.getScore()))
def playWolfPVEGUI(difficulty, algorithm):
    game = Game("hare", difficulty, algorithm)
    interfacePlayPVP(game)
def playHarePVETerminal(difficulty, algorithm):
    G = Game("wolf", difficulty, algorithm)
    while True:
        userStartTime = time.time()
        print("Choose a move from: Wx i j or H i j")
        print("To restart type restart")
        G.printBoardTutorial()
        G.printState()
        inpt = input()
        if inpt == "restart":
            G = Game()
            continue
        inpt = inpt.split(" ")
        if len(inpt) != 3:
            print("Wrong input")
            continue
        r = 0
        if inpt[0] == "W0":
            r = G.moveWolf(0, (int(inpt[1]), int(inpt[2])))
        elif inpt[0] == "W1":
            r = G.moveWolf(1, (int(inpt[1]), int(inpt[2])))
        elif inpt[0] == "W2":
            r = G.moveWolf(2, (int(inpt[1]), int(inpt[2])))
        elif inpt[0] == "H":
            r = G.moveHare((int(inpt[1]), int(inpt[2])))
        if r == -1:
            print("The move is not possible, please choose another move")
        if G.checkWin() == "hare":
            print("Hare Win!")
        if G.checkWin() == "wolf":
            print("Wolves Win!")
        endTime = time.time() - userStartTime
        formattedTime = float("{:.2f}".format(endTime))
        print("User move took: " + str(formattedTime))
        print("Your move:")
        G.printState()
        startTime = time.time()
        G.makeAIMove()
        endTime = time.time() - startTime
        formattedTime = float("{:.2f}".format(endTime))
        print("Computer move took: " + str(formattedTime))
        print("Computer move:")
        G.printState()
        print("Current score: " + str(G.getScore()))

def playHarePVEGUI(difficulty, algorithm):
    game = Game("wolf", difficulty, algorithm)
    interfacePlayPVP(game)


if __name__ == "__main__":
    print("Choose the style you want to play")
    print("1. Terminal")
    print("2. GUI")
    style = int(input())
    print("Choose game mode:")
    print("1. Player vs AI")
    print("2. Player vs Player")
    i = int(input())
    if i == 2:
        if style == 1:
            playTerminalPVP()
        if style == 2:
            playGUIPVP()
    if i == 1:
        print("Choose difficulty")
        print("1. Easy")
        print("2. Medium")
        print("3. Hard")
        difficulty = int(input())
        if difficulty == 1:
            difficulty = "easy"
        elif difficulty == 2:
            difficulty = "medium"
        elif difficulty == 3:
            difficulty = "hard"

        print("Choose what algorithm you want to play against")
        print("1. minimax")
        print("2. minimax alpha beta pruning")
        algorithm = int(input())
        if algorithm == 1:
            algorithm = "minimax"
        else:
            algorithm = "alphabeta"

        print("Choose what side you want to play")
        print("1. Play as Hounds")
        print("2. Play as Hare")
        i2 = int(input())
        if i2 == 1:
            if style == 1:
                playWolfPVETerminal(difficulty, algorithm)
            if style == 2:
                playWolfPVEGUI(difficulty, algorithm)
        if i2 == 2:
            if style == 1:
                playHarePVETerminal(difficulty, algorithm)
            if style == 2:
                playHarePVEGUI(difficulty, algorithm)

