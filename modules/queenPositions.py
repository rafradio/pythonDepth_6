import random

class QueenPositions:
    def __init__(self):
        self.chessBoard = {}
        self.chessBoardForMoving = []
        self.queensPosition = list()

    def initSets(self):
        horizont: str = ["a", "b", "c", "d", "e", "f", "g", "h"]
        for i in range(len(horizont)):
            arr = list()
            for j in range(1,9):
                key: str = horizont[i] + str(j)
                self.chessBoard[key] = "Empty"
                arr.append(key)

            self.chessBoardForMoving.append(arr)

    def putFirstQueen(self):
        i = random.randint(0, 7)
        j = random.randint(0, 7)
        self.chessBoard[self.chessBoardForMoving[i][j]] = 'Queen'
        self.queensPosition.append(self.chessBoardForMoving[i][j])

    def findNewPositions(self):
        initHorizont = 7
        initVert = 7
        possibleTOPut = False
        queenPos = ""
        while (initHorizont > -1):
            while (initVert > -1):
                queenPos = self.chessBoardForMoving[initHorizont][initVert]

                if self.chessBoard[queenPos] != 'Queen':
                    possibleTOPut = self.checkHorizont(queenPos, initVert)
                    if (possibleTOPut): possibleTOPut = self.checkVertical(queenPos, initHorizont)
                    if (possibleTOPut): possibleTOPut = self.checkDiagonals(initHorizont, initVert)

                if (possibleTOPut): break
                initVert -= 1
            
            if (possibleTOPut): break
            initVert = 7
            initHorizont -= 1
        
        self.chessBoard[queenPos] = "Queen"
        self.queensPosition.append(queenPos)


    def checkHorizont(self, pos: str, vert: int):
        keyLambda = lambda x: self.chessBoardForMoving[x][vert]
        arr = list(filter(lambda x: x == "Queen", [self.chessBoard[keyLambda(i)] for i in range(8)]))

        return (len(arr) == 0)

    
    def checkVertical(self, pos: str, horisont: int):
        keyLambda = lambda x: self.chessBoardForMoving[horisont][x]
        arr = list(filter(lambda x: x == "Queen", [self.chessBoard[keyLambda(i)] for i in range(8)]))

        return (len(arr) == 0)

    
    def checkDiagonals(self, vert: int, horisont: int):
        coordinates = list()
        for i in range(8):
            coordinates.append((vert+i, horisont+i))
            coordinates.append((vert-i, horisont-i))
            coordinates.append((vert+i, horisont-i))
            coordinates.append((vert-i, horisont+i))

        arr = filter(lambda x: -1 < x[0] < 8 and  -1 < x[1] < 8, coordinates)
        arr1 = list(filter(lambda x: self.chessBoard[self.chessBoardForMoving[x[0]][x[1]]] == 'Queen', arr))

        return (len(arr1) == 0)

            
                

    