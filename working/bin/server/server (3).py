import sys, os, threading, socket, random


server = None
serversocket = ""
clientsockets = []
games = []

#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
def Main():

    global server
    server = Server()
    server.Start("0.0.0.0", 28000, 2)
    
    while True:
        server.ParseMsg()        
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::


######################################################################
# OBJ SERVER
######################################################################
class Server():
    #------------------------------------------------------------------
    def __init__(self):    
        self.sid = None
        self.serversocket     = None
        self.games             = []
        self.clientsockets     = []
    #------------------------------------------------------------------
    def Start(self, IP, PORT, CONNLIMIT):         
        self.serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.serversocket.bind( (IP, PORT) ) 
        self.serversocket.listen(CONNLIMIT)
        print "Server started " + str(IP) + ":" + str(PORT)
        return
    #------------------------------------------------------------------
    def Stop(self): return
    #------------------------------------------------------------------
    def checkGid(self,theNewGame):
        #check to see if a new gid is valid.
        for game in self.games:
            if( theNewGame.gid == game.gid) :
                return False;
            if (theNewGame.gid > 100):
                theNewGame.gid = 1;
        return True;
    #------------------------------------------------------------------
    def NewGame(self):
        #instantiate a new game and return the instance 
        
        newGame = Game()
        
        while (~self.checkGid(newGame)):
            newGame.gid += 1;
        print "Created new game: " + str(newGame.gid)        
        return newGame
    def FlushGame(self): 
        #ideally this should remove the game from the self.games array.
        return
    #------------------------------------------------------------------
    def LoadGame(self): return
    #------------------------------------------------------------------
    def ReadCmd(self, CMD):
        cmdParts = CMD.split( ":", len(CMD) )
        if cmdParts[1] == "NEW":
            game = self.NewGame()
            self.games.append(game)
            print "--GAMES---------"
            for x in range(0, len(self.games)):
                print "GID:" + str(self.games[x].gid)
            print "            "
            return "TRUE:"+str(game.gid)
    #------------------------------------------------------------------
    def ParseMsg(self):
        connection, address = self.serversocket.accept()
        buf = connection.recv(64)    
        print "Server Received: " + str(buf)        
        #print "Recieved:" + str(buf)
        response = self.ReadCmd(str(buf))        
        print "Sending Response: " + str(response)
        connection.send(str(response))            
        return    
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    
######################################################################
# OBJ GAME
######################################################################
class Game():
    def __init__(self):
        self.gid = random.randint(0,101)
        self.board = Board()
        self.warden = Warden(self)
        self.players = [Player(),Player()]
        self.movingColor = "w";
        #need to define a way to get player names.
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

######################################################################
# OBJ PLAYER
######################################################################
class Player():
    def __init__(self):
        self.pid = ""
        #might be good to query client to get player info. 
######################################################################
# OBJ BOARD
######################################################################
class Board():
    def __init__(self):
        self.spaces = [
        [ Space("rw",0,0), Space("kb",0,1), Space("bb",0,2), Space("qb",0,3), Space("Kb",0,4), Space("bb",0,5), Space("kb",0,6), Space("rb",0,7) ],
            [ Space("pw",1,0), Space("pb",1,1), Space("pb",1,2), Space("pb",1,3), Space("pb",1,4), Space("pb",1,5), Space("pb",1,6), Space("pb",1,7) ],
            [ Space("e",2,0), Space("e",2,1), Space("e",2,2), Space("e",2,3), Space("e",2,4), Space("e",2,5), Space("e",2,6), Space("e",2,7) ],
            [ Space("pb",3,0), Space("pw",3,1), Space("pw",3,2), Space("pw",3,3), Space("pw",3,4), Space("pw",3,5), Space("pw",3,6), Space("pw",3,7) ],
            [ Space("rb",4,0), Space("kw",4,1), Space("bw",4,2), Space("qw",4,3), Space("Kb",4,4), Space("bw",4,5), Space("kw",4,6), Space("rw",4,7) ]
        ]
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

######################################################################
# OBJ SPACE
######################################################################
class Space():
    def __init__(self, PIECE, XPOS, YPOS):
        self.xPos = XPOS
        self.yPos = YPOS
        self.currPiece = Piece(PIECE)        

#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

######################################################################
# OBJ PIECE
######################################################################
class Piece():
    #defines a piece's identity.
    def __init__(self, whoami):
        self.whoami = whoami
        self.buildpiece(str(whoami));
        
        # validMoves will describe all possible
        # changes in coordinates for valid moves by that piece.
        # example:
        #    knight can only be (x+1,y+2), (x-1,y+2), (x-1,y-2),(x+1,y-2)
        # for the pawn I've defined validCaptures separately from moves alone.
        # ...the size of the board notwithstanding. 
        # validCaptures will define valid capture moves for the pawn.
        self.validMoves = [];
        return self;

    def buildpiece(self, who):
    
        piecetype = who[:1]
        color = who[1:2]
        if piecetype is "r":
            self.name = "Rook"
            self.validMoves = [ (0, 1),(0, 2),(0, 3),(0, 4),(0, 5),(0, 6), #-
                                (0,-1),(0,-2),(0,-3),(0,-4),(0,-5),(0,-6), #
                                (1, 0),(2, 0),(3, 0),(4, 0),(5, 0),(6, 0), # cardinals
                                (-1,0),(-2,0),(-3,0),(-4,0),(-5,0),(-6,0)]; #-
            self.validCaptures  = False;
        elif piecetype is "k":
            self.name = "Knight"
            self.validMoves = [ (1,2) , (-1, 2) , (1,-2),(-1,-2) ];
            self.validCaptures  = False;
        elif piecetype is "b":
            self.name = "Bishop"
            self.validMoves = [ (1,  1), (2,  2), (3,  3), (4,  4),#-
                                (1, -1), (2, -2), (3, -3), (4, -4),#
                                (-1, 1), (-2, 2), (-3, 3), (-4, 4), # diagonals
                                (-1,-1), (-2,-2), (-3,-3), (-4,-4) ];#-
            self.validCaptures  = False;
        elif piecetype is "q":
            self.name = "Queen"
            self.validMoves = [ (1,  1), (2,  2), (3,  3), (4,  4), #-
                                (1, -1), (2, -2), (3, -3), (4, -4), #
                                (-1, 1), (-2, 2), (-3, 3), (-4, 4), # diagonals
                                (-1,-1), (-2,-2), (-3,-3), (-4,-4), #-
                                (0, 1),(0, 2),(0, 3),(0, 4),(0, 5),(0, 6), #-
                                (0,-1),(0,-2),(0,-3),(0,-4),(0,-5),(0,-6), #
                                (1, 0),(2, 0),(3, 0),(4, 0),(5, 0),(6, 0), # cardinals
                                (-1,0),(-2,0),(-3,0),(-4,0),(-5,0),(-6,0)]; #-
            self.validCaptures  = False;
        elif piecetype is "K":
            self.name = "King"
            self.validMoves = [ (0,1), (0,-1), ( 1,0), (-1, 0), # move one space any direction
                                (1,1), (1,-1), (-1,1), (-1,-1)]; #
            self.validCaptures  = False;
        elif piecetype is "p":
            self.name = "Pawn"
            self.validMoves =    [ (0,1)        ];
            self.validCaptures = [ (1,1), (-1,1)];
            #pawn is also the only pieces whose valid moves depend on its orientation.
            if color is "b":
                self.validMoves =    [ (0,-1)        ];
                self.validCaptures = [ (1,-1), (-1,-1)];    
                
        if color is "w":
            self.color = "White"
        elif color is "b":
            self.color = "Black"





#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

######################################################################
# OBJ WARDEN
######################################################################
class Warden():
    def move(self, S1, S2):

        print("Attempted move by " + S1.piece.color + " " + S1.piece.name +"!")

        validMove = self.isValidMove(S1,S2);
        if (~validMove): print("Not a valid move for " + S1.piece.name);
        else: print("Valid move by " + S1.piece.color + " " + S1.piece.name +"!")
        
        #NOT YET IMPLEMENTED - check if we're putting the king in check with this move. 
        # If so, change variable in the game so isValidMove can analyze it.  
        
        #NOT YET IMPLEMENTED - do the move.
        
        #update the turn.
        if (self.movingColor =="White"): 
            self.movingColor = "Black"
        else:
            self.movingColor = "White";
        
    
    #------------------------------------------------------------------
    def isValidMove(self,S1, S2):
        #THESE VARIABLES need to be defined in the Turn class.
        validMove = False;
        kingInCheck = False;
        kingMovingIntoCheck = False;
        #first we need to check that the destination space is on the board.
        if ((S2.xPos > 10 ) or  (S2.xPos > 0) or (S2.yPos < 0 ) or (S2.yPos > 3 )):
            validMove = False;
            
        
        elif (kingInCheck):
            #NOT YET IMPLEMENTED  - is the king in check?
            #we should have already looked for checkmate before getting to a move.
            print "King is must move out of check!";
        elif(kingMovingIntoCheck):
            print "King cannot move into check!"
        else:
            #if we get here then the move needs to be verified by
            #the allowed movements for a given piece.
            #first calculate delta between coordinates, then see if
            # it's in the list of valid Deltas 
            diff = (S2.xPos - S1.xPos, S2.yPos - S2.yPos);
            for move in S1.piece.validMoves:
                if diff == move:
                    validMove = True;
            if S1.piece.validCaptures:
                for capture in S1.piece.validCaptures:
                    if diff == capture:
                        validMove = True;
            
            #if and only if we get here then we've gotten a validMove,
            #surely there will be more things to check. we can implement those later.
            # for instance. Would the move put the king in check?
            return validMove;
    #------------------------------------------------------------------
    def __init__(self, GAME):
        self._game = GAME;
        #white moves first
        self._game.movingColor = "White";
        return self;
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

######################################################################
# OBJ TURN
######################################################################
# A turn is used by the warden to determine who is moving and
# the list of valid moves in a given turn. 
# The Turn class will also be useful for computer AI to determine
# what moves are valid for it to make in a given Turn. 
######################################################################
class Turn():
    def __init__(self,GAME):
        self._game = GAME;
        self.movingColor = GAME.movingColor;
        self.moves = self.enumValidMoves();   
        return self;
    def enumValidMoves(self):
        moves = {};
        #moves will be a dictionary of piece names --> spaces to move into
        # a row might be "rw"
        for thisSpace in self.board.spaces:
            piecemoves = [];
            if (thisSpace.currPiece.color==self.movingColor): 
                for move in thisSpace.currPiece.validMoves:
                    newSpace = self.board.spaces[thisSpace.yPos+move[0]][thisSpace.xPos+move[1]];
                    if self._game.warden.isValidMove(thisSpace,newSpace):
                        piecemoves.append(newSpace);
    
                moves[thisSpace.currPiece.whoami] = piecemoves;
        return moves;
    
Main()
