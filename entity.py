import constants as cx
import render as re

class Entity:

	def __init__(self,
			x,y,
			char_input = 2,
			fg = 15,bg = 0,
			hp = 10,speed = 10,
			faction = cx.Faction.Enemy,
			block_m = True,
			dispname = ""):
		self.x = x
		self.y = y
		self.char = char_input
		self.fg = fg
		self.bg = bg
		self.stats = Stats(hp,speed)
		self.block_m = block_m
		self.faction = faction
		self.dispname = dispname
		
	def move(self,dx,dy,map,entities,message_console,messages):
		if (self.x+dx > -1 and self.x+dx < map.width and self.y+dy > -1 and self.y+dy < map.height):
			
			target_entity = blocking_entity(entities,self.x+dx,self.y+dy)
			if target_entity is not None:
				if target_entity.faction == self.faction:
					self.talk(target_entity,message_console,messages)
				elif target_entity.faction != self.faction:
					self.attack(target_entity,message_console,messages)
			elif map.t_[self.x+dx][self.y+dy].block_m:
				re.messageprint(message_console,"You're blocked in that direction!",messages)
			else:
				self.x+=dx
				self.y+=dy

	def talk(self,other,message_console,messages):

		message = re.construct_message(self,other," talk to ", " talks to ")
		re.messageprint(message_console,message,messages)
	
	def attack(self,other,message_console,messages):
	
		damage = self.stats.at - other.stats.df
		message = re.construct_message(self,other," attack ", " attacks "," for ",damage," HP")
		other.stats.hp -= damage
		if other.stats.hp < 1:
			message += " " + re.construct_message(other,other," die"," dies","",0,"","!",True)
			other.block_m = False
			other.char = ord("%")
		re.messageprint(message_console,message,messages)
		
def blocking_entity(entities,x,y):
	for entity in entities:
		if ((entity.x == x) and (entity.y == y) and entity.block_m):
			return entity
	return None

class Stats:

	def __init__(self,hp,speed, at=3, df=0):
		self.hp = hp
		self.max_hp = hp
		self.speed = speed
		self.at = at
		self.df = df