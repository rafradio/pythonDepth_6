import modules as m



def main():
    arr = ['a5', 'b3', 'c1', 'd6', 'e8', 'f2', 'g4', 'h7']
    obj = m.QueenPositionsTaken(arr)
    obj.initSets()
    obj.putAllQueens()
    obj.findSolution()
    

if __name__ == '__main__':
    main()