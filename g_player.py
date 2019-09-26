# g_player.py
# Contains all the player data

import upygame

ply01Pixels = b'\
\x12\x22\x21\x11\x11\x11\x00\x00\
\x01\x22\x22\x22\x22\x22\x10\x00\
\x00\x12\x24\x42\x22\x22\x21\x00\
\x00\x14\x42\x22\x44\x44\x22\x10\
\x00\x14\x22\x24\x11\x11\x42\x10\
\x00\x01\x42\x21\x12\x12\x12\x10\
\x00\x01\x42\x24\x11\x11\x42\x10\
\x00\x00\x14\x22\x22\x22\x21\x00\
\x00\x00\x01\x14\x44\x41\x10\x00\
\x00\x00\x01\x42\x22\x22\x10\x00\
\x00\x00\x14\x24\x22\x22\x21\x00\
\x00\x01\x42\x42\x22\x22\x21\x00\
\x00\x01\x44\x14\x42\x22\x10\x00\
\x00\x00\x11\x14\x44\x14\x41\x00\
\x00\x00\x01\x41\x14\x44\x10\x00\
\x00\x00\x00\x14\x11\x41\x00\x00\
'
ply01 = upygame.surface.Surface(16, 16, ply01Pixels)

ply02Pixels = b'\
\x12\x22\x21\x11\x11\x11\x00\x00\
\x01\x22\x22\x22\x22\x22\x10\x00\
\x00\x12\x24\x42\x22\x22\x21\x00\
\x00\x14\x42\x22\x44\x44\x22\x10\
\x00\x14\x22\x24\x11\x11\x42\x10\
\x00\x01\x42\x21\x12\x12\x12\x10\
\x00\x01\x42\x24\x11\x11\x42\x10\
\x00\x00\x14\x22\x22\x22\x21\x00\
\x00\x00\x01\x14\x44\x41\x10\x00\
\x00\x00\x01\x42\x22\x22\x10\x00\
\x00\x00\x01\x42\x42\x22\x21\x00\
\x00\x00\x01\x42\x42\x22\x21\x00\
\x00\x00\x00\x14\x42\x22\x10\x00\
\x00\x00\x00\x01\x44\x41\x00\x00\
\x00\x00\x00\x01\x44\x41\x00\x00\
\x00\x00\x00\x14\x14\x44\x10\x00\
'
ply02 = upygame.surface.Surface(16, 16, ply02Pixels)

ply03Pixels = b'\
\x12\x22\x21\x11\x11\x11\x00\x00\
\x01\x22\x22\x22\x22\x22\x10\x00\
\x00\x12\x24\x42\x22\x22\x21\x00\
\x00\x14\x42\x22\x44\x44\x22\x10\
\x00\x14\x22\x24\x11\x11\x42\x10\
\x00\x01\x42\x21\x12\x12\x12\x10\
\x00\x01\x42\x24\x11\x11\x42\x10\
\x00\x00\x14\x22\x22\x22\x21\x00\
\x00\x00\x01\x14\x44\x41\x10\x00\
\x00\x00\x01\x42\x22\x22\x10\x00\
\x00\x00\x01\x42\x42\x22\x21\x00\
\x00\x00\x00\x14\x24\x22\x21\x00\
\x00\x00\x00\x14\x24\x22\x10\x00\
\x00\x00\x00\x01\x44\x41\x00\x00\
\x00\x00\x00\x01\x44\x10\x00\x00\
\x00\x00\x00\x01\x44\x41\x00\x00\
'
ply03 = upygame.surface.Surface(16, 16, ply03Pixels)

ply04Pixels = b'\
\x12\x22\x21\x11\x11\x11\x00\x00\
\x01\x22\x22\x22\x22\x22\x10\x00\
\x00\x12\x24\x42\x22\x22\x21\x00\
\x00\x14\x42\x22\x44\x44\x22\x10\
\x00\x14\x22\x24\x11\x11\x42\x10\
\x00\x01\x42\x21\x12\x12\x12\x10\
\x00\x01\x42\x24\x11\x11\x42\x10\
\x00\x00\x14\x22\x22\x22\x21\x00\
\x00\x00\x01\x14\x44\x41\x10\x00\
\x00\x00\x01\x42\x22\x22\x10\x00\
\x00\x00\x01\x44\x24\x22\x21\x00\
\x00\x00\x01\x42\x42\x42\x21\x00\
\x00\x00\x00\x14\x24\x22\x11\x00\
\x00\x00\x00\x14\x44\x41\x14\x10\
\x00\x00\x01\x44\x11\x14\x44\x10\
\x00\x00\x01\x41\x01\x44\x11\x00\
'
ply04 = upygame.surface.Surface(16, 16, ply04Pixels)

ply05Pixels = b'\
\x12\x22\x21\x11\x11\x11\x00\x00\
\x01\x22\x22\x22\x22\x22\x10\x00\
\x00\x12\x24\x42\x22\x22\x21\x00\
\x00\x14\x42\x22\x44\x44\x22\x10\
\x00\x14\x22\x24\x11\x11\x42\x10\
\x00\x01\x42\x21\x12\x12\x12\x10\
\x00\x01\x42\x24\x11\x11\x42\x10\
\x00\x00\x14\x22\x22\x22\x21\x00\
\x00\x00\x01\x14\x44\x41\x10\x00\
\x00\x00\x01\x42\x22\x22\x10\x00\
\x00\x00\x01\x42\x42\x22\x21\x00\
\x00\x00\x01\x42\x42\x22\x21\x00\
\x00\x00\x00\x14\x42\x22\x10\x00\
\x00\x00\x00\x01\x44\x41\x00\x00\
\x00\x00\x00\x14\x14\x11\x00\x00\
\x00\x00\x00\x14\x14\x44\x10\x00\
'
ply05 = upygame.surface.Surface(16, 16, ply05Pixels)

ply06Pixels = b'\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x02\x00\x00\x00\x00\
\x00\x00\x00\x02\x40\x00\x00\x00\
\x00\x00\x00\x02\x40\x00\x00\x00\
\x00\x00\x20\x02\x40\x00\x00\x00\
\x00\x00\x24\x02\x40\x20\x00\x00\
\x00\x00\x24\x02\x40\x24\x00\x00\
\x00\x00\x24\x02\x40\x24\x00\x00\
\x00\x00\x24\x02\x40\x24\x00\x00\
\x00\x00\x24\x00\x40\x24\x00\x00\
\x00\x00\x24\x00\x00\x24\x00\x00\
\x00\x00\x04\x00\x00\x24\x00\x00\
\x00\x00\x00\x00\x00\x04\x00\x00\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x00\x00\x00\
'
ply06 = upygame.surface.Surface(16, 16, ply06Pixels)

livesPixels = b'\
\x00\x00\x00\x00\
\x0d\xd0\x0d\x60\
\xdd\x2d\xdd\xd6\
\xd2\xdd\xdd\xd6\
\xd2\xdd\xdd\xd6\
\x6d\xdd\xdd\xd6\
\x06\xdd\xdd\x60\
\x00\x6d\xd6\x00\
'
lives = upygame.surface.Surface(8, 8, livesPixels)

arrow_leftPixels = b'\
\x00\x00\x20\x00\x00\x00\
\x00\x02\xd0\x00\x00\x00\
\x00\x2d\xd0\x00\x00\x00\
\x02\xdd\xd2\x22\x22\x22\
\x2d\xdd\xdd\xdd\xdd\xdd\
\xdd\xdd\xdd\xdd\xdd\xdd\
\x0d\xdd\xdd\xdd\xdd\xdd\
\x00\xdd\xd0\x00\x00\x00\
\x00\x0d\xd0\x00\x00\x00\
\x00\x00\xd0\x00\x00\x00\
'
arrow_left = upygame.surface.Surface(12, 10, arrow_leftPixels)

arrow_rightPixels = b'\
\x00\x00\x00\x02\x00\x00\
\x00\x00\x00\x0f\x20\x00\
\x00\x00\x00\x0f\xf2\x00\
\x22\x22\x22\x2f\xff\x20\
\xff\xff\xff\xff\xff\xf2\
\xff\xff\xff\xff\xff\xff\
\xff\xff\xff\xff\xff\xf0\
\x00\x00\x00\x0f\xff\x00\
\x00\x00\x00\x0f\xf0\x00\
\x00\x00\x00\x0f\x00\x00\
'
arrow_right = upygame.surface.Surface(12, 10, arrow_rightPixels)

arrow_upPixels = b'\
\x00\x00\x2d\x00\x00\
\x00\x02\xdd\xd0\x00\
\x00\x2d\xdd\xdd\x00\
\x02\xdd\xdd\xdd\xd0\
\x2d\xdd\xdd\xdd\xdd\
\x00\x02\xdd\xd0\x00\
\x00\x02\xdd\xd0\x00\
\x00\x02\xdd\xd0\x00\
\x00\x02\xdd\xd0\x00\
\x00\x02\xdd\xd0\x00\
\x00\x02\xdd\xd0\x00\
\x00\x02\xdd\xd0\x00\
'
arrow_up = upygame.surface.Surface(10, 12, arrow_upPixels)