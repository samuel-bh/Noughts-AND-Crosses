
class colour:
    NOUGHT = '\033[94m'
    CROSS = '\033[92m'
    END = '\033[0m'

def neaten_symbol(r):
    if r == "":
        return " "
    else:
        if r == "X":
            return colour.CROSS + r + colour.END
        else:
            return colour.NOUGHT + r + colour.END

def draw_board_line(b, row):


    print(' ' + neaten_symbol(b[row][0]), end="")
    print(' | ' + neaten_symbol(b[row][1]) + ' | ' + neaten_symbol(b[row][2]))

def draw_separator():
    print('-'*13)

def draw_board(b):
    print("\n")
    print("   1   2   3")
    print("1 ",end="")
    draw_board_line(b,0)
    print("  ⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯")
    print("2 ",end="")    
    draw_board_line(b,1)
    print("  ⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯")
    print("3 ",end="")
    draw_board_line(b,2)
    print("\n")

