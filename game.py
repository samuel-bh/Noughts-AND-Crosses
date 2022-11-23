# imports
import json
from random import choice

import Modules.user_input as usr_input
from Modules.output import draw_board
import Modules.input_validator as inp_validator

# open game config file
with open("gameData.json","r") as data:
    config = json.load(data)

# output friendly welcome messages
print(config["prompts"]["welcomeMsg"])
print(config["prompts"]["setupMsg"])

# declare symbols
symbols = ["X","O"]
# import empty board
board = config["boardData"]

# get usernames (for UX)
config["players"]["player1"]["name"] = usr_input.get_user_name("Player 1",config["prompts"]["playerNumber"])
config["players"]["player2"]["name"] = usr_input.get_user_name("Player 2",config["prompts"]["playerNumber"])

# choose which player is going to play next

plr1_symbol = choice(symbols)
symbols.remove(plr1_symbol)
# set player symbol in config
config["players"]["player1"]["symbol"] = plr1_symbol
config["players"]["player2"]["symbol"] = symbols[0]

# draw line to clearly separate instructions from game
print("\n" + "-"*20 + "\n")

# start message & set game as running
print(config["prompts"]["gameStartMsg"])
config["gameRunning"] = True

draw_board(board)

# while game hasn't been won
switchPlay = False
while config["gameRunning"] == True:
    for player in config["players"]:
        if switchPlay:
            switchPlay = False
            continue
        
        switchPlay = False

        # check again that the game isn't running to account for delay
        if not config["gameRunning"]: continue
        player = config["players"][player]
        # get users next move
        move = usr_input.get_next_move(player,config["prompts"]["addrPrompt"])
        validation = inp_validator.validate_move(board,move)

        # if problem with validation, output the problem
        if validation["status"] == "problem":
            print(validation["output"])
            # ignore the rest of the instructions
            switchPlay = True
            continue

        # set the player move on the board
        board[move[0]][move[1]] = player["symbol"]

        draw_board(board)

        # check if theres a win on the board
        win_check = inp_validator.checkForWin(board,symbols,config["diagWins"])
        # if win, go through all of the celebration stuff        
        if win_check["status"] == "win":
            winner_name = player["name"]
            winsymbol = win_check["winner"]
            print(config["prompts"]["gameWinMsg"].format(symbol=winsymbol))
            draw_board(board)

            # end loop, game is over
            config["gameRunning"] = False
            break
        
        # check if board is full
        board_full = inp_validator.checkForFullBoard(board)
        if board_full["status"] == "problem":
            # output problem and stop game - tie
            print(board_full["output"])
            config["gameRunning"] = False
            
