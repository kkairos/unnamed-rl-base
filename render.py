import tcod
import tcod.event as tcv
import constants

# Movement
def draw_all(map_console,entities):
	for x in entities:
		draw_e(map_console,x)
	
def clear_all(map_console,entities):
	for x in entities:
		clear_e(map_console,x)

def draw_e(map_console,x):
	tcod.console_set_default_foreground(map_console,constants.COLORS[x.fg])
	map_console.put_char(x.x, x.y, x.char, x.bg)
	
def clear_e(map_console,x):
	map_console.put_char(x.x, x.y, ord(" "), tcod.BKGND_DEFAULT)

def draw_map(map,map_console):
	for y in range(map_console.height):
		for x in range(map_console.width):
			tcod.console_set_default_foreground(map_console,map.t_[x][y].fg)
			tcod.console_set_default_background(map_console,map.t_[x][y].bg)
			map_console.put_char(x, y, map.t_[x][y].char, tcod.BKGND_DEFAULT)

def draw_con(main_console,map_console):
	map_console.blit(
		main_console,
		0,1, #dest
		0,0, #src
		80,25, #w&h
		1.0,1.0, #fg,bg alpha
		None
		)