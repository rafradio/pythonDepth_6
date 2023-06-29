import sys
import modules as m
# from modules.calendar_1 import *

def main(args):
    data = args[1] if len(args) > 1 else m.takeData()
    print(m.checkData(data))

if __name__ == '__main__':
    main(sys.argv)