import tcod, tcod.event
from controls import key_input
import entity as ec
import render as re
import constants
import map

def menu(main_console,menu_console):

	re.draw_con(main_console,menu_console)
	tcod.console_flush()
	while True:
		for event in tcod.event.wait():
			if event.type == "KEYDOWN":
				action = key_input(event.sym)
				move = False
				exit = False
				pause = False
				pause = action.get('pause')
				exit = action.get('exit')
				if exit or pause:
					return

def main():

	print(constants.COLORS)
	
	printqueue = []
	printqueue.append("Hallo world!")
	printqueue.append("Pleasure to meet you.")
	for line in printqueue:
		print(line)
	
	screen_width = 80
	screen_height = 25
	map_w = 80
	map_h = 21
	
	level_map = map.Map(map_w,map_h)
	
	player = ec.Entity(int(level_map.width/2),int(level_map.height/2),ord("@"),15,0)
	
	npc = ec.Entity(int(level_map.width*3/4),int(level_map.height*1/4),ord("@"),14,0)
	
	entities = [player,npc]
	
	print(str(player.x) + " " + str(player.y) + " " + chr(player.char))
	
	key = tcod.Key()
	mouse = tcod.Mouse()
	
	tcod.console_set_custom_font("courier8x14.png",
		tcod.FONT_TYPE_GREYSCALE | tcod.FONT_LAYOUT_ASCII_INROW,
		32,8
		)
	main_console = tcod.console_init_root(screen_width, screen_height, "D@N ROGUE", False, 3, "F", True)
	
	map_console = tcod.console.Console(map_w, map_h, "F", None)
	menu_console = tcod.console.Console(map_w, map_h, "F", None)
	
	menu_console.print(int(menu_console.width/2),int(menu_console.height/2)-1,"G A M E   P A U S E D",constants.COLORS[15],constants.COLORS[0],tcod.BKGND_DEFAULT,tcod.CENTER)
	menu_console.print(int(menu_console.width/2),int(menu_console.height/2)+1,"Enter to Resume",constants.COLORS[15],constants.COLORS[0],tcod.BKGND_DEFAULT,tcod.CENTER)
	
	fg_sh = 15
	bg_sh = 0
	
	while True:
	
		re.draw_map(level_map,map_console)
		re.draw_all(map_console,entities)
		re.draw_con(main_console,map_console)
		tcod.console_flush()
		re.clear_all(map_console,entities)
		for event in tcod.event.wait():
			if event.type == "KEYDOWN":
				action = key_input(event.sym)
				move = False
				exit = False
				pause = False
				move = action.get('move')
				exit = action.get('exit')
				pause = action.get('pause')
				if move:
					dx,dy = move
					player.move(dx,dy,level_map)
				if exit:
					return True
				if pause:
					menu(main_console,menu_console)
			elif event.type == "WINDOWCLOSE":
				return True

if __name__ == "__main__":
	main()