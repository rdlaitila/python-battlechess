#import python packages
import sys, os, curses, time

#get global reference to parent cengine module
cengine = sys.modules["cengine"] 

#very important globals
colorPair = 49

#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::  
class newCanvas(): 
    #-----------------------------------
    def __init__(self, pWIDTH, pHEIGHT):
        self.buffer = [[cengine.graphics.newCell("", 1) for x in range(pHEIGHT)] for y in range(pWIDTH)]
        self.xOrigin = 0
        self.yOrigin = 0
        self.xTranslate = 0
        self.yTranslate = 0
    #-----------------------------------
    def resize(self,pNEWWIDTH, pNEWHEIGHT): 
        return
    #-----------------------------------
    def clear(self):
        for a in range(0, len(self.buffer)):
            for b in range(0, len(self.buffer[a])):
                self.buffer[a][b] = ["", 0]
    #-----------------------------------
    def setCell(self,pXPOS, pYPOS, pCHARDATA):
        x = pXPOS + self.xTranslate
        y = pYPOS + self.yTranslate
        if  x >= 0 and x <= len(self.buffer) - 1 and y >= 0 and y <= len(self.buffer[0]) - 1:
            self.buffer[x][y] = pCHARDATA
        else: return
    #-----------------------------------
    def setFromCanvas(self, pCANVAS):
        return
    #-----------------------------------
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
def newCell(pCHAR, pCOLORPAIR):
    cell = [pCHAR, pCOLORPAIR]
    return cell
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
def getWidth(): 
    global cengine
    return cengine.screen.getmaxyx()[1]-1
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
def getHeight(): 
    global cengine
    return cengine.screen.getmaxyx()[0]-1
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
def setColor(pFOREGROUND, pBACKGROUND):
    
    f = pFOREGROUND.upper()
    b = pBACKGROUND.upper()
    
    if f == "BLACK" and b == "BLACK": cengine.graphics.colorPair = 1
    elif f == "BLACK" and b == "BLUE": cengine.graphics.colorPair = 2
    elif f == "BLACK" and b == "CYAN": cengine.graphics.colorPair = 3
    elif f == "BLACK" and b == "GREEN": cengine.graphics.colorPair = 4
    elif f == "BLACK" and b == "MAGENTA": cengine.graphics.colorPair = 5
    elif f == "BLACK" and b == "RED": cengine.graphics.colorPair = 6
    elif f == "BLACK" and b == "WHITE": cengine.graphics.colorPair = 7
    elif f == "BLACK" and b == "YELLOW": cengine.graphics.colorPair = 8    
    elif f == "BLUE" and b == "BLACK": cengine.graphics.colorPair = 9
    elif f == "BLUE" and b == "BLUE": cengine.graphics.colorPair = 10
    elif f == "BLUE" and b == "CYAN": cengine.graphics.colorPair = 11
    elif f == "BLUE" and b == "GREEN": cengine.graphics.colorPair = 12
    elif f == "BLUE" and b == "MAGENTA": cengine.graphics.colorPair = 13
    elif f == "BLUE" and b == "RED": cengine.graphics.colorPair = 14
    elif f == "BLUE" and b == "WHITE": cengine.graphics.colorPair = 15
    elif f == "BLUE" and b == "YELLOW": cengine.graphics.colorPair = 16    
    elif f == "CYAN" and b == "BLACK": cengine.graphics.colorPair = 17
    elif f == "CYAN" and b == "BLUE": cengine.graphics.colorPair = 18
    elif f == "CYAN" and b == "CYAN": cengine.graphics.colorPair = 19
    elif f == "CYAN" and b == "GREEN": cengine.graphics.colorPair = 20
    elif f == "CYAN" and b == "MAGENTA": cengine.graphics.colorPair = 21
    elif f == "CYAN" and b == "RED": cengine.graphics.colorPair = 22
    elif f == "CYAN" and b == "WHITE": cengine.graphics.colorPair = 23
    elif f == "CYAN" and b == "YELLOW": cengine.graphics.colorPair = 24    
    elif f == "GREEN" and b == "BLACK": cengine.graphics.colorPair = 25
    elif f == "GREEN" and b == "BLUE": cengine.graphics.colorPair = 26
    elif f == "GREEN" and b == "CYAN": cengine.graphics.colorPair = 27
    elif f == "GREEN" and b == "GREEN": cengine.graphics.colorPair = 28
    elif f == "GREEN" and b == "MAGENTA": cengine.graphics.colorPair = 29
    elif f == "GREEN" and b == "RED": cengine.graphics.colorPair = 30
    elif f == "GREEN" and b == "WHITE": cengine.graphics.colorPair = 31
    elif f == "GREEN" and b == "YELLOW": cengine.graphics.colorPair = 32    
    elif f == "MAGENTA" and b == "BLACK": cengine.graphics.colorPair = 33
    elif f == "MAGENTA" and b == "BLUE": cengine.graphics.colorPair = 34
    elif f == "MAGENTA" and b == "CYAN": cengine.graphics.colorPair = 35
    elif f == "MAGENTA" and b == "GREEN": cengine.graphics.colorPair = 36
    elif f == "MAGENTA" and b == "MAGENTA": cengine.graphics.colorPair = 37
    elif f == "MAGENTA" and b == "RED": cengine.graphics.colorPair = 38
    elif f == "MAGENTA" and b == "WHITE": cengine.graphics.colorPair = 39
    elif f == "MAGENTA" and b == "YELLOW": cengine.graphics.colorPair = 40     
    elif f == "RED" and b == "BLACK": cengine.graphics.colorPair = 41
    elif f == "RED" and b == "BLUE": cengine.graphics.colorPair = 42
    elif f == "RED" and b == "CYAN": cengine.graphics.colorPair = 43
    elif f == "RED" and b == "GREEN": cengine.graphics.colorPair = 44
    elif f == "RED" and b == "MAGENTA": cengine.graphics.colorPair = 45
    elif f == "RED" and b == "RED": cengine.graphics.colorPair = 46
    elif f == "RED" and b == "WHITE": cengine.graphics.colorPair = 47 
    elif f == "RED" and b == "YELLOW": cengine.graphics.colorPair = 48    
    elif f == "WHITE" and b == "BLACK": cengine.graphics.colorPair = 49
    elif f == "WHITE" and b == "BLUE": cengine.graphics.colorPair = 50
    elif f == "WHITE" and b == "CYAN": cengine.graphics.colorPair = 51
    elif f == "WHITE" and b == "GREEN": cengine.graphics.colorPair = 52
    elif f == "WHITE" and b == "MAGENTA": cengine.graphics.colorPair = 53
    elif f == "WHITE" and b == "RED": cengine.graphics.colorPair = 54
    elif f == "WHITE" and b == "WHITE": cengine.graphics.colorPair = 55
    elif f == "WHITE" and b == "YELLOW": cengine.graphics.colorPair = 56    
    elif f == "YELLOW" and b == "BLACK": cengine.graphics.colorPair = 57
    elif f == "YELLOW" and b == "BLUE": cengine.graphics.colorPair = 58
    elif f == "YELLOW" and b == "CYAN": cengine.graphics.colorPair = 59
    elif f == "YELLOW" and b == "GREEN": cengine.graphics.colorPair = 60
    elif f == "YELLOW" and b == "MAGENTA": cengine.graphics.colorPair = 61
    elif f == "YELLOW" and b == "RED": cengine.graphics.colorPair = 62
    elif f == "YELLOW" and b == "WHITE": cengine.graphics.colorPair = 63
    elif f == "YELLOW" and b == "YELLOW": cengine.graphics.colorPair = 64
    
    return
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
def line(pCHAR, pX1, pY1, pX2, pY2):
    #"""Brensenham line algorithm"""
    
    x = pX1
    y = pY1
    x2 = pX2
    y2 = pY2
    
    steep = 0
    coords = []
    dx = abs(x2 - x)
    if (x2 - x) > 0: sx = 1
    else: sx = -1
    dy = abs(y2 - y)
    if (y2 - y) > 0: sy = 1
    else: sy = -1
    if dy > dx:
        steep = 1
        x,y = y,x
        dx,dy = dy,dx
        sx,sy = sy,sx
    d = (2 * dy) - dx
    for i in range(0,dx):
        if steep: coords.append((y,x))
        else: coords.append((x,y))
        while d >= 0:
            y = y + sy
            d = d - (2 * dx)
        x = x + sx
        d = d + (2 * dy)
    coords.append((x2,y2))
    
    for coord in coords:
        newCell = cengine.graphics.newCell(pCHAR, cengine.graphics.colorPair)
        cengine.canvas.setCell( coord[0], coord[1], newCell )
    
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
def rectangle(pMODE, pCHAR, pX, pY, pWIDTH, pHEIGHT):
    global cengine    
    
    if str.upper(pMODE) == "FILL":
        for a in range(pX, (pX + pWIDTH)):        
            for b in range(pY, (pY + pHEIGHT)):            
                cengine.canvas.setCell( a, b, newCell(pCHAR, cengine.graphics.colorPair) )
    elif str.upper(pMODE) == "LINE":
        for a in range(pX, (pX + pWIDTH)):            
            for b in range(pY, (pY + pHEIGHT)):
                if b == pY: cengine.canvas.setCell( a, b, newCell(pCHAR, cengine.graphics.colorPair) )
                if b == pY + pHEIGHT-1: cengine.canvas.setCell( a, b, newCell(pCHAR, cengine.graphics.colorPair) )                
                if a == pX: cengine.canvas.setCell( a, b, newCell(pCHAR, cengine.graphics.colorPair) )
                if a == pX + pWIDTH -1: cengine.canvas.setCell( a, b, newCell(pCHAR, cengine.graphics.colorPair) )
    return
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
def circle(pCHAR, x0, y0, radius):
    newCell = cengine.graphics.newCell(pCHAR, cengine.graphics.colorPair)
    
    f = 1 - radius
    ddf_x = 1
    ddf_y = -2 * radius
    x = 0
    y = radius
    cengine.canvas.setCell(x0, y0 + radius, newCell)
    cengine.canvas.setCell(x0, y0 - radius, newCell)
    cengine.canvas.setCell(x0 + radius, y0, newCell)
    cengine.canvas.setCell(x0 - radius, y0, newCell) 
    
    while x < y:
        if f >= 0: 
            y -= 1
            ddf_y += 2
            f += ddf_y
        x += 1
        ddf_x += 2
        f += ddf_x    
        cengine.canvas.setCell(x0 + x, y0 + y, newCell)
        cengine.canvas.setCell(x0 - x, y0 + y, newCell)
        cengine.canvas.setCell(x0 + x, y0 - y, newCell)
        cengine.canvas.setCell(x0 - x, y0 - y, newCell)
        cengine.canvas.setCell(x0 + y, y0 + x, newCell)
        cengine.canvas.setCell(x0 - y, y0 + x, newCell)
        cengine.canvas.setCell(x0 + y, y0 - x, newCell)
        cengine.canvas.setCell(x0 - y, y0 - x, newCell)
        
    return
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
def printstr(pSTRING, pXPOS, pYPOS):
    global cengine
    
    string = pSTRING
    x = pXPOS
    y = pYPOS

    #create a new list of cells to insert into the canvas buffer
    cellList = []    
    for char in string:
        newCell = cengine.graphics.newCell(char, cengine.graphics.colorPair)
        cellList.append(newCell)

    a = x #start insert into canvas buffer at x pos
    for a, cell in enumerate(cellList):
        cengine.canvas.setCell(x + a, y, cell)
    
    return
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
def printstrw(pSTRING, pXPOS, pYPOS, pWRAP):
    
    space = " "
    words = pSTRING.split(" ")
    lines = []
    
    currLine = ""
    for a in range(0, len(words)):        
        currLength = len(currLine) + len(words[a]) + len(" ")
        if currLength > pWRAP:            
            lines.append(currLine)
            currLine = str(words[a]) + " "
        elif currLength <= pWRAP:            
            currLine = currLine + str(words[a]) + " "    
    lines.append(currLine)
    
    x = pXPOS
    y = pYPOS
    for line in lines:
        cellList = []    
        for char in str(line):
            newCell = cengine.graphics.newCell(char, cengine.graphics.colorPair)
            cellList.append(newCell)
        a = x #start insert into canvas buffer at x pos
        for a, cell in enumerate(cellList):
            cengine.canvas.setCell(x + a, y, cell)
        y += 1
    
    return y
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
def addstr(pXPOS, pYPOS, pCANVASCHAR): 
    global cengine    
    
    #check and ensure the addstr operation is within screen boundries
    #as to not throw a curses draw exception. If out of bounds don't draw.
    #NOTE: if very large canvases are not properly restrained during looping 
    #in the cengine.draw() operation will cause very slow draws
    if pXPOS <= cengine.graphics.getWidth() and pXPOS >= 0:
        if pYPOS <= cengine.graphics.getHeight() and pYPOS >=0:
            string = str(pCANVASCHAR[0])                        
            cengine.screen.addstr( pYPOS, pXPOS, string, curses.color_pair(pCANVASCHAR[1]) )

    return
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::