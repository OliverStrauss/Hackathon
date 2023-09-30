

def display_map(map):
    for x in range(0,25):
        rowstr = ""
        print("")
        for y in range(0,25):
            if y == 0:
                rowstr =  rowstr + "|"
            if map[x][y] == False:
                rowstr =  rowstr + "O|"
            else:
                rowstr = rowstr + "x|"
            
        print(rowstr)

def field_plot(matrix):
    print("One tile is equal to 20 acres")
    x = int(int(input("What acreage does your feild start at on the X axis"))/20)
    y = int(int(input("What acreage does your feild start at on the Y axis"))/20)
    xlen = int(input("What acreage of your feild is in width"))
    ylen = int(input("What acreage of your feild is in height"))
    xlen = int(xlen/20)
    ylen = int(ylen/20)

    print(x,y)
    print(xlen,ylen)
    for i in range(y,ylen+y):
        for y in range(x, x+xlen):
    
            matrix[i][y] = True


        

def main():
    SCREENHEIGHT = 500
    SCREENWIDTH = SCREENHEIGHT

    #wb = T.Screen()
    #wb.bgcolor("green")
    #wb.setup(SCREENWIDTH,SCREENHEIGHT)
    #createGrid()
     #Method 1: Using list comprehension
rows = 25
cols = 25

# Initialize a 2D array of booleans with False values
matrix = [[False for _ in range(cols)] for _ in range(rows)]

# Method 2: Using nested loops
rows = 25
cols = 25

# Initialize a 2D array of booleans with False values
matrix = []
for _ in range(rows):
    row = [False] * cols
    matrix.append(row)

field_plot(matrix)
# Printing the 2D array
display_map(matrix)















main()