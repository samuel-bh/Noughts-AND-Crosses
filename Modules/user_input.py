
def get_user_name(playerNum,prompt):
    # get and return username, formatting the prompt
    inp = input(prompt.format(plrNo=playerNum))
    return inp

def get_next_move(playerObj,prompt):
    # return next move in code-friendly format
    playerName = playerObj["name"]
    playerSymbol = playerObj["symbol"]
    inp = input(prompt.format(plrName=playerName,symbol=playerSymbol))

    if len(inp) != 3:
        return {"status":"problem"}

    try:
        if not inp[1] == ",":
            return {"status":"problem"}
        return (int(inp[2])-1, int(inp[0])-1,)
    except:
        return {"status":"problem"}