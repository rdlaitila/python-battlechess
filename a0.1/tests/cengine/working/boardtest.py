import sys, os, cengine, time

#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
def cengine_load():
    return
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
def cengine_update():     
    return
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
def cengine_draw():
    
    boardWidth = 65
    boardHeight = 21
    boardXStep = 8
    boardYStep = 4
    
    #cengine.graphics.setBackgroundColor("WHITE")
    
    cengine.graphics.setColor("WHITE", "WHITE")
    cengine.graphics.rectangle("FILL", " ", 0, 0, boardWidth, boardHeight)
    cengine.graphics.setColor("BLACK", "RED")    
    cengine.graphics.rectangle("line", " ", 0, 0, boardWidth, boardHeight)
    
    cengine.graphics.line(" ", 0, boardYStep * 1, boardWidth-1, boardYStep * 1)
    cengine.graphics.line(" ", 0, boardYStep * 2, boardWidth-1, boardYStep * 2)
    cengine.graphics.line(" ", 0, boardYStep * 3, boardWidth-1, boardYStep * 3)
    cengine.graphics.line(" ", 0, boardYStep * 4, boardWidth-1, boardYStep * 4)
    
    cengine.graphics.line(" ", boardXStep * 1, 0,  boardXStep * 1, boardHeight-1)
    cengine.graphics.line(" ", boardXStep * 2, 0,  boardXStep * 2, boardHeight-1)
    cengine.graphics.line(" ", boardXStep * 3, 0,  boardXStep * 3, boardHeight-1)
    cengine.graphics.line(" ", boardXStep * 4, 0,  boardXStep * 4, boardHeight-1)
    cengine.graphics.line(" ", boardXStep * 5, 0,  boardXStep * 5, boardHeight-1)
    cengine.graphics.line(" ", boardXStep * 6, 0,  boardXStep * 6, boardHeight-1)
    cengine.graphics.line(" ", boardXStep * 7, 0,  boardXStep * 7, boardHeight-1)
    
    #BOARD NUMBERS
    cengine.graphics.setColor("BLACK", "RED")
    cengine.graphics.printstr("A", 4, 20)
    cengine.graphics.printstr("B", 12, 20)
    cengine.graphics.printstr("C", 20, 20)
    cengine.graphics.printstr("D", 28, 20)
    cengine.graphics.printstr("E", 36, 20)
    cengine.graphics.printstr("F", 44, 20)
    cengine.graphics.printstr("G", 52, 20)
    cengine.graphics.printstr("H", 60, 20)
    cengine.graphics.printstr("5", 0, 2)
    cengine.graphics.printstr("4", 0, 6)
    cengine.graphics.printstr("3", 0, 10)
    cengine.graphics.printstr("2", 0, 14)
    cengine.graphics.printstr("1", 0, 18)
    
    #BLACK ROYAL ROW
    cengine.graphics.setColor("MAGENTA", "WHITE")
    cengine.graphics.rectangle("LINE", "@", 2, 1, 5, 3)
    cengine.graphics.rectangle("LINE", "@", 58, 1, 5, 3)
    
    #BLACK PAWNS
    cengine.graphics.setColor("MAGENTA", "WHITE")
    cengine.graphics.circle("+", 4, 6, 1)
    cengine.graphics.circle("+", 12, 6, 1)
    cengine.graphics.circle("+", 20, 6, 1)
    cengine.graphics.circle("+", 28, 6, 1)
    cengine.graphics.circle("+", 36, 6, 1)
    cengine.graphics.circle("+", 44, 6, 1)
    cengine.graphics.circle("+", 52, 6, 1)
    cengine.graphics.circle("+", 60, 6, 1)
    
    #WHITE
    cengine.graphics.setColor("BLACK", "WHITE")
    cengine.graphics.circle("+", 4, 14, 1)
    cengine.graphics.circle("+", 12, 14, 1)
    cengine.graphics.circle("+", 20, 14, 1)
    cengine.graphics.circle("+", 28, 14, 1)
    cengine.graphics.circle("+", 36, 14, 1)
    cengine.graphics.circle("+", 44, 14, 1)
    cengine.graphics.circle("+", 52, 14, 1)
    cengine.graphics.circle("+", 60, 14, 1)
    
    #WHITE ROYAL ROW
    cengine.graphics.setColor("BLACK", "WHITE")
    cengine.graphics.rectangle("LINE", "@", 2, 17, 5, 3)
    cengine.graphics.rectangle("LINE", "@", 58, 17, 5, 3)
    
    
    #MENU
    cengine.graphics.setColor("WHITE", "BLACK")
    cengine.graphics.printstr("-=MENU=-", 69, 1)
    cengine.graphics.printstr("1.) Move", 67, 2)
    cengine.graphics.printstr("2.) Taunt", 67, 3)
    cengine.graphics.printstr("3.) Chat", 67, 4)
    cengine.graphics.printstr("4.) Exit", 67, 5)
    
    return
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
def cengine_keypressed(keycode):
  
    return
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
def cengine_exit():
    cengine.cls()
    print "Attaching Beards to Dwarves..."
    time.sleep(1)
    print "BuhBy!"
    time.sleep(1)
    return
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
cengine.registerCallBack("load", cengine_load) #calls this UDF after the internal cengine.load() method is called
cengine.registerCallBack("update", cengine_update) #calls this UDF after the internal cengine.update() method is called
cengine.registerCallBack("draw", cengine_draw) #calls this UDF after the internal cengine.draw() method is called
cengine.registerCallBack("keypressed", cengine_keypressed) #calls this UDF after the internal cengine.keypressed() method is called
cengine.registerCallBack("exit", cengine_exit) #calls this UDF before the internal cengine.exit() method is called
cengine.init() #kick off the cengine program loop

