# interface.py
# Creates and draws the game instructions

import upygame as pygame
import umachine

class Interface:
    def __init__(self):
        self.infoX = 4		# Start left pos
        self.infoYStart = 2
        self.ySpacing = 10	# Spacing between lines of text
        self.page1 = ["To use a teleporter to", "change levels, stand on", "it and push up or down.", "                   [ press A ]"]
        self.page2 = ["Exiting the screen to", "the left ascends a level", "whereas exiting to the", "right descends a level.", "[ press A ]"]
        self.page3 = ["To complete each stage", "grab all the     imps.", "Some imps spawn", "bonuses like     time,", "     bonus points,", "     freeze enemies,", "or     extra lives.", "         [ press A ]"]

    # Information text
    def showInstructions(self, screen, colour, gameState, page1Images, levelImages, page4Images):
        self.infoY = self.infoYStart

        if gameState == 2:
            for line in self.page1:
                umachine.draw_text(self.infoX, self.infoY, line, colour)
                self.infoY += self.ySpacing
            
            # Tiles
            screen.blit(levelImages[1], 10, 43)
            screen.blit(levelImages[1], 18, 43)
            screen.blit(levelImages[1], 26, 43)
            screen.blit(levelImages[0], 34, 43)
            screen.blit(levelImages[0], 42, 43)
            screen.blit(levelImages[0], 50, 43)
            screen.blit(levelImages[1], 58, 43)
            screen.blit(levelImages[1], 66, 43)
            screen.blit(levelImages[1], 74, 43)
            
            screen.blit(levelImages[0], 10, 62)
            screen.blit(levelImages[0], 18, 62)
            screen.blit(levelImages[0], 26, 62)
            screen.blit(levelImages[1], 34, 62)
            screen.blit(levelImages[1], 42, 62)
            screen.blit(levelImages[1], 50, 62)
            screen.blit(levelImages[0], 58, 62)
            screen.blit(levelImages[0], 66, 62)
            screen.blit(levelImages[0], 74, 62)
            
            screen.blit(levelImages[1], 10, 80)
            screen.blit(levelImages[1], 18, 80)
            screen.blit(levelImages[1], 26, 80)
            screen.blit(levelImages[0], 34, 80)
            screen.blit(levelImages[0], 42, 80)
            screen.blit(levelImages[0], 50, 80)
            screen.blit(levelImages[1], 58, 80)
            screen.blit(levelImages[1], 66, 80)
            screen.blit(levelImages[1], 74, 80)
            
            # Moby
            screen.blit(page1Images[0], 40, 46, 0, True)
            
            # Arrow up/down
            screen.blit(page1Images[3], 42, 30)
            screen.blit(page1Images[3], 42, 67, 0, False, True)
            
        elif gameState == 3:
            for line in self.page2:
                umachine.draw_text(self.infoX, self.infoY, line, colour)
                self.infoY += self.ySpacing
                
            # Draw graphic
            screen.blit(levelImages[0], 20, 52)
            screen.blit(levelImages[0], 28, 52)
            screen.blit(levelImages[0], 36, 52)
            screen.blit(levelImages[1], 44, 52)
            screen.blit(levelImages[1], 52, 52)
            screen.blit(levelImages[1], 60, 52)
            screen.blit(levelImages[0], 68, 52)
            screen.blit(levelImages[0], 76, 52)
            screen.blit(levelImages[0], 84, 52)
            
            screen.blit(levelImages[1], 20, 70)
            screen.blit(levelImages[1], 28, 70)
            screen.blit(levelImages[1], 36, 70)
            screen.blit(levelImages[0], 44, 70)
            screen.blit(levelImages[0], 52, 70)
            screen.blit(levelImages[0], 60, 70)
            screen.blit(levelImages[1], 68, 70)
            screen.blit(levelImages[1], 76, 70)
            screen.blit(levelImages[1], 84, 70)
            
            # Moby
            screen.blit(page1Images[0], 50, 54)
            
            # Arrows left/right
            screen.blit(page1Images[1], 21, 59)
            screen.blit(page1Images[1], 35, 59)
            screen.blit(page1Images[1], 66, 41)
            screen.blit(page1Images[1], 80, 41)
            
            screen.blit(page1Images[2], 66, 59)
            screen.blit(page1Images[2], 80, 59)
            screen.blit(page1Images[2], 21, 77)
            screen.blit(page1Images[2], 35, 77)
    
        elif gameState == 4:
            for line in self.page3:
                umachine.draw_text(self.infoX, self.infoY, line, colour)
                self.infoY += self.ySpacing
                
            # Draw graphic
            screen.blit(page4Images[0], 4, 51)   # freeze
            screen.blit(page4Images[1], 15, 61)  # life
            screen.blit(page4Images[2], 57, 30)  # time
            screen.blit(page4Images[3], 4, 39)   # bonus
            screen.blit(page4Images[4], 54, 10)  # imp