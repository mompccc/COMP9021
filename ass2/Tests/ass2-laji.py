import re
import sys
def read_grid():
    grid = []
    with open(input('enter the file name:')) as file:
        for line in file:
            grid_line = re.findall(r'\d',line)
            if grid_line != []:
                grid.append(grid_line)
    return grid

grid = read_grid()
N1 = len(grid)
N2 = len(grid[0])

def display():
    for i in range(0,N1):
        for j in range(0,N2):
           grid[i][j] = int(grid[i][j])
           print(grid[i][j], end = '  ')
        print()

def colour_shapes():
    colour = 1
    for i in range(0,N1):
        for j in range(0,N2):
            if grid[i][j] == 1:
                colour += 1
                find_shapes(i,j,i,j,i,j,colour)

def find_shapes(X,Y,X0,Y0,X1,Y1,colour):
    if X == X1 and Y == Y1:
        if X - 1 >= 0 and grid[X - 1][Y] == 1:
            X1 = X
            Y1 = Y
            grid[X - 1][Y] = colour
            return find_shapes(X - 1,Y,X0,Y0,X1,Y1,colour)
        elif X - 1 >= 0 and Y + 1 <= N2 - 1 and grid[X - 1][Y + 1] == 1:
            X1 = X
            Y1 = Y
            grid[X - 1][Y + 1] = colour
            return find_shapes(X - 1,Y + 1,X0,Y0,X1,Y1,colour) 
        elif Y + 1 <= N2 - 1 and grid[X][Y + 1] == 1:
            X1 = X
            Y1 = Y
            grid[X][Y + 1] = colour
            return find_shapes(X,Y + 1,X0,Y0,X1,Y1,colour)
        elif X + 1 <= N1 - 1 and Y + 1 <= N2 - 1 and grid[X + 1][Y + 1] == 1:
            X1 = X
            Y1 = Y
            grid[X + 1][Y + 1] = colour
            return find_shapes(X + 1,Y + 1,X0,Y0,X1,Y1,colour)
        elif X + 1 <= N1 - 1 and grid[X + 1][Y] == 1:
            X1 = X
            Y1 = Y
            grid[X + 1][Y] = colour
            return find_shapes(X + 1,Y,X0,Y0,X1,Y1,colour)
        elif Y - 1 >= 0 and X + 1 <= N1 - 1 and grid[X + 1][Y - 1] == 1:
            X1 = X 
            Y1 = Y
            grid[X + 1][Y - 1] = colour
            return find_shapes(X + 1,Y - 1,X0,Y0,X1,Y1,colour)
        elif Y - 1 >= 0 and grid[X][Y - 1] == 1:
            X1 = X 
            Y1 = Y
            grid[X][Y - 1] = colour
            return find_shapes(X,Y - 1,X0,Y0,X1,Y1,colour)
        elif X - 1 >= 0 and Y - 1 >= 0 and grid[X - 1][Y - 1] == 1:
            X1 = X
            Y1 = Y
            grid[X - 1][Y - 1] = colour
            return find_shapes(X - 1,Y - 1,X0,Y0,X1,Y1,colour)
        
    ## SE
    if X > X1 and Y > Y1:
        if X - 1 >= 0 and grid[X - 1][Y] == 1:
            if X - 1 == X0 and Y == Y0:
                grid[X0][Y0] = colour
                return 
            X1 = X
            Y1 = Y
            grid[X - 1][Y] = colour
            return find_shapes(X - 1,Y,X0,Y0,X1,Y1,colour)
        elif X - 1 >= 0 and Y + 1 <= N2 - 1 and grid[X - 1][Y + 1] == 1:
            if X - 1 == X0 and Y + 1 == Y0:
                grid[X0][Y0] = colour
                return 
            X1 = X
            Y1 = Y
            grid[X - 1][Y + 1] = colour
            return find_shapes(X - 1,Y + 1,X0,Y0,X1,Y1,colour) 
        elif Y + 1 <= N2 - 1 and grid[X][Y + 1] == 1:
            if X == X0 and Y + 1 == Y0:
                grid[X0][Y0] = colour
                return 
            X1 = X
            Y1 = Y
            grid[X][Y + 1] = colour
            return find_shapes(X,Y + 1,X0,Y0,X1,Y1,colour)
        elif X + 1 <= N1 - 1 and Y + 1 <= N2 - 1 and grid[X + 1][Y + 1] == 1:
            if X + 1 == X0 and Y + 1 == Y0:
                grid[X0][Y0] = colour
                return 
            X1 = X
            Y1 = Y
            grid[X + 1][Y + 1] = colour
            return find_shapes(X + 1,Y + 1,X0,Y0,X1,Y1,colour)
        elif X + 1 <= N1 - 1 and grid[X + 1][Y] == 1:
            if X + 1 == X0 and Y == Y0:
                grid[X0][Y0] = colour
                return 
            X1 = X
            Y1 = Y
            grid[X + 1][Y] = colour
            return find_shapes(X + 1,Y,X0,Y0,X1,Y1,colour)
        elif Y - 1 >= 0 and X + 1 <= N1 - 1 and grid[X + 1][Y - 1] == 1:
            if Y - 1 == Y0 and X + 1 == X0:
                grid[X0][Y0] = colour
                return 
            X1 = X 
            Y1 = Y
            grid[X + 1][Y - 1] = colour
            return find_shapes(X + 1,Y - 1,X0,Y0,X1,Y1,colour)
        elif Y - 1 >= 0 and grid[X][Y - 1] == 1:
            if X == X0 and Y - 1 == Y0:
                grid[X0][Y0] = colour
                return 
            X1 = X 
            Y1 = Y
            grid[X][Y - 1] = colour
            return find_shapes(X,Y - 1,X0,Y0,X1,Y1,colour) 
        else:
            return find_shapes(X1,Y1,X0,Y0,X1,Y1,colour)
            
    
    ## S
    if X > X1 and Y == Y1:
        if X - 1 >= 0 and Y + 1 <= N2 - 1 and grid[X - 1][Y + 1] == 1:
            if X - 1 == X0 and Y + 1 == Y0:
                grid[X0][Y0] = colour
                return 
            X1 = X
            Y1 = Y
            grid[X - 1][Y + 1] = colour
            return find_shapes(X - 1,Y + 1,X0,Y0,X1,Y1,colour) 
        elif Y + 1 <= N2 - 1 and grid[X][Y + 1] == 1:
            if X == X0 and Y + 1 == Y0:
                grid[X0][Y0] = colour
                return 
            X1 = X
            Y1 = Y
            grid[X][Y + 1] = colour
            return find_shapes(X,Y + 1,X0,Y0,X1,Y1,colour)
        elif X + 1 <= N1 - 1 and Y + 1 <= N2 - 1 and grid[X + 1][Y + 1] == 1:
            if X + 1 == X0 and Y + 1 == Y0:
                grid[X0][Y0] = colour
                return 
            X1 = X
            Y1 = Y
            grid[X + 1][Y + 1] = colour
            return find_shapes(X + 1,Y + 1,X0,Y0,X1,Y1,colour)
        elif X + 1 <= N1 - 1 and grid[X + 1][Y] == 1:
            if X + 1 == X0 and Y == Y0:
                grid[X0][Y0] = colour
                return 
            X1 = X
            Y1 = Y
            grid[X + 1][Y] = colour
            return find_shapes(X + 1,Y,X0,Y0,X1,Y1,colour)
        elif Y - 1 >= 0 and X + 1 <= N1 - 1 and grid[X + 1][Y - 1] == 1:
            if Y - 1 == Y0 and X + 1 == X0:
                grid[X0][Y0] = colour
                return 
            X1 = X 
            Y1 = Y
            grid[X + 1][Y - 1] = colour
            return find_shapes(X + 1,Y - 1,X0,Y0,X1,Y1,colour)
        elif Y - 1 >= 0 and grid[X][Y - 1] == 1:
            if X == X0 and Y - 1 == Y0:
                grid[X0][Y0] = colour
                return 
            X1 = X 
            Y1 = Y
            grid[X][Y - 1] = colour
            return find_shapes(X,Y - 1,X0,Y0,X1,Y1,colour)
        elif X - 1 >= 0 and Y - 1 >= 0 and grid[X - 1][Y] == 1:
            if X - 1 == X0 and Y - 1 == Y0:
                grid[X0][Y0] = colour
                return 
            X1 = X
            Y1 = Y
            grid[X - 1][Y - 1] = colour
            return find_shapes(X - 1,Y - 1,X0,Y0,X1,Y1,colour)
        else:
            return find_shapes(X1,Y1,X0,Y0,X1,Y1,colour)
            

    ## SW
    if X > X1 and Y < Y1:
        if Y + 1 <= N2 - 1 and grid[X][Y + 1] == 1:
            if X == X0 and Y + 1 == Y0:
                grid[X0][Y0] = colour
                return 
            X1 = X
            Y1 = Y
            grid[X][Y + 1] = colour
            return find_shapes(X,Y + 1,X0,Y0,X1,Y1,colour)
        elif X + 1 <= N1 - 1 and Y + 1 <= N2 - 1 and grid[X + 1][Y + 1] == 1:
            if X + 1 == X0 and Y + 1 == Y0:
                grid[X0][Y0] = colour
                return 
            X1 = X
            Y1 = Y
            grid[X + 1][Y + 1] = colour
            return find_shapes(X + 1,Y + 1,X0,Y0,X1,Y1,colour)
        elif X + 1 <= N1 - 1 and grid[X + 1][Y] == 1:
            if X + 1 == X0 and Y == Y0:
                grid[X0][Y0] = colour
                return 
            X1 = X
            Y1 = Y
            grid[X + 1][Y] = colour
            return find_shapes(X + 1,Y,X0,Y0,X1,Y1,colour)
        elif Y - 1 >= 0 and X + 1 <= N1 - 1 and grid[X + 1][Y - 1] == 1:
            if Y - 1 == Y0 and X + 1 == X0:
                grid[X0][Y0] = colour
                return 
            X1 = X 
            Y1 = Y
            grid[X + 1][Y - 1] = colour
            return find_shapes(X + 1,Y - 1,X0,Y0,X1,Y1,colour)
        elif Y - 1 >= 0 and grid[X][Y - 1] == 1:
            if X == X0 and Y - 1 == Y0:
                grid[X0][Y0] = colour
                return 
            X1 = X 
            Y1 = Y
            grid[X][Y - 1] = colour
            return find_shapes(X,Y - 1,X0,Y0,X1,Y1,colour)
        elif X - 1 >= 0 and Y - 1 >= 0 and grid[X - 1][Y - 1] == 1:
            if X - 1 == X0 and Y - 1 == Y0:
                grid[X0][Y0] = colour
                return 
            X1 = X
            Y1 = Y
            grid[X - 1][Y - 1] = colour
            return find_shapes(X - 1,Y - 1,X0,Y0,X1,Y1,colour)
        elif X - 1 >= 0 and grid[X - 1][Y] == 1:
            if X - 1 == X0 and Y == Y0:
                grid[X0][Y0] = colour
                return 
            X1 = X
            Y1 = Y
            grid[X - 1][Y] = colour
            return find_shapes(X - 1,Y,X0,Y0,X1,Y1,colour)
        else:
            return find_shapes(X1,Y1,X0,Y0,X1,Y1,colour)
            

    ## W
    if X == X1 and Y < Y1: 
        if X + 1 <= N1 - 1 and Y + 1 <= N2 - 1 and grid[X + 1][Y + 1] == 1:
            if X + 1 == X0 and Y + 1 == Y0:
                grid[X0][Y0] = colour
                return 
            X1 = X
            Y1 = Y
            grid[X + 1][Y + 1] = colour
            return find_shapes(X + 1,Y + 1,X0,Y0,X1,Y1,colour)
        elif X + 1 <= N1 - 1 and grid[X + 1][Y] == 1:
            if X + 1 == X0 and Y == Y0:
                grid[X0][Y0] = colour
                return 
            X1 = X
            Y1 = Y
            grid[X + 1][Y] = colour
            return find_shapes(X + 1,Y,X0,Y0,X1,Y1,colour)
        elif Y - 1 >= 0 and X + 1 <= N1 - 1 and grid[X + 1][Y - 1] == 1:
            if Y - 1 == Y0 and X + 1 == X0:
                grid[X0][Y0] = colour
                return 
            X1 = X 
            Y1 = Y
            grid[X + 1][Y - 1] = colour
            find_shapes(X + 1,Y - 1,X0,Y0,X1,Y1,colour)
        elif Y - 1 >= 0 and grid[X][Y - 1] == 1:
            if X == X0 and Y - 1 == Y0:
                grid[X0][Y0] = colour
                return 
            X1 = X 
            Y1 = Y
            grid[X][Y - 1] = colour
            return find_shapes(X,Y - 1,X0,Y0,X1,Y1,colour)
        elif X - 1 >= 0 and Y - 1 >= 0 and grid[X - 1][Y - 1] == 1:
            if X - 1 == X0 and Y - 1 == Y0:
                grid[X0][Y0] = colour
                return 
            X1 = X
            Y1 = Y
            grid[X - 1][Y - 1] = colour
            return find_shapes(X - 1,Y - 1,X0,Y0,X1,Y1,colour)
        elif X - 1 >= 0 and grid[X - 1][Y] == 1:
            if X - 1 == X0 and Y == Y0:
                grid[X0][Y0] = colour
                return 
            X1 = X
            Y1 = Y
            grid[X - 1][Y] = colour
            return find_shapes(X - 1,Y,X0,Y0,X1,Y1,colour)
        elif X - 1 >= 0 and Y + 1 <= N2 - 1 and grid[X - 1][Y + 1] == 1:
            if X - 1 == X0 and Y + 1 == Y0:
                grid[X0][Y0] = colour
                return 
            X1 = X
            Y1 = Y
            grid[X - 1][Y + 1] = colour
            return find_shapes(X - 1,Y + 1,X0,Y0,X1,Y1,colour)
        else:
            return find_shapes(X1,Y1,X0,Y0,X1,Y1,colour)
            

    ## NW
    if X < X1 and Y < Y1:
        if X + 1 <= N1 - 1 and grid[X + 1][Y] == 1:
            if X + 1 == X0 and Y == Y0:
                grid[X0][Y0] = colour
                return 
            X1 = X
            Y1 = Y
            grid[X + 1][Y] = colour
            return find_shapes(X + 1,Y,X0,Y0,X1,Y1,colour)
        elif Y - 1 >= 0 and X + 1 <= N1 - 1 and grid[X + 1][Y - 1] == 1:
            if Y - 1 == Y0 and X + 1 == X0:
                grid[X0][Y0] = colour
                return 
            X1 = X 
            Y1 = Y
            grid[X + 1][Y - 1] = colour
            find_shapes(X + 1,Y - 1,X0,Y0,X1,Y1,colour)
        elif Y - 1 >= 0 and grid[X][Y - 1] == 1:
            if X == X0 and Y - 1 == Y0:
                grid[X0][Y0] = colour
                return 
            X1 = X 
            Y1 = Y
            grid[X][Y - 1] = colour
            return find_shapes(X,Y - 1,X0,Y0,X1,Y1,colour)
        elif X - 1 >= 0 and Y - 1 >= 0 and grid[X - 1][Y - 1] == 1:
            if X - 1 == X0 and Y - 1 == Y0:
                grid[X0][Y0] = colour
                return 
            X1 = X
            Y1 = Y
            grid[X - 1][Y - 1] = colour
            return find_shapes(X - 1,Y - 1,X0,Y0,X1,Y1,colour)
        elif X - 1 >= 0 and grid[X - 1][Y] == 1:
            if X - 1 == X0 and Y == Y0:
                grid[X0][Y0] = colour
                return 
            X1 = X
            Y1 = Y
            grid[X - 1][Y] = colour
            return find_shapes(X - 1,Y,X0,Y0,X1,Y1,colour)
        elif X - 1 >= 0 and Y + 1 <= N2 - 1 and grid[X - 1][Y + 1] == 1:
            if X - 1 == X0 and Y + 1 == Y0:
                grid[X0][Y0] = colour
                return 
            X1 = X
            Y1 = Y
            grid[X - 1][Y + 1] = colour
            return find_shapes(X - 1,Y + 1,X0,Y0,X1,Y1,colour)
        elif Y + 1 <= N2 - 1 and grid[X][Y + 1] == 1:
            if X == X0 and Y + 1 == Y0:
                grid[X0][Y0] = colour
                return 
            X1 = X
            Y1 = Y
            grid[X][Y + 1] = colour
            return find_shapes(X,Y + 1,X0,Y0,X1,Y1,colour)
        else:
            return find_shapes(X1,Y1,X0,Y0,X1,Y1)
            

    ## N
    if X < X1 and Y == Y1:
        if Y - 1 >= 0 and X + 1 <= N1 - 1 and grid[X + 1][Y - 1] == 1:
            if Y - 1 == Y0 and X + 1 == X0:
                grid[X0][Y0] = colour
                return 
            X1 = X 
            Y1 = Y
            grid[X + 1][Y - 1] = colour
            return find_shapes(X + 1,Y - 1,X0,Y0,X1,Y1,colour)
        elif Y - 1 >= 0 and grid[X][Y - 1] == 1:
            if X == X0 and Y - 1 == Y0:
                grid[X0][Y0] = colour
                return 
            X1 = X 
            Y1 = Y
            grid[X][Y - 1] = colour
            return find_shapes(X,Y - 1,X0,Y0,X1,Y1,colour)
        elif X - 1 >= 0 and Y - 1 >= 0 and grid[X - 1][Y - 1] == 1:
            if X - 1 == X0 and Y - 1 == Y0:
                grid[X0][Y0] = colour
                return 
            X1 = X
            Y1 = Y
            grid[X - 1][Y - 1] = colour
            return find_shapes(X - 1,Y - 1,X0,Y0,X1,Y1,colour)
        elif X - 1 >= 0 and grid[X - 1][Y] == 1:
            if X - 1 == X0 and Y == Y0:
                grid[X0][Y0] = colour
                return 
            X1 = X
            Y1 = Y
            grid[X - 1][Y] = colour
            return find_shapes(X - 1,Y,X0,Y0,X1,Y1,colour)
        elif X - 1 >= 0 and Y + 1 <= N2 - 1 and grid[X - 1][Y + 1] == 1:
            if X - 1 == X0 and Y + 1 == Y0:
                grid[X0][Y0] = colour
                return 
            X1 = X
            Y1 = Y
            grid[X - 1][Y + 1] = colour
            return find_shapes(X - 1,Y + 1,X0,Y0,X1,Y1,colour)
        elif Y + 1 <= N2 - 1 and grid[X][Y + 1] == 1:
            if X == X0 and Y + 1 == Y0:
                grid[X0][Y0] = colour
                return 
            X1 = X
            Y1 = Y
            grid[X][Y + 1] = colour
            return find_shapes(X,Y + 1,X0,Y0,X1,Y1,colour)
        elif X + 1 <= N1 - 1 and Y + 1 <= N2 - 1 and grid[X + 1][Y + 1] == 1:
            if X + 1 == X0 and Y + 1 == Y0:
                grid[X0][Y0] = colour
                return 
            X1 = X
            Y1 = Y
            grid[X + 1][Y + 1] = colour
            return find_shapes(X + 1,Y + 1,X0,Y0,X1,Y1,colour)
        else:
            return find_shapes(X1,Y1,X0,Y0,X1,Y1,colour)
            

    ## NE  
    if X < X1 and Y > Y1:
        if Y - 1 >= 0 and grid[X][Y - 1] == 1:
            if X == X0 and Y - 1 == Y0:
                grid[X0][Y0] = colour
                return 
            X1 = X 
            Y1 = Y
            grid[X][Y - 1] = colour
            return find_shapes(X,Y - 1,X0,Y0,X1,Y1,colour)
        elif X - 1 >= 0 and Y - 1 >= 0 and grid[X - 1][Y - 1] == 1:
            if X - 1 == X0 and Y - 1 == Y0:
                grid[X0][Y0] = colour
                return 
            X1 = X
            Y1 = Y
            grid[X - 1][Y - 1] = colour
            return find_shapes(X - 1,Y - 1,X0,Y0,X1,Y1,colour)
        elif X - 1 >= 0 and grid[X - 1][Y] == 1:
            if X - 1 == X0 and Y == Y0:
                grid[X0][Y0] = colour
                return 
            X1 = X
            Y1 = Y
            grid[X - 1][Y] = colour
            return find_shapes(X - 1,Y,X0,Y0,X1,Y1,colour)
        elif X - 1 >= 0 and Y + 1 <= N2 - 1 and grid[X - 1][Y + 1] == 1:
            if X - 1 == X0 and Y + 1 == Y0:
                grid[X0][Y0] = colour
                return 
            X1 = X
            Y1 = Y
            grid[X - 1][Y + 1] = colour
            return find_shapes(X - 1,Y + 1,X0,Y0,X1,Y1,colour)
        elif Y + 1 <= N2 - 1 and grid[X][Y + 1] == 1:
            if X == X0 and Y + 1 == Y0:
                grid[X0][Y0] = colour
                return 
            X1 = X
            Y1 = Y
            grid[X][Y + 1] = colour
            return find_shapes(X,Y + 1,X0,Y0,X1,Y1,colour)
        elif X + 1 <= N1 - 1 and Y + 1 <= N2 - 1 and grid[X + 1][Y + 1] == 1:
            if X + 1 == X0 and Y + 1 == Y0:
                grid[X0][Y0] = colour
                return 
            X1 = X
            Y1 = Y
            grid[X + 1][Y + 1] = colour
            return find_shapes(X + 1,Y + 1,X0,Y0,X1,Y1,colour)
        elif X + 1 <= N1 - 1 and grid[X + 1][Y] == 1:
            if X + 1 == X0 and Y == Y0:
                grid[X0][Y0] = colour
                return 
            X1 = X 
            Y1 = Y
            grid[X + 1][Y] = colour
            return find_shapes(X + 1,Y,X0,Y0,X1,Y1,colour)
        else:
            return find_shapes(X1,Y1,X0,Y0,X1,Y1,colour)
            
    ## E
    if X == X1 and Y > Y1:
        if X - 1 >= 0 and Y - 1 >= 0 and grid[X - 1][Y - 1] == 1:
            if X - 1 == X0 and Y - 1 == Y0:
                grid[X0][Y0] = colour
                return
            X1 = X
            Y1 = Y
            grid[X - 1][Y - 1] = colour
            return find_shapes(X - 1,Y - 1,X0,Y0,X1,Y1,colour)
        elif X - 1 >= 0 and grid[X - 1][Y] == 1:
            if X - 1 == X0 and Y == Y0:
                grid[X0][Y0] = colour
                return
            X1 = X
            Y1 = Y
            grid[X - 1][Y] = colour
            return find_shapes(X - 1,Y,X0,Y0,X1,Y1,colour)
        elif X - 1 >= 0 and Y + 1 <= N2 - 1 and grid[X - 1][Y + 1] == 1:
            if X - 1 == X0 and Y + 1 == Y0:
                grid[X0][Y0] = colour
                return
            X1 = X - 1
            Y1 = Y + 1
            grid[X - 1][Y + 1] = colour
            return find_shapes(X - 1,Y + 1,X0,Y0,X1,Y1,colour) 
        elif Y + 1 <= N2 - 1 and grid[X][Y + 1] == 1:
            if X == X0 and Y + 1 == Y0:
                grid[X0][Y0] = colour
                return
            X1 = X
            Y1 = Y
            grid[X][Y + 1] = colour
            return find_shapes(X,Y + 1,X0,Y0,X1,Y1,colour)
        elif X + 1 <= N1 - 1 and Y + 1 <= N2 - 1 and grid[X + 1][Y + 1] == 1:
            if X + 1 == X0 and Y + 1 == Y0:
                grid[X0][Y0] = colour
                return
            X1 = X
            Y1 = Y
            grid[X + 1][Y + 1] = colour
            return find_shapes(X + 1,Y + 1,X0,Y0,X1,Y1,colour)
        elif X + 1 <= N1 - 1 and grid[X + 1][Y] == 1:
            if X + 1 == X0 and Y == Y0:
                grid[X0][Y0] = colour
                return
            X1 = X
            Y1 = Y
            grid[X + 1][Y] = colour
            return find_shapes(X + 1,Y,X0,Y0,X1,Y1,colour)
        elif Y - 1 >= 0 and X + 1 <= N1 - 1 and grid[X + 1][Y - 1] == 1:
            if Y - 1 == Y0 and X + 1 == X0:
                grid[X0][Y0] = colour
                return
            X1 = X 
            Y1 = Y
            grid[X + 1][Y - 1] = colour
            return find_shapes(X + 1,Y - 1,X0,Y0,X1,Y1,colour)
        else:
            return find_shapes(X1,Y1,X0,Y0,X1,Y1,colour)
    display()
    find_shapes(1,1,1,1,1,1,2)
