# imps.py
# All the data for collectible impd

import upygame
import umachine
import urandom as random

class Imps:
    def __init__(self, x, y, image, type):
        self.name = ["Floopy", "Trunzil", "Greepol", "Whirly", "Scooch", "Crakmo", "Lettuce", "Struf"]
        self.habitat = ["grass huts", "rusty cages", "pine tree cones", "beach ball", "onesey", "cdrom", "cathode tube", "glass bead"]
        self.eats = ["grilled fedora", "snail tunnels", "barking tyres", "dust cakes", "paperclips", "pokittos", "usb cables", "fish eyes"]
        self.temper = ["angry", "implicit", "wild", "excited", "timid", "flaring", "calm", "thoughtful"]
        self.status = ["flacid", "sleepy", "jumpy", "secure", "popular", "vulnerable", "inept", "lonely"]
        self.x = x
        self.y = y
        self.image = image
        self.type = type
        self.state = True   # True for visible, False for hidden
        
        # Set the random stats on instantiation
        self.rndName = random.getrandbits(3)
        self.rndHabitat = random.getrandbits(3)
        self.rndEats = random.getrandbits(3)
        self.rndTemper = random.getrandbits(3)
        self.rndStatus = random.getrandbits(3)
        
    # Return position
    def getPosition(self):
        return [self.x, self.y]
    
    # Return type for animation class
    def getType(self):
        return self.type
    
    # Get text
    def getName(self):
        return self.name[self.rndName]
    
    def getHabitat(self):
        return self.habitat[self.rndHabitat]
    
    def getEats(self):
        return self.eats[self.rndEats]
        
    def getTemper(self):
        return self.temper[self.rndTemper]
        
    def getStatus(self):
        return self.status[self.rndStatus]
        
    # Set the updated image
    def setImage(self, image, type):
        self.image = image
        self.type = type
        
    # 'Delete' imp
    def deleteImp(self):
        self.state = False
        
    # Reset imp
    def resetImp(self):
        self.state = True
        self.rndName = random.getrandbits(3)
        self.rndHabitat = random.getrandbits(3)
        self.rndEats = random.getrandbits(3)
        self.rndTemper = random.getrandbits(3)
        self.rndStatus = random.getrandbits(3)
        
    # Get state of imp
    def getState(self):
        return self.state
        
    # Check for player collision
    def update(self, playerX, playerY):
        if playerX > self.x and playerX < self.x + 8:
            if playerY < self.y and playerY + 16 >= self.y:
                return True
                
        return False

    # Draw imp screen
    def drawStats(self, screen, level):
        screen.blit(self.image, 50, 20) # Image
        umachine.draw_text(40, 0, "LEVEL: " + str(level), 12)
        umachine.draw_text(40, 30, self.getName(), 2)
        umachine.draw_text(0, 50, "HABITAT: " + self.getHabitat(), 15)
        umachine.draw_text(4, 58, "TEMPER: " + self.getTemper(), 13)
        umachine.draw_text(14, 66, "EATS: " + self.getEats(), 14)
        umachine.draw_text(4, 74, "STATUS: " + self.getStatus(), 10)
        