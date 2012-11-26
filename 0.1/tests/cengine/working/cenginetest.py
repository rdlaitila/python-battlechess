import sys, os, cengine, time

pause = False
lastkey = "0"
debug = False
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
def cengine_load():
    return
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
def cengine_update():     
    return
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
def cengine_draw():
    global pause
    global lastkey
    global debug
    
    if pause == False:
        xTranslate = cengine.canvas.xTranslate
        yTranslate = cengine.canvas.yTranslate
        
        xTO = (xTranslate) * (-1)
        yTO = (yTranslate) * (-1)
        
        cengine.graphics.setColor("BLACK", "RED")     
        
        intro = """Welcome to cEngine. The only curses based 2d terminal game engine written from the ground up to provide the best 2d unicode terminal gaming experience in the world. Please view the samples below to see the power of cEngine! Soon you will be playing with you old friends such as carrot ^ pipe | and pound #. Much fun to be had!! use arrow UP/DOWN to scroll through the samples."""                
        txtbottom = cengine.graphics.printstrw(intro, 0, 1, cengine.graphics.getWidth())
        
        cengine.graphics.printstr( "Keys: [q] QUIT [d] DEBUG [p] PAUSE [down arrow] SCROLL DOWN [up arrow] SCROLL UP", 0, txtbottom)
        
        cengine.graphics.setColor("Black", "WHITE")        
        
        cengine.graphics.rectangle( "LINE", "#", 0, txtbottom + 2, 14, 12 )
        cengine.graphics.printstr( "Rectangle", 2, txtbottom + 4 )
        
        cengine.graphics.setColor("GREEN", "BLACK")
        
        cengine.graphics.line( "#", 16, txtbottom + 2, 40, txtbottom + 6 ) 
        cengine.graphics.printstr( "Line", 16, txtbottom + 4 )
        
        cengine.graphics.setColor("CYAN", "BLACK")
        
        cengine.graphics.circle("#", 50, txtbottom + 7, 5)
        cengine.graphics.printstr("Circle", 47, txtbottom + 6)
        
        if debug:
            #DEBUG BOX DRAW LAST
            cengine.graphics.rectangle("FILL", " ", 0 + xTO, 0 + yTO, cengine.graphics.getWidth(), 5 )        
            cengine.graphics.printstr( "-=cEngine Demo Debug=-", 0 + xTO, 0 + yTO )
            cengine.graphics.printstr(  "Clock:" + str(time.clock()) + " Updates: " + str(cengine.updates) + " Draws: " + str(cengine.draws), 0 + xTO, 1 + yTO)         
            cengine.graphics.printstr( "Last Keycode: " + str(lastkey), 0 + xTO, 2 + yTO)            
            cengine.graphics.printstr( "Canvas Draw Operation Translate: (" + str(xTranslate) + "," + str(yTranslate) + ")", 0 + xTO, 3 + yTO)
            cengine.graphics.line( "-", 0 + xTO, 4 + yTO, cengine.graphics.getWidth() + xTO, 4 + yTO )        
        #time.sleep(1)
        
    return
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
def cengine_keypressed(keycode):
    global lastkey
    global pause
    global strbuff
    global debug
    lastkey =  str(keycode)    
    
    if keycode == 113: #char(q)
        cengine.exit()
    elif keycode == 100: 
        if debug == True: debug = False
        elif debug == False: debug = True    
    elif keycode == 258:
        cengine.canvas.yTranslate -= 1
    elif keycode == 259:
        cengine.canvas.yTranslate += 1
    elif keycode == 112: #char(p)
        if pause == True: pause = False
        elif pause == False: pause = True    
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

