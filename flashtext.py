# flashtext.py
# Displays in-game text with option to move it up slowly before disappearing

import upygame as pygame
import umachine

class Text:
    def __init__(self, duration, speed, text, move, y):
        self.startY = y
        self.x = (120 - (len(text) * 5)) // 2   # Try center the text dynamically
        self.y = self.startY
        self.text = ""
        self.duration = duration  # Display duration
        self.moveTimer = speed  # (1 is recommended )Move text up timer
        self.speed = speed + 1
        self.text = text
        self.move = move

    # Display text
    def draw (self):
        if (self.duration > 0):
            umachine.draw_text(self.x, self.y, self.text, 2)

    # Update display duration
    def update(self):
        self.duration -= 1
        if (self.move):
        	if (self.moveTimer > 0):
        	    self.moveTimer -= 1
        	else:
				self.moveTimer = self.speed
				self.y -= 1
