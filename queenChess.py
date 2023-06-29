import modules as m



def main():
    for i in range(1000):

        obj = m.QueenPositions()
        obj.initSets()
        j = 0
        obj.putFirstQueen()
        j = 1
        obj.findNewPositions(j)
        j = 2
        obj.findNewPositions(j)
        j = 3
        
        # print(obj.chessBoard)
        obj.findNewPositions(j)
        j = 4
        # obj.queensPosition.append('c6')
        obj.findNewPositions(j)
        obj.findNewPositions()
        obj.findNewPositions()
        obj.findNewPositions()
        # for i in range(len(obj.chessBoardForMoving)):
        #     print(obj.chessBoardForMoving[i])
        if obj.queensPosition[7] != 'h8':
            print(i)
            print(obj.queensPosition)
            break

        # print(obj.queensPosition)

if __name__ == '__main__':
    main()