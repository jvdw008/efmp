# levels.py
# Used to auto generate levels for the game

import upygame
import urandom as random

class Levels:
    def __init__(self, level):
        self.currentLevel = 0
        self.platforms = 5
        self.startX = 0
        self.startY = 18
        self.spacing = 8
        self.x = 0
        self.y = 0
        self.level = level
        
    # Draw the platforms
    def drawLevel(self, screen, levelImages):
        self.y = 0
        self.x = 00
        
        for row in range(self.platforms):
            for col in range(14):
                if self.level[row][col] == 1:
                    screen.blit(levelImages[0], self.startX + self.x, self.startY + self.y)
                else:
                    screen.blit(levelImages[1], self.startX + self.x, self.startY + self.y)
                self.x += self.spacing
            self.y += 16
            self.x = 0

    # Return platform Id
    def getPlatformType(self, playerX, playerY):
        # First, determine which platform level moby is standing on
        if playerY == 2:
            currentPlatformLevel = 0
            
        elif playerY == 18:
            currentPlatformLevel = 1
            
        elif playerY == 34:
            currentPlatformLevel = 2
            
        elif playerY == 50:
            currentPlatformLevel = 3
            
        elif playerY == 66:
            currentPlatformLevel = 4
            
        # Now let's calc the X position to match
        currentCol = int(playerX // 8)
        if currentCol < 0:
            currentCol == 0
            
        if currentCol > 14:
            currentCol = 14
            
        result = 0
        for pos in range(currentCol):
            result = self.level[currentPlatformLevel][pos]
            
        return result