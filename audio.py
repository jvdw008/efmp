# audio.py
# This class plays audio

import upygame as pygame
import sounds               # The sound data

class Audio:
    def __init__(self, g_sound):
        self.sound = g_sound

		# Play sfx
    def playSfx(self, snd):
        self.sound.play_sfx(snd, len(snd), False)
