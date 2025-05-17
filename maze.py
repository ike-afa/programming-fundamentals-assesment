class cell:

    row=None
    col=None
    visited=False
    leftConnected=False
    rightConnected=False
    topConnected=False
    bottomConnected=False



if __name__ == "__main__":
    c = cell()
    print(c.visited)
    c.visited = True
    print(c.visited)