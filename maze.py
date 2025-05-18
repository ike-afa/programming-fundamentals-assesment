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

if __name__ == "__main__":
    c = cell()
    print(c.visited)
    c.visited = True
    print(c.visited)

    maze = newMaze(20, 20)
    