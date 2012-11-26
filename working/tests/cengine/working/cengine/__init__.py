#import python packages
import sys, os, curses, time 
from datetime import datetime

#import cengine packages
import lib, graphics

#get global reference to cengine module
cengine = sys.modules["cengine"]

#very important globals
version = "1"
inittime = datetime.now()
screen = curses.initscr()
canvas = cengine.graphics.newCanvas( cengine.graphics.getWidth(), cengine.graphics.getHeight() )
doMainLoop = True

#global callbacks
cb_load         = None
cb_update       = None
cb_draw         = None
cb_keypressed   = None
cb_exit         = None

#stat vars
updates = 0
draws = 0
keypresses = 0

#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
def init():
    global cengine    
    
    #DO LOAD
    cengine.load()    
    cengine.cb_load()    
    
    while doMainLoop:        
        #DO UPDATE
        cengine.update()
        cengine.cb_update()
        cengine.updates+=1
        
        #DO DRAW
        #clear the screen
        cengine.screen.clear()
        
        #call UDF callback for draw operations
        cengine.cb_draw()
        
        #call internal draw function to push canvas buffer to screen
        cengine.draw()
        
        #refresh the curses screen
        cengine.screen.refresh()
        
        #clear the canvas buffer for next draw op
        cengine.canvas.clear()
        cengine.draws+=1
        
    return
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
def load():
    global cengine   
    
    #curses.echo()
    #curses.nocbreak()
    #cengine.screen.keypad(0)
    
    curses.noecho()
    curses.cbreak()
    curses.curs_set(0)    
    cengine.screen.keypad(1)
    cengine.screen.nodelay(1)
    
    curses.start_color()        
    
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_BLUE)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_CYAN)
    curses.init_pair(4, curses.COLOR_BLACK, curses.COLOR_GREEN)
    curses.init_pair(5, curses.COLOR_BLACK, curses.COLOR_MAGENTA)
    curses.init_pair(6, curses.COLOR_BLACK, curses.COLOR_RED)
    curses.init_pair(7, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.init_pair(8, curses.COLOR_BLACK, curses.COLOR_YELLOW)    
    
    curses.init_pair(9, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(10, curses.COLOR_BLUE, curses.COLOR_BLUE)
    curses.init_pair(11, curses.COLOR_BLUE, curses.COLOR_CYAN)
    curses.init_pair(12, curses.COLOR_BLUE, curses.COLOR_GREEN)
    curses.init_pair(13, curses.COLOR_BLUE, curses.COLOR_MAGENTA)
    curses.init_pair(14, curses.COLOR_BLUE, curses.COLOR_RED)
    curses.init_pair(15, curses.COLOR_BLUE, curses.COLOR_WHITE)
    curses.init_pair(16, curses.COLOR_BLUE, curses.COLOR_YELLOW) 
    
    curses.init_pair(17, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(18, curses.COLOR_CYAN, curses.COLOR_BLUE)
    curses.init_pair(19, curses.COLOR_CYAN, curses.COLOR_CYAN)
    curses.init_pair(20, curses.COLOR_CYAN, curses.COLOR_GREEN)
    curses.init_pair(21, curses.COLOR_CYAN, curses.COLOR_MAGENTA)
    curses.init_pair(22, curses.COLOR_CYAN, curses.COLOR_RED)
    curses.init_pair(23, curses.COLOR_CYAN, curses.COLOR_WHITE)
    curses.init_pair(24, curses.COLOR_CYAN, curses.COLOR_YELLOW)
    
    curses.init_pair(25, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(26, curses.COLOR_GREEN, curses.COLOR_BLUE)
    curses.init_pair(27, curses.COLOR_GREEN, curses.COLOR_CYAN)
    curses.init_pair(28, curses.COLOR_GREEN, curses.COLOR_GREEN)
    curses.init_pair(29, curses.COLOR_GREEN, curses.COLOR_MAGENTA)
    curses.init_pair(30, curses.COLOR_GREEN, curses.COLOR_RED)
    curses.init_pair(31, curses.COLOR_GREEN, curses.COLOR_WHITE)
    curses.init_pair(32, curses.COLOR_GREEN, curses.COLOR_YELLOW)
    
    curses.init_pair(33, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
    curses.init_pair(34, curses.COLOR_MAGENTA, curses.COLOR_BLUE)
    curses.init_pair(35, curses.COLOR_MAGENTA, curses.COLOR_CYAN)
    curses.init_pair(36, curses.COLOR_MAGENTA, curses.COLOR_GREEN)
    curses.init_pair(37, curses.COLOR_MAGENTA, curses.COLOR_MAGENTA)
    curses.init_pair(38, curses.COLOR_MAGENTA, curses.COLOR_RED)
    curses.init_pair(39, curses.COLOR_MAGENTA, curses.COLOR_WHITE)
    curses.init_pair(40, curses.COLOR_MAGENTA, curses.COLOR_YELLOW)
    
    curses.init_pair(41, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(42, curses.COLOR_RED, curses.COLOR_BLUE)
    curses.init_pair(43, curses.COLOR_RED, curses.COLOR_CYAN)
    curses.init_pair(44, curses.COLOR_RED, curses.COLOR_GREEN)
    curses.init_pair(45, curses.COLOR_RED, curses.COLOR_MAGENTA)
    curses.init_pair(46, curses.COLOR_RED, curses.COLOR_RED)
    curses.init_pair(47, curses.COLOR_RED, curses.COLOR_WHITE)
    curses.init_pair(48, curses.COLOR_RED, curses.COLOR_YELLOW)
    
    curses.init_pair(49, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(50, curses.COLOR_WHITE, curses.COLOR_BLUE)
    curses.init_pair(51, curses.COLOR_WHITE, curses.COLOR_CYAN)
    curses.init_pair(52, curses.COLOR_WHITE, curses.COLOR_GREEN)
    curses.init_pair(53, curses.COLOR_WHITE, curses.COLOR_MAGENTA)
    curses.init_pair(54, curses.COLOR_WHITE, curses.COLOR_RED)
    curses.init_pair(55, curses.COLOR_WHITE, curses.COLOR_WHITE)
    curses.init_pair(56, curses.COLOR_WHITE, curses.COLOR_YELLOW)
    
    curses.init_pair(57, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(58, curses.COLOR_YELLOW, curses.COLOR_BLUE)
    curses.init_pair(59, curses.COLOR_YELLOW, curses.COLOR_CYAN)
    curses.init_pair(60, curses.COLOR_YELLOW, curses.COLOR_GREEN)
    curses.init_pair(61, curses.COLOR_YELLOW, curses.COLOR_MAGENTA)
    curses.init_pair(62, curses.COLOR_YELLOW, curses.COLOR_RED)
    curses.init_pair(63, curses.COLOR_YELLOW, curses.COLOR_WHITE)
    curses.init_pair(64, curses.COLOR_YELLOW, curses.COLOR_YELLOW)
    
    cengine.graphics.colorPair = 49
    cengine.graphics.bgColorPair = 49
    
    cengine.cls()
    
    return
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
def update():
    global cengine
        
    key = " "
    #figure key presses
    try:    
        key = cengine.screen.getch()
        #key = cengine.screen.getkey()
        cengine.keypressed(key)
    except: 
        pass
    
    return
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
def draw():
    global cengine  
    
    #get the canvas buffer
    buffer = cengine.canvas.buffer
    
    xStart = 0
    xStop = len(buffer)
    yStart = 0
    yStop = len(buffer[0])
        
    #loop through and draw the background color:
    for a in range(xStart, xStop):
        for b in range(yStart, yStop):
            cengine.graphics.addstr(a, b, [" ", cengine.graphics.bgColorPair])    
    
    #loop through and draw the canvas buffer
    for a in range(xStart, xStop):
        for b in range(yStart, yStop):
            cengine.graphics.addstr(a, b, buffer[a][b])
    
    return
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
def keypressed(pKEY):
    global cengine    
    
    if pKEY != -1:
        #print str(pKEY)
        #time.sleep(2)
        cengine.cb_keypressed(pKEY)
    
    cengine.keypresses+=1
    
    return
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
def exit():
    global cengine
    
    #kill mainloop boolean
    cengine.doMainLoop = False
    
    #call user defined callback
    cengine.cb_exit()    
    
    #reset screen
    cengine.restoreScreen()
    
    #kill the app
    quit()
    sys.exit()    
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
def registerCallBack(pTYPE, pFUNC):
    global cengine    
    
    if pTYPE == "load":
        cengine.cb_load = pFUNC
    elif pTYPE == "update":
        cengine.cb_update = pFUNC
    elif pTYPE == "draw":
        cengine.cb_draw = pFUNC
    elif pTYPE == "keypressed":
        cengine.cb_keypressed = pFUNC
    elif pTYPE == "exit":
        cengine.cb_exit = pFUNC
    return
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::  
def restoreScreen():
    global cengine
    
    curses.initscr()
    curses.nocbreak()
    curses.echo()
    curses.endwin()
    return
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::  
def cls():
    if os.name == "posix":
        os.system('clear') #on linux
    elif os.name == "nt":   
        os.system('cls') #on windows
    else: return False
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::