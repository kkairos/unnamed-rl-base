import constants
from random import randint

class Tile:

	def __init__(self,block_m,block_s=None,char=0,fg=15,bg=0):
		self.block_m = block_m
		if block_s is None:
			block_s = block_m
		self.block_s = block_s
		self.char = char
		self.fg = constants.COLORS[fg]
		self.bg =  constants.COLORS[bg]

def newtile(terrain):
	return Tile(
		terrain["block_m"],
		terrain["block_s"],
		terrain["char"],
		terrain["fg"],
		terrain["bg"]
		)

class Map:

	def __init__(self,width,height):
		self.width = width
		self.height = height
		self.t_ = self.t_init()
		
	def t_init(self):
		tiles = [[newtile(constants.TERRAIN["floor"]) for y in range(self.height)] for x in range(self.width)]
		
		for y in range(self.height):
			for x in range(self.width):
				tiles[x][y] = newtile(constants.TERRAIN["floor"])

		for y in range(self.height):
			for x in range(self.width):
				if y==0 or x==0 or (y==self.height-1) or (x==self.width-1):
					tiles[x][y] = newtile(constants.TERRAIN["wall"])
		return tiles

def tunnel_h(map,x0,x1,y):
	for x in range(x0,x1+1):
		map.t_[x][y] = newtile(constants.TERRAIN["floor"])
		
def tunnel_v(map,y0,y1,x):
	for y in range(y0,y1+1):
		map.t_[x][y] = newtile(constants.TERRAIN["floor"])

def wall_h(map,x0,x1,y):
	for x in range(x0,x1+1):
		map.t_[x][y] = newtile(constants.TERRAIN["wall"])
		
def wall_v(map,y0,y1,x):
	for y in range(y0,y1+1):
		map.t_[x][y] = newtile(constants.TERRAIN["wall"])

def make_map(map):
	return
	
def divide_map(map):
	return