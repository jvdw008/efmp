# drops.py
# Bonus items class

import upygame

class Drops:
    def __init__(self, x, y, type):
        self.x = x
        self.y = y
        self.type = type
    
    def getPosition(self):
        return [self.x, self.y]
        
    def getType(self):
        return self.type