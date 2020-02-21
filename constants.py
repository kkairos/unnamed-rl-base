COLORS = {
	15 : (255,255,255),
	14 : (255,255,84),
	13 : (255,84,255),
	12 : (255,84,84),
	11 : (84,255,255),
	10 : (84,255,84),
	9 : (84,84,255),
	8 : (84,84,84),
	7 : (168,168,168),
	6 : (168,84,0),
	5 : (168,0,168),
	4 : (168,0,0),
	3 : (0,168,168),
	2 : (0,168,0),
	1 : (0,0,168),
	0 : (0,0,0)
	}

INPUT_SETTINGS = 0

"""
0: numpad + arrows
1: QWEASDZXC + arrows
"""

TERRAIN = {
	"wall": {
		"block_m" : True,
		"block_s" : True,
		"char" : ord("#"),
		"fg" : 7,
		"bg" : 0,
		"type" : "wall"
		},
	"floor" : {
		"block_m" : False,
		"block_s" : False,
		"char" : 249,
		"fg" : 7,
		"bg" : 0,
		"type" : "floor"
		}
	}