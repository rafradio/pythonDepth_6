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
        # i = 5
        # j = 0
        self.chessBoard[self.chessBoardForMoving[i][j]] = 'Queen'
        self.queensPosition.append(self.chessBoardForMoving[i][j])

    def findNewPositions(self, j = 10):
        initHorizont = 0
        initVert = 0
        possibleTOPut = False
        queenPos = ""
        while (initHorizont < 8):
            while (initVert < 8):
                queenPos = self.chessBoardForMoving[initHorizont][initVert]

                if self.chessBoard[queenPos] != 'Queen':
                    possibleTOPut = self.checkHorizont(queenPos, initVert)

                    if (possibleTOPut): possibleTOPut = self.checkVertical(queenPos, initHorizont)

                    if (possibleTOPut): possibleTOPut = self.checkDiagonals(initHorizont, initVert)

                else: possibleTOPut = False

                if (possibleTOPut): break
                initVert += 1
            
            if (possibleTOPut): break
            initVert = 0
            initHorizont += 1
        
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
        
        checkFlag = True
        coordinates = list()
        for i in range(8):
            coordinates.append((vert+i, horisont+i))
            coordinates.append((vert-i, horisont-i))
            coordinates.append((vert+i, horisont-i))
            coordinates.append((vert-i, horisont+i))

        arr = filter(lambda x: -1 < x[0] < 8 and  -1 < x[1] < 8, coordinates)
        arr1 = list(filter(lambda x: self.chessBoard[self.chessBoardForMoving[x[0]][x[1]]] == 'Queen', arr))

        return (len(arr1) == 0)
        for i in range(8):
            if (vert+i) < 8 and (horisont+i) < 8: 
                checkPos = self.chessBoardForMoving[vert+i][horisont+i]
                # if checkPos1 == 'c6': print(self.chessBoard[checkPos], ' ', checkPos)
                if (self.chessBoard[checkPos] == "Queen"):
                    checkFlag = False
                    break

            # try: 
            #     checkPos = self.chessBoardForMoving[vert+i][horisont+i]
            #     if checkPos1 == 'c6': print(self.chessBoard[checkPos], ' ', checkPos)
            #     if (self.chessBoard[checkPos] == "Queen"):
            #         checkFlag = False
            #         break
            # except: pass

            if (vert-i) > -1 and (horisont-i) > -1: 
                checkPos = self.chessBoardForMoving[vert-i][horisont-i]
                # if checkPos1 == 'c6': print(self.chessBoard[checkPos], ' ', checkPos)
                if (self.chessBoard[checkPos] == "Queen"):
                    checkFlag = False
                    break

            # try: 
            #     checkPos = self.chessBoardForMoving[vert-i][horisont-i]
            #     if checkPos1 == 'c6': print(self.chessBoard[checkPos], ' ', checkPos)
            #     if (self.chessBoard[checkPos] == "Queen"):
            #         checkFlag = False
            #         break
            # except: pass

            if (vert-i) > -1 and (horisont+i) < 8: 
                checkPos = self.chessBoardForMoving[vert-i][horisont+i]
                # if checkPos1 == 'c6': print(self.chessBoard[checkPos], ' ', checkPos)
                if (self.chessBoard[checkPos] == "Queen"):
                    checkFlag = False
                    break

            # try: 
            #     checkPos = self.chessBoardForMoving[vert-i][horisont+i]
            #     if checkPos1 == 'c6': print(self.chessBoard[checkPos], ' ', checkPos)
            #     if (self.chessBoard[checkPos] == "Queen"):
            #         checkFlag = False
            #         break
            # except: pass

            if (vert+i) < 8 and (horisont-i) > -1: 
                checkPos = self.chessBoardForMoving[vert+i][horisont-i]
                # if checkPos1 == 'c6': print(self.chessBoard[checkPos], ' ', checkPos)
                if (self.chessBoard[checkPos] == "Queen"):
                    checkFlag = False
                    break
            # try: 
            #     checkPos = self.chessBoardForMoving[vert+i][horisont-i]
            #     if checkPos1 == 'c6': print(self.chessBoard[checkPos], ' ', checkPos)
            #     if (self.chessBoard[checkPos] == "Queen"):
            #         checkFlag = False
            #         break
            # except: pass

        return checkFlag

            
                

    