class Leaf:
    def __init__(self):
        self.id = None
        self.x = None
        self.y = None
        self.insects = None
        self.maxWeight = None

    def readLeaf(self, line):
        line = line.split(" ")
        self.id = line[0]
        self.x = line[1]
        self.y = line[2]
        self.insects = line[3]
        self.maxWeight = line[4]

    def __repr__(self):
        return " id: " + self.id + " x: "+ self.x + " y: " + self.y + " insects: " + self.insects + " maxWeight: " + self.maxWeight

    def __str__(self):
        return " id: " + self.id + " x: "+ self.x + " y: " + self.y + " insects: " + self.insects + " maxWeight: " + self.maxWeight
class Board:
    def __init__(self, fileName):
        self.board = []
        with open(fileName, "r") as f:
            self.radius = int(f.readline())
            self.wieight = int(f.readline())
            self.startLeaf = f.readline()

            for line in f:
                leaf = Leaf()
                leaf.readLeaf(line)
                self.board.append(leaf)
    def print(self):
        print(self.board)


fileNames = ["input1.txt", "input2.txt", "input3.txt", "input4.txt"]
b = Board(fileNames[0])
b.print()
