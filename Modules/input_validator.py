

def validate_move(board,move):
    try:
        if move["status"] == "problem":
            return {"status":"problem","output":"Input is not in expected format"}
    except:         
        x = move[0]
        y = move[1]
        if not (x in [0,1,2]) or not (y in [0,1,2]):
            return {"status":"problem","output":"Specified coordinate is not in range"}
        try:
            if board[x][y] != "":
                return {"status":"problem","output":"Specified move is overlapping an existing symbol"}
            else:
                return {"status":"valid","output":"N/A"}
        except:
                return {"status":"problem","output":"Space does not exist on board"}

def checkForFullBoard(board):
    for row in board:
        for item in row:
            if item == "":
                return {"status":"continue"}
    
    return {"status":"problem","output":"Game board full - nobody wins."}

def checkForWin(board,symbols,winDiags):
    
    # horizontal wins
    for row in board:
        for symbol in ["O","X"]:
            if row.count(symbol) == 3:
                return {"status":"win","winner":symbol}
    
    # vertical wins
    rowlist = []
    for symbol in ["O","X"]:
        for i in [0,1,2]:
            for row in board:
                rowlist.append(row[i])
            if rowlist.count(symbol) == 3:
                    return {"status":"win","winner":symbol}
                    
            rowlist.clear()
    
    for symbol in ["O","X"]:
        for pattern in winDiags:
            matchedCoordinates = []
            for coordinate in pattern:
                x = coordinate[0] -1
                y = coordinate[1] -1
                if board[x][y] == symbol:
                    matchedCoordinates.append(coordinate)
                
            if len(matchedCoordinates) == 3:
                return {"status":"win","winner":symbol}

            

    return {"status":"no_win"}