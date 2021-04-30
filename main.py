from os import system
import random
from classes.pieces import *
from time import sleep
import re

def grid_pieces(grid, x, y):
    x += 1
    pieces = "abcdefgh"
    colours = ["white", "black"]
    for c in range(0, 2): # Is the colour of the grid data structure (white / black)
        for p in range(len(grid[colours[c]]), 0, -1):
            piece = grid[colours[c]][p-1]
            comp_pos = pieces[y] + str(x)
            if(piece.position == comp_pos):
                return piece.letter
    return "#"

def get_object(grid, coord):
    pieces = "abcdefgh"
    colours = ["white", "black"]
    for c in range(0, 2): # Is the colour of the grid data structure (white / black)
        for p in range(0, len(grid[colours[c]])):
            piece = grid[colours[c]][p]
            if(piece.position == coord):
                return piece
    return "#"

def get_index(grid, piece):
    colours = ["white", "black"]
    for c in range(0, 2): # Is the colour of the grid data structure (white / black)
        for p in range(0, len(grid[colours[c]])):
            piece_2 = grid[colours[c]][p]
            if(piece == piece_2):
                return p

def print_grid(grid):
    pieces = "abcdefgh"
    colours = ["white", "black"]
    for row in range(7, -1, -1):
        print(row+1, end=' | ')
        for column in range(0, 8): # Sets up printing an 8*8 board
            piece = grid_pieces(grid, row, column)
            print(piece, end='')
        print()
    print("    --------")
    print("    ABCDEFGH")

def check_validity(grid, move, colour):
    valid = "^[a-h][1-8][a-gh][1-8]$"
    move = move[0:4]
    if(move[0:2] == move[2:4]):
        return False
    check = re.findall(valid, move)
    if(check[0] == move):
        piece = get_object(grid, move[0:2])
        if(piece == "#"):
            return False
        if(piece.colour == colour):
            piece_2 = get_object(grid, move[2:4])
            if(piece_2 != "#"):
                is_valid = piece.check_valid(grid, move[0:2], move[2:4], piece_2.position)
            else:
                is_valid = piece.check_valid(grid, move[0:2], move[2:4], "#")
            if(is_valid == False):
                return False
            else:
                return True
    return False

def get_input(grid, colour):
    valid = False
    move = input("Enter your move (starting and ending coords, a2a4 for example)\n\t")
    move = move.lower()
    valid = check_validity(grid, move, colour)
    while(valid == False):
        move = input("Please enter a valid move.\n\n\t")
        valid = check_validity(grid, move, colour)
    return move

def check_for_winner(grid):
    # Checking to see if each king exists. If one doesn't then we end the game
    # And say that player n wins
    # ai ai ai
    colours = ["white", "black"]
    for c in range(0, 2): # Is the colour of the grid data structure (white / black)
        letters = []
        for p in range(0, len(grid[colours[c]])):
            piece = grid[colours[c]][p]
            letters.append(piece.letter.lower())
        if("k" not in letters):
            return colours[(c+1)%2] + " is the winner"
    return False

def print_moves(moves):
    colours = ["white", "black"]
    for c in range(0, 2):
        for m in range(0, len(moves[colours[c]])):
            print(colours[c], ": ", moves[colours[c]][m])

def promote_piece(grid, piece): 
    valid_pieces = ["queen", "bishop", "knight", "rook"]
    valid = False
    upgrade = input("Would you like to promote to Queen, Rook, Knight or Bishop\n\t").lower()
    if(upgrade in valid_pieces):
        valid = True
    if(upgrade != "knight"):
        letter = upgrade[0].upper()
    else:
        letter = "N"
    while(valid == False):
            upgrade = input("Please enter a valid input.\n\t").lower()
            if(upgrade in valid_pieces):
                valid = True
            else:
                valid = False
    if(piece.colour == "black"):
        letter = letter.upper()
    if(upgrade == "queen"):
        valid = True
        grid[piece.colour].append(Queen(piece.position, piece.colour, letter))
    elif(upgrade == "rook"):
        valid = True
        grid[piece.colour].append(Rook(piece.position, piece.colour, letter))
    elif(upgrade == "knight"):
        valid = True
        grid[piece.colour].append(Knight(piece.position, piece.colour, letter))
    elif(upgrade == "bishop"):
        valid = True
        grid[piece.colour].append(Bishop(piece.position, piece.colour, letter))
    position = get_index(grid, piece)
    grid[piece.colour].pop(position)

def game():
    while(1):
        pieces = {
            "white": [
                Pawn("a2", "white", "P"),
                Pawn("b2", "white", "P"),
                Pawn("c2", "white", "P"),
                Pawn("d2", "white", "P"),
                Pawn("e2", "white", "P"),
                Pawn("f2", "white", "P"),
                Pawn("g2", "white", "P"),
                Pawn("h2", "white", "P"),
                Knight("b1", "white", "N"),
                Knight("g1", "white", "N"),
                Bishop("c1", "white", "B"),
                Bishop("f1", "white", "B"),
                Rook("a1", "white", "R"),
                Rook("h1", "white", "R"),
                Queen("d1", "white", "Q"),
                King("e1", "white", "K")
            ],
            "black": [
                Pawn("a7", "black", "p"),
                Pawn("b7", "black", "p"),
                Pawn("c7", "black", "p"),
                Pawn("d7", "black", "p"),
                Pawn("e7", "black", "p"),
                Pawn("f7", "black", "p"),
                Pawn("g7", "black", "p"),
                Pawn("h7", "black", "p"),
                Knight("b8", "black", "n"),
                Knight("g8", "black", "n"),
                Bishop("f8", "black", "b"),
                Bishop("c8", "black", "b"),
                Rook("a8", "black", "r"),
                Rook("h8", "black", "r"),
                Queen("d8", "black", "q"),
                King("e8", "black", "k")
            ]
        }
        turns = ["white", "black"]
        turn = 0
        winner = False
        previous_moves = {
            "white": [],
            "black": []
        }
        while(winner == False):
            player = turns[turn%2]
            try:
                system("CLS")
            except:
                system("Clear")
            print_grid(pieces)
            print("It is " + player + "'s turn.")
            user_input = get_input(pieces, player)
            prev_moves = input("Would you like to see the previous moves? (y/yes)\n\t").lower()
            if(prev_moves == "y" or prev_moves == "yes"):
                print_moves(previous_moves)
                input("Press enter to continue")
            previous_moves[player].append(user_input)
            piece = get_object(pieces, user_input[0:2])
            piece_2 = get_object(pieces, user_input[2:4])
            if(piece_2 != "#"):
                index = get_index(pieces, piece_2)
                colour = piece_2.colour
                pieces[colour].pop(index)
            piece.move_to(user_input[2:4])
            if((piece.letter.lower() == "p") and (piece.position[1] == "1" or piece.position[1] == "8")):
                promote_piece(pieces, piece)
            winner = check_for_winner(pieces)
            turn += 1
        print(winner)
        sleep(5)

game()