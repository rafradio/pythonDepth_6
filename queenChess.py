import modules as m



def main():
    for i in range(1000):

        obj = m.QueenPositions()
        obj.initSets()
        obj.putFirstQueen()
        for _ in range(7): obj.findNewPositions()
        if obj.queensPosition[7] != 'a1':
            print(i)
            print(obj.queensPosition)
            break


if __name__ == '__main__':
    main()