grid = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8,
    1: "a",
    2: "b",
    3: "c",
    4: "d",
    5: "e",
    6: "f",
    7: "g",
    8: "h"
}

def check_position(pieces, to_check):
    colours = ["white", "black"]
    for c in range(0, 2):
        for p in range(0, len(pieces[colours[c]])):
            if(pieces[colours[c]][p].position == to_check):
                return False

class Piece:
    def __init__(self, position, colour, letter):
        self.position = position
        self.colour = colour
        self.letter = letter

class Bishop(Piece):
    def check_valid(self, pieces, coming, going, p):
        x1 = grid[coming[0]]
        x2 = grid[going[0]]
        y1 = int(coming[1])
        y2 = int(going[1])
        x_dist = abs(x2-x1)
        y_dist = abs(y2-y1)
        inc_x = int((x2-x1)/(x1-x2))
        inc_y = int(-((y2-y1)/(y1-y2)))
        if(x_dist == y_dist):
            for y in range(y1, y2, inc_y):
                for x in range(x1, x2, inc_x):
                    valid = check_position(pieces, grid[x] + str(y))
                    print(valid)
                    if(valid == False):
                        return False
            return True
            
        # Code to check if the piece's movement is valid
    
    def move_to(self, going):
        self.position = going
        # Code to move to the given point on the grid

class Knight(Piece):
    def check_valid(self, pieces, coming, going, p):
        x1 = grid[coming[0]]
        x2 = grid[going[0]]
        y1 = int(coming[1])
        y2 = int(going[1])
        x_dist = abs(x2-x1)
        y_dist = abs(y2-y1)
        if(x_dist == 1 and y_dist == 2):
            return True
        elif(x_dist == 2 and y_dist == 1):
            return True
        else:
            return False
        # Code to check if the piece's movement is valid
    
    def move_to(self, going):
        self.position = going
        # Code to move to the given point on the grid

class Rook(Piece):
    def check_valid(self, pieces, coming, going, p):
        x1 = grid[coming[0]]
        x2 = grid[going[0]]
        y1 = int(coming[1])
        y2 = int(going[1])
        x_dist = abs(x2-x1)
        y_dist = abs(y2-y1)
        inc_x = int((x2-x1)/(x1-x2))
        inc_y = int(-((y2-y1)/(y1-y2)))
        if(x_dist == 0 and y_dist != 0):
            for y in range(y1, y2, inc_y):
                valid = check_position(pieces, grid[y] + x1)
                if(valid == False):
                    return False
            return True
        elif(y_dist == 0 and x_dist != 0):
            for x in range(x1, x2, inc_x):
                valid = check_position(pieces, grid[x] + y1)
                if(valid == False):
                    return False
            return True
        else:
            return False
        # Code to check if the piece's movement is valid
    
    def move_to(self, going):
        self.position = going
        # Code to move to the given point on the grid

class Queen(Piece):
    def check_valid(self, pieces, coming, going, p):
        x1 = grid[coming[0]]
        x2 = grid[going[0]]
        y1 = int(coming[1])
        y2 = int(going[1])
        x_dist = abs(x2-x1)
        y_dist = abs(y2-y1)
        inc_x = int((x2-x1)/(x1-x2))
        inc_y = int(-((y2-y1)/(y1-y2)))
        if(x_dist == y_dist):
            for y in range(y1, y2, inc_y):
                for x in range(x1, x2, inc_x):
                    valid = check_position(pieces, grid[x] + str(y))
                    print(valid)
                    if(valid == False):
                        return False
        elif(x_dist == 0 and y_dist != 0):
            for y in range(y1, y2, inc_y):
                valid = check_position(pieces, grid[y] + x1)
                if(valid == False):
                    return False
            return True
        elif(y_dist == 0 and x_dist != 0):
            for x in range(x1, x2, inc_x):
                valid = check_position(pieces, grid[x] + y1)
                if(valid == False):
                    return False
            return True
        else:
            return False
        # Code to check if the piece's movement is valid
    
    def move_to(self, going):
        self.position = going
        # Code to move to the given point on the grid

class King(Piece):
    def check_valid(self, pieces, coming, going, p):
        x1 = grid[coming[0]]
        x2 = grid[going[0]]
        y1 = int(coming[1])
        y2 = int(going[1])
        x_dist = abs(x2-x1)
        y_dist = abs(y2-y1)
        if(x_dist == y_dist and x_dist == 1):
            return True
        elif(x_dist == 0 and y_dist == 1):
            return True
        elif(y_dist == 0 and x_dist == 1):
            return True
        else:
            return False
        # Code to check if the piece's movement is valid
    
    def move_to(self, going):
        self.position = going
        # Code to move to the given point on the grid

class Pawn(Piece):
    def __init__(self, position, colour, letter):
        Piece.__init__(self, position, colour, letter)
        self.hasMoved = False

    def check_valid(self, pieces, coming, going, is_piece):
        self.x1 = grid[coming[0]]
        self.x2 = grid[going[0]]
        self.y1 = int(coming[1])
        self.y2 = int(going[1])
        self.x_dist = abs(self.x2-self.x1)
        self.y_dist = abs(self.y2-self.y1)
        if(is_piece == "#"):
            if(self.hasMoved == False):
                self.hasMoved = True
                if(self.x_dist == 0 and self.y_dist == 2):
                    return True
                elif(self.x_dist == 0 and self.y_dist == 1):
                    return True
            elif(self.hasMoved == True):
                if(self.x_dist == 0 and self.y_dist == 1):
                    return True
        else:
            self.hasMoved = False
            self.x3 = grid[is_piece[0]]
            self.y3 = int(is_piece[1])
            self.x2_dist = abs(self.x3-self.x1)
            self.y2_dist = abs(self.y3-self.y1)
            if(self.x2_dist == self.y2_dist == 1):
                return True
        return False


    def move_to(self, going):
        self.position = going
