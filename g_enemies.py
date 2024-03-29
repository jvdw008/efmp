# g_enemies.py
# Enemy graphics

import upygame

enemy0_0Pixels = b'\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x11\x11\x11\x11\x11\x00\x00\
\x01\x44\x42\x22\x22\x22\x10\x00\
\x14\x44\x42\x11\x11\x11\x21\x00\
\x14\x25\x21\xcc\x44\xcc\x12\x10\
\x14\x25\x21\xc1\xcc\x1c\x12\x10\
\x14\x55\x21\xcc\x44\xcc\x12\x10\
\x14\x44\x42\x11\x11\x11\x22\x10\
\x14\x44\x42\x22\x22\x22\x21\x00\
\x15\x44\x52\x21\x21\x21\x21\x00\
\x15\x55\x22\x11\x11\x11\x10\x00\
\x15\x55\x22\x12\x12\x12\x10\x00\
\x01\x55\x42\x12\x12\x12\x21\x00\
\x01\x55\x42\x22\x22\x22\x21\x00\
\x00\x15\x54\x44\x44\x44\x10\x00\
'
enemy0_0 = upygame.surface.Surface(16, 16, enemy0_0Pixels)

enemy0_1Pixels = b'\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x11\x11\x11\x11\x11\x00\x00\
\x01\x44\x42\x22\x22\x22\x10\x00\
\x14\x44\x42\x11\x11\x11\x21\x00\
\x14\x25\x21\xcc\x44\xcc\x12\x10\
\x14\x25\x21\xc1\xcc\x1c\x12\x10\
\x14\x55\x21\xcc\x44\xcc\x12\x10\
\x14\x44\x42\x11\x11\x11\x22\x10\
\x14\x44\x42\x22\x22\x22\x21\x00\
\x15\x44\x22\x21\x21\x21\x21\x00\
\x15\x55\x22\x12\x12\x12\x10\x00\
\x01\x55\x42\x12\x12\x12\x21\x00\
\x01\x55\x42\x22\x22\x22\x21\x00\
\x00\x15\x54\x44\x44\x44\x10\x00\
'
enemy0_1 = upygame.surface.Surface(16, 16, enemy0_1Pixels)

enemy0_2Pixels = b'\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x11\x11\x11\x11\x11\x00\x00\
\x01\x44\x42\x22\x22\x22\x10\x00\
\x14\x44\x42\x11\x11\x11\x21\x00\
\x14\x25\x21\xcc\x44\xcc\x12\x10\
\x14\x25\x21\xc1\xcc\x1c\x12\x10\
\x14\x55\x21\xcc\x44\xcc\x12\x10\
\x14\x44\x42\x11\x11\x11\x22\x10\
\x14\x44\x42\x22\x22\x22\x21\x00\
\x15\x44\x22\x21\x21\x21\x21\x00\
\x15\x55\x22\x12\x12\x12\x10\x00\
\x01\x55\x42\x22\x22\x22\x21\x00\
\x00\x15\x54\x44\x44\x44\x10\x00\
'
enemy0_2 = upygame.surface.Surface(16, 16, enemy0_2Pixels)

enemy1_0Pixels = b'\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x11\x11\x00\x00\x00\
\x00\x00\x11\xff\xff\x10\x00\x00\
\x00\x01\xff\xf5\x55\xf1\x00\x00\
\x00\x1f\xff\x52\x52\x5f\x10\x00\
\x00\x1f\x55\x26\x26\x2f\x10\x00\
\x01\xf5\xf5\x26\x26\x2f\x10\x00\
\x01\xff\x5f\x52\x52\x5f\x10\x00\
\x01\xf5\x55\x55\x55\x9f\x10\x00\
\x01\xf5\x55\x55\x99\x99\xf1\x00\
\x01\xf5\x55\x95\x58\x99\xf1\x00\
\x0f\x55\x59\x59\x85\x89\xf1\x00\
\x1f\x55\x95\x99\x98\x99\xf1\x00\
\x1f\x5f\x59\x99\x99\x9f\xf1\x00\
\x1f\xf9\xf9\xf9\x99\xff\x10\x00\
\x01\xff\xff\xff\xff\xf1\x00\x00\
'
enemy1_0 = upygame.surface.Surface(16, 16, enemy1_0Pixels)

enemy1_1Pixels = b'\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x11\x11\x00\x00\
\x00\x00\x00\x11\xff\xff\x10\x00\
\x00\x00\x01\xff\xf5\x55\xf1\x00\
\x00\x00\x1f\xff\x52\x52\x5f\x10\
\x00\x00\x1f\x55\x26\x26\x2f\x10\
\x00\x01\xf5\xf5\x26\x26\x2f\x10\
\x00\x01\xff\x5f\x52\x52\x5f\x10\
\x00\x1f\x55\x55\x55\x59\x9f\x10\
\x00\x1f\x59\x59\x55\x99\x9f\x10\
\x01\xf5\x55\x95\x99\x89\xff\x10\
\x1f\x55\x95\x99\x99\x99\xf1\x00\
\x1f\x5f\x59\x99\x99\x9f\xf1\x00\
\x1f\xf5\xf9\xf9\x99\xff\x10\x00\
\x01\xff\xff\xff\xff\xf1\x00\x00\
'
enemy1_1 = upygame.surface.Surface(16, 16, enemy1_1Pixels)

enemy1_2Pixels = b'\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x01\x11\x10\x00\
\x00\x00\x00\x01\x1f\xff\xf1\x00\
\x00\x00\x00\x1f\xff\x55\x5f\x10\
\x00\x00\x01\xff\xf5\x25\x25\xf1\
\x00\x00\x01\xf5\x52\x62\x62\xf1\
\x00\x00\x1f\x5f\x52\x62\x62\xf1\
\x00\x00\x1f\xf5\xf5\x25\x25\xf1\
\x00\x11\xf5\x55\x55\x55\x55\xf1\
\x01\xff\x55\x55\x59\x59\x99\xf1\
\x1f\x55\x55\x95\x99\x89\x9f\x10\
\x1f\x5f\x59\x99\x99\x99\xf1\x00\
\x1f\xf5\xf9\xf9\x99\xff\x10\x00\
\x01\xff\xff\xff\xff\xf1\x00\x00\
'
enemy1_2 = upygame.surface.Surface(16, 16, enemy1_2Pixels)

enemy2_0Pixels = b'\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x11\x00\x00\x00\x00\x00\
\x00\x01\x7c\x10\x00\x00\x00\x00\
\x00\x17\x71\xc1\x00\x00\x00\x00\
\x00\x17\x7c\x10\x10\x00\x00\x00\
\x00\x17\xc1\x11\x51\x10\x00\x00\
\x00\x1c\x77\x42\x52\x21\x00\x00\
\x00\x1c\x71\x11\x51\x10\x00\x00\
\x00\x1c\xcc\x11\x51\x00\x00\x00\
\x01\xcc\x1c\x14\x44\x10\x00\x00\
\x00\x13\x33\x33\x33\x10\x00\x00\
\x01\x37\x73\x33\x77\x31\x00\x00\
\x13\x72\x23\x37\x22\x73\x10\x00\
\x17\x21\x42\x32\x14\x27\x10\x00\
\x15\x24\xc2\x52\x4c\x25\x10\x00\
\x01\x12\x21\x11\x22\x11\x00\x00\
'
enemy2_0 = upygame.surface.Surface(16, 16, enemy2_0Pixels)

enemy2_1Pixels = b'\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x11\x00\x00\x00\x00\x00\
\x00\x01\x7c\x10\x00\x00\x00\x00\
\x00\x17\x71\xc1\x00\x00\x00\x00\
\x00\x17\x7c\x10\x10\x00\x00\x00\
\x00\x17\xc1\x11\x51\x10\x00\x00\
\x00\x1c\x77\x42\x52\x21\x00\x00\
\x00\x1c\x71\x11\x51\x10\x00\x00\
\x00\x1c\xcc\x11\x51\x00\x00\x00\
\x01\xcc\x1c\x14\x44\x10\x00\x00\
\x01\x37\x73\x33\x77\x31\x00\x00\
\x13\x72\x27\x37\x22\x73\x10\x00\
\x17\x24\x12\x32\x41\x27\x10\x00\
\x15\x2c\x42\x52\xc4\x25\x10\x00\
\x01\x12\x21\x11\x22\x11\x00\x00\
'
enemy2_1 = upygame.surface.Surface(16, 16, enemy2_1Pixels)

enemy2_2Pixels = b'\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x11\x00\x00\x00\x00\x00\
\x00\x01\x7c\x10\x00\x00\x00\x00\
\x00\x17\x71\xc1\x00\x00\x00\x00\
\x00\x17\x7c\x10\x10\x00\x00\x00\
\x00\x17\xc1\x11\x51\x11\x00\x00\
\x00\x1c\x77\x42\x52\x22\x10\x00\
\x00\x1c\x71\x11\x51\x11\x00\x00\
\x00\x1c\xcc\x11\x51\x00\x00\x00\
\x01\xcc\x1c\x14\x44\x10\x00\x00\
\x01\x37\x73\x33\x77\x31\x00\x00\
\x13\x72\x23\x37\x22\x73\x10\x00\
\x17\x2c\x42\x32\xc4\x27\x10\x00\
\x15\x24\x12\x52\x41\x25\x10\x00\
\x01\x12\x21\x11\x22\x11\x00\x00\
'
enemy2_2 = upygame.surface.Surface(16, 16, enemy2_2Pixels)

bulletPixels = b'\
\x00\x20\x00\
\x2d\x22\xc0\
\x00\x20\x00\
'
bullet = upygame.surface.Surface(6, 3, bulletPixels)
