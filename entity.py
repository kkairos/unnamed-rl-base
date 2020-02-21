class Entity:

	def __init__(self,x,y,char_input=2,fg=15,bg=0):
		self.x = x
		self.y = y
		self.char = char_input
		self.fg = fg
		self.bg = bg
	
	def move(self,dx,dy,map):
		if (self.x+dx > -1 and self.x+dx < map.width and self.y+dy > -1 and self.y+dy < map.height):
			if map.t_[self.x+dx][self.y+dy].block_m == False:
				self.x+=dx
				self.y+=dy