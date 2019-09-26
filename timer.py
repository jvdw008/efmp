# timer.py
# This is to count the time down in-game

import upygame
import umachine

class Timer:
    def __init__(self, val):
        self.timerStartVal = val
        self.timer = self.timerStartVal         # how many seconds
        self.time = 0
        
    # Update the counter
    def update(self):
        self.count = umachine.time_ms() % 500
        
        if self.timer >= 0:
            if self.count == 0 or self.count == 10:
                self.timer -= 1
        
    # Return current time left
    def getTime(self):
        return self.timer
        
    # Display graphical timer
    def drawTime(self, screen, numbers, x, y, fontSpace):
        self.time = self.getTime()
        
        if self.time >= 50:
            screen.blit(numbers[5], x, y)
            screen.blit(numbers[self.time - 50], x + fontSpace, y)
        
        if self.time >= 40 and self.time < 50:
            screen.blit(numbers[4], x, y)
            screen.blit(numbers[self.time - 40], x + fontSpace, y)
            
        if self.time >= 30 and self.time < 40:
            screen.blit(numbers[3], x, y)
            screen.blit(numbers[self.time - 30], x + fontSpace, y)
            
        if self.time >= 20 and self.time < 30:
            screen.blit(numbers[2], x, y)
            screen.blit(numbers[self.time - 20], x + fontSpace, y)
            
        if self.time >= 10 and self.time < 20:
            screen.blit(numbers[1], x, y)
            screen.blit(numbers[self.time - 10], x + fontSpace, y)
            
        if self.time < 10:
            screen.blit(numbers[0], x, y)
            screen.blit(numbers[self.time - 10], x + fontSpace, y)
            
    # Set timer if player collected a time item
    def setTimer(self, val):
        self.timer += val
        if self.timer > 59:
            self.timer = 59
            
    # Count timer down when level complete, to add to score
    def depleteTimer(self):
        self.timer -= 1