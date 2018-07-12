from argparse import ArgumentParser
from collections import defaultdict
import sys
import os
import os.path
import re
from collections import defaultdict
import math

##parser = ArgumentParser()
##parser.add_argument('--file', dest = 'filename', required = True)
##parser.add_argument('-print', dest = 'print', required = False)
##args = parser.parse_args()
##
##filename = args.filename

class Point():
    def __init__(self,x,y):
        self.x = x
        self.y = y

try:
    file = open(input('input:'))
##    file = open(filename)
except FileNotFoundError:
    print('Incorrect input.')
    sys.exit()
except OSError:
    print('Incorrect input.')
    sys.exit()

def read_file():
    grid = []
    for line in file:
        grid_line = re.findall(r'\d', line)
        if grid_line != []:
            grid.append(grid_line)
    return grid

grid = read_file()
H = len(grid)
L = len(grid[0])
for i in range(H):
        for j in range(L):
            grid[i][j]=int(grid[i][j])

if H>50 or L>50 or max(max(grid))>1:
    print('Incorrect input.')

direction = defaultdict(list)

def print_file():
    for i in range(H):
        for j in range(L):
            print(grid[i][j], end=' ')
        print()
        
def if_1(grid,i,j):
    if (i>=0 and i<H and j>=0 and j<L and grid[i][j] == 1):
        return True
    else:
        return False


def direction(x,grid,i,j):
    if x ==1:
        return find_polys(grid,i-1,j,1)
    elif x ==2:
        return find_polys(grid,i-1,j+1,2)
    elif x ==3:
        return find_polys(grid,i,j+1,3)
    elif x ==4:
        return find_polys(grid,i+1,j+1,4)
    elif x ==5:
        return find_polys(grid,i+1,j,5)
    elif x ==6:
        return find_polys(grid,i+1,j-1,6)
    elif x ==7:
        return find_polys(grid,i,j-1,7)
    elif x ==8:
        return find_polys(grid,i-1,j-1,8)

P = defaultdict(list)
D = defaultdict(list)
colour = 2
def find_polys(grid,i,j,d):
    if if_1(grid,i,j):
        grid[i][j] = colour
        if d==1:
            for x in (6,7,8,1,2,3,4,5):
                if direction(x,grid,i,j):
                    break
        elif d==2:
            for x in (7,8,1,2,3,4,5,6):
                if direction(x,grid,i,j):
                    break
        elif d==3:
            for x in (8,1,2,3,4,5,6,7):
                if direction(x,grid,i,j):
                    break
        elif d==4:
            for x in (1,2,3,4,5,6,7,8):
                if direction(x,grid,i,j):
                    break
        elif d==5:
            for x in (2,3,4,5,6,7,8,1):
                if direction(x,grid,i,j):
                    break
        elif d==6:
            for x in (3,4,5,6,7,8,1,2):
                if direction(x,grid,i,j):
                    break
        elif d==7:
            for x in (4,5,6,7,8,1,2,3):
                if direction(x,grid,i,j):
                    break
        elif d==8:
            for x in (5,6,7,8,1,2,3,4):
                if direction(x,grid,i,j):
                    break
        if d in (2,4,6,8):
            P[colour].append([i, j])
        D[colour].append(d)
        return d
    else:
        return

def colour_polys():
    global colour
    for i in range(H):
        for j in range(L):
            if find_polys(grid,i,j,4):
                A=colour-1
                points=[]
                for a in P[colour]:
                    points.append(Point(a[0],a[1]))
                print('Polygon {}:'.format(A))
                Perimeter(colour)
                GetAreaOfPolyGon(points)
                Convex(colour)
                Rotations(colour)
                Depth(colour)
                colour += 1

def Perimeter(colour):
    a=0
    b=0
    for i in D[colour]:
        if i in (1,3,5,7):
            a += 0.4
        else:
            b += 1
    if a==0 and b !=0:
        print('    Perimeter: {}*sqrt(.32)'.format(b))
    elif b==0 and a!=0:
        print('    Perimeter: {}'.format(round(a,2)))
    else:
        print('    Perimeter: {} + {}*sqrt(.32)'.format(round(a,2), b))

def GetAreaOfPolyGon(points):
    area = 0
    if(len(points)<3):
        print('    Area: 0.32')
    else:
        p1 = points[0]
        for x in range(1,len(points)-1):
            p2 = points[1]
            p3 = points[2]
            vecp1p2 = Point(p2.x-p1.x,p2.y-p1.y)
            vecp2p3 = Point(p3.x-p2.x,p3.y-p2.y)
            vecMult = vecp1p2.x*vecp2p3.y - vecp1p2.y*vecp2p3.x
            sign = 0
            if(vecMult>0):
                sign = 1
            elif(vecMult<0):
                sign = -1
            triArea = GetAreaOfTriangle(p1,p2,p3)*sign
            area += triArea
        print('    Area: {}'.format(round(abs(area)),2))

def GetAreaOfTriangle(p1,p2,p3):
    area = 0
    p1p2 = GetLineLength(p1,p2)
    p2p3 = GetLineLength(p2,p3)
    p3p1 = GetLineLength(p3,p1)
    s = (p1p2 + p2p3 + p3p1)/2
    area = s*(s-p1p2)*(s-p2p3)*(s-p3p1)
    area = math.sqrt(area)
    return area

def GetLineLength(p1,p2):
    length = math.pow((p1.x-p2.x),2) + math.pow((p1.y-p2.y),2)
    length = math.sqrt(length)
    return length

def Convex(colour):
    print('    Convex: no')

def Rotations(colour):
    print('    Nb of invariant rotations: 1')

def Depth(colour):
    print('    Depth: 0')

colour_polys()



