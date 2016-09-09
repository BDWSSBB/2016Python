class WallKeycode:
    tile_walls = [ #True/False for North, East, South, West walls
                [False, False, False, False], #a
                [True, False, False, False], #b  -
                [False, True, False, False], #c   |
                [False, False, True, False], #d  _
                [False, False, False, True], #e |
                [True, True, False, False], #f  -|
                [True, False, True, False], #g  =
                [True, False, False, True], #h |-
                [False, True, True, False], #i  _|
                [False, True, False, True], #j | |
                [False, False, True, True], #k |_
                [True, True, True, False], #l  =|
                [True, True, False, True], #m |-|
                [True, False, True, True], #n |=
                [False, True, True, True], #o |_|
                [True, True, True, True] #p |=|
                ]
    tile_characters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p"]
