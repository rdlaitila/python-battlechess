import sys, socket, uuid, os, curses

menu = [
"########     ###    ######## ######## ##       ########",
"##     ##   ## ##      ##       ##    ##       ##      ",
"##     ##  ##   ##     ##       ##    ##       ##      ",
"########  ##     ##    ##       ##    ##       ######  ",
"##     ## #########    ##       ##    ##       ##      ",
"##     ## ##     ##    ##       ##    ##       ##      ",
"########  ##     ##    ##       ##    ######## ########",
"                                                       ",
"      ######  ##     ## ########  ######   ######      ",
"     ##    ## ##     ## ##       ##    ## ##    ##     ",
"     ##       ##     ## ##       ##       ##           ",
"     ##       ######### ######    ######   ######      ", 
"     ##       ##     ## ##             ##       ##     ", 
"     ##    ## ##     ## ##       ##    ## ##    ##     ", 
"      ######  ##     ## ########  ######   ######      ",
"                                                       ",
"                  2012 Ver 1.0 Client                  ",
"                                                       ",
"     1.)New Match                                      ",
"     2.)Resume Match                                   ",
"     3.)Join Match                                     ",
"     4.)Quit                                           "]

client = None
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
def Main():
    global client
    
    client = Client()
    client.screen.keypad(1)
    curses.noecho()
    curses.curs_set(0)       
    
    while True: 
        draw()
        update()
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
def update():
    global client
    
    if client.state == "MENU":
        event = client.screen.getch()
        if event == ord("1"):
            client.state = "NEWGAME"
            return
        elif event == ord("2"):
            return
        elif event == ord("3"):
            return
        elif event == ord("4"): 
            client.quit()
    elif client.state == "NEWGAME":
        curses.echo()
        curses.cbreak()
        buff = ""
        while 1:            
            event = client.screen.getch()
            buff = buff + str(unichr(event))
            if event == 27:
                client.state = "MENU"
                curses.noecho()
                curses.curs_set(0)           
                break
            elif event in (10, curses.KEY_ENTER):
                client.screen.addstr(1, 0, "You entered: " + str(buff) )
                response = client.send( "127.0.0.1", 28000, str(client.cid) + ":" + "0" + ":NEW:" + str(buff).rstrip() )
                client.screen.addstr(2, 0, str(response) )
                client.screen.addstr(3, 0, "[ESC to exit]" )                
                #break
    elif client.state == "RESUMELIST": 
        return
    elif client.state == "GAMELIST": 
        return
    elif client.state == "GAME":
        
        return        
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
def draw():
    global client
    global menu        
    
    client.screen.clear()
    curses.noecho()
    curses.curs_set(0)
    
    if client.state == "MENU":        
        for a, str in enumerate(menu):
            client.screen.addstr(a, 0, menu[a])
    elif client.state == "NEWGAME":        
        client.screen.addstr(0, 0, "Enter game name: ")
    elif client.state == "RESUMELIST": return
    elif client.state == "GAMELIST": return
    elif client.state == "GAME": return  

#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
def cls():
    if os.name == "posix":
        os.system('clear') #on linux
    elif os.name == "nt":   
        os.system('cls') #on windows
    else: return False
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::



######################################################################
# OBJ CLIENT
######################################################################
class Client():
    def __init__(self):
        self.id         = str(uuid.getnode())
        self.gid        = "0" #no game 
        self.screen     = curses.initscr()
        self.commands   = ["NEW", "LOA", "END", "LIS" "MOV"]
        self.state      = "MENU" #MENU, NEWGAME, RESUMELIST, GAMELIST, GAME
        
        #load CID
        try:
            f = open("CID", "r")
            self.cid = str(f.read())                
        except:        
            f = open("CID", "w")            
            f.write(self.cid)
    def Send(self, IP, PORT, DATA):
        clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        clientsocket.connect((IP, PORT)) 
        clientsocket.send(DATA)
        response = clientsocket.recv(64)
        clientsocket.close()
        return response
    def Receive(self, RESPONSE): return        
    def Quit(self):                
        curses.endwin()
        quit()
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
Main()