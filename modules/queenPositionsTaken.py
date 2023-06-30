import random

class QueenPositionsTaken:
    def __init__(self, arr):
        self.chessBoard = {}
        self.chessBoardForMoving = []
        self.queensPosition = arr

    def initSets(self):
        horizont: str = ["a", "b", "c", "d", "e", "f", "g", "h"]
        for i in range(len(horizont)):
            arr = list()
            for j in range(1,9):
                key: str = horizont[i] + str(j)
                self.chessBoard[key] = "Empty"
                arr.append(key)

            self.chessBoardForMoving.append(arr)

    def putAllQueens(self):
        for i in range(len(self.queensPosition)): 
            self.chessBoard[self.queensPosition[i]] = 'Queen'


    def myFunc(self, x):
        
        self.chessBoard[x] = "Empty"
        horizont = ["a", "b", "c", "d", "e", "f", "g", "h"]
        vert = horizont.index(x[0])
        horiz = int(x[1]) - 1
        # print(x, vert, horiz)
        possibleTOPut = self.checkHorizont(horiz)
        if (possibleTOPut): possibleTOPut = self.checkVertical(vert)
        if (possibleTOPut): possibleTOPut = self.checkDiagonals(vert, horiz)
        self.chessBoard[x] = "Queen"
        return possibleTOPut

    def findSolution(self):

        arr = list(map(self.myFunc, self.queensPosition))
        result = list(filter(lambda x: x, arr))
        print(len(result) == 8)


    def checkHorizont(self, vert: int):
        keyLambda = lambda x: self.chessBoardForMoving[x][vert]
        arr = list(filter(lambda x: x == "Queen", [self.chessBoard[keyLambda(i)] for i in range(8)]))

        return (len(arr) == 0)

    
    def checkVertical(self, horisont: int):
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

            
                

    