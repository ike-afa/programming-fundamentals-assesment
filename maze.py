import random

class cell:

    row=None
    col=None
    visited=False
    leftConnected=False
    rightConnected=False
    topConnected=False
    bottomConnected=False

def newMaze(numRows, numCols):
    maze = []
    for row in range(0, numRows):
        rowArray = []
        for col in range(0, numCols):
            c = cell()
            c.row = row
            c.col = col
            rowArray.append(c)
        maze.append(rowArray)
    return maze


def showMaze(numRows, numCols, maze):
    for row in range(0, numRows):
        topLine = ""
        cellLine = ""
        for col in range(0, numCols):
            if maze[row][col].topConnected:
                topLine = topLine + "+ "
            else:
                topLine = topLine + "+-"
            if maze[row][col].leftConnected:
                cellLine = cellLine + "  "
            else:
                cellLine = cellLine + "| "
        
        print(topLine + "+")
        print(cellLine + "|")
    print("+-"*(numCols)+"+")
        
def findNeighbours(row, col, rows, cols, maze):
    '''finds all neighbours of a cell'''
    neighbours = []
    for i in range(-1, 2):
       # add i to row
       if row + i < 0 or row + i >= rows:
           continue
       
       for j in range(-1, 2):
           # add j to col
           if col + j < 0 or col + j >= cols:
               continue
           
           if i == 0 and j == 0:
               # skip target cell
               continue

           neighbour = maze[row+i][col+j]
           neighbours.append(neighbour)

    return neighbours

def unvisitedNeighbour(row, col, rows, cols, maze):
    '''return a random unvisited neighbour (or None)'''
    neighbours = findNeighbours(row, col, rows, cols, maze)
    unvisited = []

    for neighbour in neighbours:
        if not neighbour.visited:
            unvisited.append(neighbour)

    if len(unvisited) == 0:
        return None
    else:
        randomIndex = random.randint(0, len(unvisited)-1)
        return unvisited[randomIndex]      
           

    
