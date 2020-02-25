import tcod, tcod.event
from controls import key_input
import entity as ec
import render as re
import constants
import map

screen_width = 80
screen_height = 25

tcod.console_set_custom_font(constants.FONT_DAT[constants.FONT_SEL]["file"],
		tcod.FONT_TYPE_GREYSCALE | tcod.FONT_LAYOUT_ASCII_INROW,
		32,8
		)
		
main_console = tcod.console_init_root(screen_width, screen_height, "D@N ROGUE", False, 3, "F", True)

printqueue = []
printqueue.append("Hallo world!")
fontstring = "testing font " + str(constants.FONT_SEL) + ": " + constants.FONT_DAT[constants.FONT_SEL]["name"] + ", " + constants.FONT_DAT[constants.FONT_SEL]["file"]
printqueue.append(fontstring)
printqueue.append("Pleasure to meet you.")
printqueue.append("The quick brown fox jumps over the lazy dog.")
printqueue.append("THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG!")
printqueue.append("the quick brown fox jumps over the lazy dog?")



lc = 1

for line in printqueue:
	main_console.print(2,lc,line,constants.COLORS[15],constants.COLORS[0],tcod.BKGND_DEFAULT,tcod.LEFT)
	print(line)
	lc+=1

re.console_borders(main_console,0,0,main_console.width-1,main_console.height-1)

ingame = True
while ingame:
	tcod.console_flush()
	for event in tcod.event.wait():
		if event.type == "KEYDOWN":
			action = key_input(event.sym)
			move = False
			exit = False
			pause = False
			pause = action.get('pause')
			exit = action.get('exit')
			if exit or pause:
				ingame = False