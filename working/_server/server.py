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
		self.serversocket 	= None
		self.games 			= []
		self.clientsockets 	= []
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
	def NewGame(self):
		newGame = Game()		
		print "Created new game: " + str(newGame.gid)		
		return newGame
	def FlushGame(self): return
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
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

######################################################################
# OBJ PLAYER
######################################################################
class Player():
	def __init__(self):
		self.pid = ""		
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

    def buildpiece(self, who):

	piecetype = who[:1]
	color = who[1:2]

	if piecetype is "r":
		self.name = "Rook"

	elif piecetype is "k":
		self.name = "Knight"

	elif piecetype is "b":
                self.name = "Bishop"

	elif piecetype is "q":
                self.name = "Queen"

	elif piecetype is "K":
                self.name = "King"

	elif piecetype is "p":
                self.name = "Pawn"

	if color is "w":
		self.color = "White"

	elif color is "b":
		self.color = "Black"


    def __init__(self, whoami):
        self.whoami = whoami
	self.buildpiece(str(whoami))
	return

#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

######################################################################
# OBJ WARDEN
######################################################################
class Warden():
    def move(self, S1, S2):

	print S1.piece.name

	if S1.piece.name is "r":
		print "Rook"

	elif S1.piece.name is "k":
		print "King"

	elif S1.piece.name is "b":
		print "Bishop"

	elif S1.piece.name is "q":
		print "Queen"

	elif S1.piece.name is "K":
		print "King"

	elif S1.piece.name is "p":
		print "Pawn"


    def __init__(self, GAME):
        self._game = GAME
        return   
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
Main()
