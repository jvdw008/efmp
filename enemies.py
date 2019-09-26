# enemies.py
# Class to manage enemies

import upygame

class Enemy:
    def __init__(self, enemyType, x, y, dir, speed):
        self.enemyType = enemyType
        self.x = x
        self.y = y
        self.min = 0
        self.max = 100
        self.direction = dir
        self.speed = speed
        self.speedUp = self.speed * 2
        
    # Update movement
    def update(self, playerX, playerY):
        # Enemy type 2 turns towards player (and hopefully shoots one day)
        if self.enemyType == 2 and self.y == playerY:
            if playerX < self.x:
                self.direction = -1
            if playerX > self.x:
                self.direction = 1
                
        if self.direction == 1:
            # Enemy type 1 speeds up when on the same platform as player
            if self.enemyType == 1 and self.y == playerY:
                self.x += self.speedUp
            else:
                self.x += self.speed
                
            if self.x >= self.max:
                self.direction = -self.direction
        else:
            if self.enemyType == 1 and self.y == playerY:
                self.x -= self.speedUp
            else:
                self.x -= self.speed
                
            if self.x <= self.min:
                self.direction = -self.direction
        
    # Return moving direction
    def getDirection(self):
        return self.direction
        
    # Return type, ie 0 - 3
    def getType(self):
        return self.enemyType
        
    # Get position
    def getEnemyPos(self):
        return [self.x, self.y]
        