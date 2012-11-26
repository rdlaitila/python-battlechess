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
		self.games.append(newGame)
		print "Created new game: " + str(newGame.gid)
		return newGame.gid		
	def FlushGame(self): return
	#------------------------------------------------------------------
	def LoadGame(self): return
	#------------------------------------------------------------------
	def ReadCmd(self, CMD):
		cmdParts = CMD.split( ":", len(CMD) )
		if cmdParts[0] == "NEW":
			return self.NewGame()
			
		print cmdParts
	#------------------------------------------------------------------		
	def ParseMsg(self):	
		connection, address = self.serversocket.accept()
		buf = connection.recv(64)		
		print "Recieved:" + str(buf)
		response = self.ReadCmd(str(buf))		
		#connection.send("server received:" + response)	
		
		return	
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
	
######################################################################
# OBJ GAME
######################################################################
class Game():
	def __init__(self):
		self.gid = random.randint(0,101)
		self.board = Board()
		self.currPlayer = None
	
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
			[ Space(0,0), Space(0,1), Space(0,2), Space(0,3), Space(0,4) ],
			[ Space(1,0), Space(1,1), Space(1,2), Space(1,3), Space(1,4) ],
			[ Space(2,0), Space(2,1), Space(2,2), Space(2,3), Space(2,4) ],
			[ Space(3,0), Space(3,1), Space(3,2), Space(3,3), Space(3,4) ],
			[ Space(4,0), Space(4,1), Space(4,2), Space(4,3), Space(4,4) ],
			[ Space(5,0), Space(5,1), Space(5,2), Space(5,3), Space(5,4) ],
			[ Space(6,0), Space(6,1), Space(6,2), Space(6,3), Space(6,4) ],
			[ Space(7,0), Space(7,1), Space(7,2), Space(7,3), Space(7,4) ]
		]
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

######################################################################
# OBJ SPACE
######################################################################
class Space():
	def __init__(self, XPOS, YPOS):
		self.xPos = XPOS
		self.yPos = YPOS
		self.currPeice = None
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

######################################################################
# OBJ PIECE
######################################################################
class Piece():
	def __init__(self): return
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::	
Main()
