import tkinter

#DECLARING CONSTANTS
NumRows = 6
NumColumns = 7
Scale = 70
CircleDim = int(Scale/(50/35))
Fill = "blue"
GWidth = 5
Colour = "red"
PlayerOneColour = "yellow"
PlayerTwoColour = "red"
Token=""
PlayerOneToken = "O"
PlayerTwoToken = "X"
TurnsTaken=0

def CreateGrid():
    Grid=[]
    for Row in range(NumRows):
        Row=[]
        for Column in range(NumColumns):
            Row.append("_")
        Grid.append(Row)
    return Grid    

def PrintGrid(Grid):
    print("\n")
    for Row in range(NumRows):
        print(str(Row) + " " + str(Grid[Row]))

def GetRow(Column, Grid):
    Valid = False
    Row=NumRows-1
    while (Valid==False):
        if Grid[Row][Column] == "_":
            Valid=True
        else:
            Row=Row-1
        if Row < 0:
            Valid=True
            Row = 1000
    return Row

def InitialiseButtons(Grid):
    for Count in range(NumColumns):
        btn = tkinter.Button(Window, text=str(Count), width = int(Scale/10), command = lambda Column=Count:DropCoin(Grid, Column))
        btn.grid(row=0, column=Count)

def InitiateGridCanvas():
    canv = tkinter.Canvas(Window, width=(Scale*NumColumns), height=(Scale*NumRows))
    canv.grid(row=1, column=0, rowspan=NumRows, columnspan=NumColumns)
    return canv


#ButtonClick Function
def DropCoin(Grid, Column):
    #Row = FindRow()
    Row=GetRow(Column, Grid)+1
    if Row == 1001:
        tkinter.messagebox.showerror("Error", "Illegal Move")
    else:
        Items = MainGame()
        Token = Items[0]
        Colour = Items[1]
        Coin = CreateCoin(Colour)
        Coin.grid(row = Row, column=Column)
        Grid[Row-1][Column] =(Token)
        Coin.lift(Coin)
        print(CheckWin(Grid, Row, Column, Token))
    PrintGrid(Grid)
    

def CreateCoin(Colour):
    CircleCanv = tkinter.Canvas(Window, width=CircleDim, height = CircleDim)
    CircleCanv.create_oval(0, 0, CircleDim, CircleDim, fill=Colour)
    return CircleCanv

def SpaceGrid(): #Used to space out the grid, as adding new canvases (when dropping coins) causes misalignment
    for Row in range(NumRows):
        Row=Row+1
        for Column in range(NumColumns):
            canvas = tkinter.Canvas(Window, width=CircleDim/1.5, height = CircleDim/1.1)
            canvas.grid(row = Row, column=Column)
        Row=Row-1

def DrawGrid(canv):
    for Counter in range(NumColumns+1):
        canv.create_line((Scale*Counter), 0, (Scale*Counter), (Scale*NumRows), fill=Fill, width=GWidth)
    for Counter in range(NumRows):
        canv.create_line(0, (Scale*Counter), (Scale*NumColumns),(Scale*Counter), fill=Fill, width=GWidth)

def CheckWin(Grid, Row, Column, Token):
    Down=False
    Up=False
    Right=False
    Left=False
    
    if not Row > NumRows-3:
        #Down possible
        Down=True
    if Row > NumRows-3:
        #Up possible
        Up=True
    if Column < 4:
        #Right possible
        Right=True
    if Column > 2:
        #Left possible
        Left=True

    Row=Row-1
    if Left==True:
        if Up == True:
            if Grid[Row][Column] == Token and Grid[Row-1][Column-1] == Token and Grid[Row-2][Column-2] == Token and Grid[Row-3][Column-3] == Token:
                return True
        if Down == True:
            if Grid[Row][Column] == Token and Grid[Row+1][Column-1] == Token and Grid[Row+2][Column-2] == Token and Grid[Row+3][Column-3] == Token:
                return True
        if (Down==False) and (Up==False):
            if Grid[Row][Column] == Token and Grid[Row][Column-1] == Token and Grid[Row][Column-2] == Token and Grid[Row][Column-3] == Token:
                return True
            
    if Right==True:
        if Up == True:
            if Grid[Row][Column] == Token and Grid[Row-1][Column+1] == Token and Grid[Row-2][Column+2] == Token and Grid[Row-3][Column+3] == Token:
                return True
        if Down == True:
            if Grid[Row][Column] == Token and Grid[Row+1][Column+1] == Token and Grid[Row+2][Column+2] == Token and Grid[Row+3][Column+3] == Token:
                return True
        if (Down==False) and (Up==False):
            if Grid[Row][Column] == Token and Grid[Row][Column+1] == Token and Grid[Row][Column+2] == Token and Grid[Row][Column+3] == Token:
                return True
    return False
            

def InitialSetup():
    Grid = CreateGrid()
    InitialiseButtons(Grid)
    canv = InitiateGridCanvas()
    DrawGrid(canv)
    SpaceGrid()

def PlayerOneMove():
    Token = PlayerOneToken
    Colour = PlayerOneColour
    return Token, Colour

def PlayerTwoMove():
    Token = PlayerTwoToken
    Colour = PlayerTwoColour
    return Token, Colour

def MainGame():
    if TurnsTaken%2==0: #if number of moves is even
        Token = PlayerOneMove()[0]
        Colour = PlayerOneMove()[1]
    else:
        Token = PlayerTwoMove()[0]
        Colour = PlayerTwoMove()[1]
        
    global TurnsTaken
    TurnsTaken=TurnsTaken+1
    print(TurnsTaken)
    return Token, Colour

Window = tkinter.Tk()
InitialSetup()
