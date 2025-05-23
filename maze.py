import random

class cell:
    row=None
    col=None
    visited=False
    leftConnected=False
    rightConnected=False
    topConnected=False
    bottomConnected=False

    def connect(self, neighbour):
        if self.row < neighbour.row:
            self.bottomConnected = True
            neighbour.topConnected = True
        else:
            self.topConnected = True
            neighbour.bottomConnected = True

        if self.col < neighbour.col:
            self.rightConnected = True
            neighbour.leftConnected = True
        else:
            self.leftConnected = True
            neighbour.rightConnected = True

        self.visited = True
        neighbour.visited = True

    def __repr__(self):
        return f"row = {self.row}, col = {self.col}, leftConnected = {self.leftConnected}, rightConnected = {self.rightConnected}, topConnected = {self.topConnected}, bottomConnected = {self.bottomConnected}"

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
           
           # skip target cell and diagonals
           if (i + j) == 0 or j == i:
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
    
def generateMaze(rows, cols):
    maze = newMaze(rows, cols)
    cells = rows * cols
    row = random.randint(0, rows - 1)
    col = random.randint(0, cols - 1)
    current = maze[row][col]
    stack = []
    numVisited = 0
    while numVisited < cells:
        neighbour = unvisitedNeighbour(current.row, current.col, rows, cols, maze)
        while neighbour == None:
            if len(stack) == 0:
                return
            current = stack.pop()
            neighbour = unvisitedNeighbour(current.row, current.col, rows, cols, maze)
        
        current.connect(neighbour)
        stack.append(current)
        current = neighbour
        numVisited += 1

        showMaze(rows, cols, maze)
        input("<ENTER> for next connection...")

if __name__ == "__main__":
    rows = 10
    cols = 10
    generateMaze(rows, cols)
