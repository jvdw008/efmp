# player.py
# Handle player control and management

import upygame as pygame
import graphics
import urandom as random

class Player:
    def __init__(self, startX, startY, minX, maxX):
        self.playerX = startX		# Start X
        self.playerY = startY		# Start Y
        self.startY = startY
        self.originalX = startX
        self.originalY = startY
        self.min = minX				# Left clamp
        self.max = maxX				# Right clamp
        self.minY = 16
        self.maxY = 66
        self.direction = 1	# 1 for right, 0 for left
        self.levelHeight = 16

    # Draw player
    def draw(self, screen, image):
        if self.direction:
            screen.blit(image, self.playerX, self.playerY)
        else:
            screen.blit(image, self.playerX, self.playerY, 0, True)

    # Get current direction
    def getDirection(self):
        return self.direction

    # Move player
    def update(self, x):
        if (x < 0):
            self.direction = 0
        elif (x > 0):
            self.direction = 1

        self.playerX += x

        if (self.playerX > self.max):
            self.playerX = self.min
            self.playerY += self.levelHeight
            # Check for bottom
            if self.playerY > self.levelHeight * 5:
                self.playerY = self.startY

        if (self.playerX < self.min):
            self.playerX = self.max
            self.playerY -= self.levelHeight
            # Check for top
            if self.playerY < self.startY:
                self.playerY = self.startY + (self.levelHeight * 4)

    # Check up
    def checkUp(self):
        if self.playerY >= self.minY:
            self.playerY -= self.levelHeight
        
    # Check down
    def checkDown(self):
        if self.playerY < self.maxY:
            self.playerY += self.levelHeight
    
    # Return player x/y pos
    def getPlayerPos(self):
        return (self.playerX, self.playerY)

    # Move player out of screen on level complete
    def warpPlayer(self):
        if self.playerY >= - 16:
            self.playerY -= 8
            
    # Reset player after above anim
    def resetPlayer(self):
        self.playerX = self.originalX
        self.playerY = self.originalY
        
    # Set splash imp start
    def setImpSplash(self, x, y):
        self.splash = [[x,y],[x,y],[x,y],[x,y],[x,y]]
        self.splashY = -8
        
    # Update splash
    def updateImpSplash(self):
        self.iter = 0
        self.removeId = 0
        self.splashY += 1
        for i in self.splash:
            if self.iter == 0:
                i[0] -= 3
            elif self.iter == 1:
                i[0] -= 2
            elif self.iter == 3:
                i[0] += 2
            elif self.iter == 4:
                i[0] += 3
            
            i[1] += self.splashY + random.getrandbits(2) # Still 50/50 for the random bit
            
            if i[1] > 88:
                self.removeId = self.iter
            
            self.iter += 1
    
        if self.removeId != 0:
            del self.splash[self.removeId - 1]
    
    # Imp splash when player gets hit    
    def drawImpSplash(self, screen, imp):
        for i in self.splash:
            screen.blit(imp, i[0], i[1])
        