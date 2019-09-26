# Copyright 2019 by Blackjet
# Graphics done using Aseprite
# Sfx done using BFXR and Audacity
# Code, music, sfx, graphics by Jaco van der Walt

# The source code in this file is released under the GNU GPL V3 license.
# Go to https://choosealicense.com/licenses/gpl-3.0/ for the full license details.

import upygame as pygame
import urandom as random
import umachine                             # For on-screen text
import graphics                             # Graphics
import sounds
from audio import Audio                     # Audio class to play sounds
from interface import Interface             # Game interface
from background import Background           # Background (aquarium)
from player import Player                   # Player class
from animation import Animation as Anim     # Animation cass for fish, coins, player etc
from timer import Timer                     # Countdown timer class
from flashtext import Text                  # On-screen text for important messages in-game
from imps import Imps                       # Imps
from levels import Levels                   # Level logic
from enemies import Enemy                   # Enemies
from drops import Drops                     # Bonus items

# Game specific imports below
# Check RAM usage
import gc
gc.collect()

# Setup the screen buffer
pygame.display.init(False)

# Set colours in RGB formatted tuples
pygame.display.set_palette_16bit([0x0000, 0x3189, 0xffff, 0x9556, 0x83f0, 0x52a9, 0xa186, 0xd2ac, 0x9709, 0x348d, 0x5e5b, 0x39ee, 0xf766, 0xf000, 0x3b78, 0x65c5])

# default mode of 110x88 @16 cols
screen = pygame.display.set_mode()

# Init audio
g_sound = pygame.mixer.Sound()

# Test for real h/w to prevent simulator from hanging
gpioPin = umachine.Pin (umachine.Pin.EXT2, umachine.Pin.ANALOG_IN)
gpioPinValue = gpioPin.value()
if(gpioPinValue == 0):
    isThisRealHardware = False
    menuSong = ""
    gameSong = ""
    pauseSong = ""
else:
    isThisRealHardware = True
    menuSong = "folder/menuSong.wav"
    gameSong = "folder/gameSong.wav"

# Version number of current game build
version = 14

# Constants
STATE_MENU = 0
STATE_INSTRUCTIONS = 1
STATE_INSTRUCTIONS2 = 2
STATE_INSTRUCTIONS3 = 3
STATE_INSTRUCTIONS4 = 4
STATE_GAME = 5
STATE_IMPSCREEN = 6
STATE_GAMEOVER = 7

# Variables
cheatsOn = False                # Testing
gameState = 0                   # 0 = menu, 1 = instruction 1, 2 = instruction 2, 3 = instruction 3, 4 = game, 5 = imp screen, 6 = game over
gameOver = False
startGame = False               # Boolean for starting the game
level = 0                       # The level of the game
score = 0                       # Player score
levelComplete = False           # When player has collected all on-screen imps
playerAnimDone = False          # Do anhimation of player flying up when level completed
playerLives = 9                 # Lives
playerPos = []                  # Player position
flashPlayer = False             # Temp invulnerability after player dies
flashTimeMax = 60               # How long player flashes for
flashTime = flashTimeMax        # Default value
movePlayerX = 0                 # player momentum
moveSpeed = 4                   # Player movement speed
warpPlayed = False              # War sound played?
upPressed = False               # Modifiers for dpad
downPressed = False             # As above
rightPressed = False
leftPressed = False
aPressed = False                # As above
bPressed = False                # As above
cPressed = False                # As above
musicPlaying = False            # Toggle for music
flashTextTimer = 20             # On-screen text timer
isTimerUp = False               # Used for time specific events
gameOverPlayed = False          # Trigger to pay gameover sound when dead
impId = 0                       # For randomizing imps
levelImps = []                  # List for imps per level
lvlEnemies = []                 # List of enemies per level
freezeEnemies = False           # Used for when player collects the stop item
freezeTimerMax = 60
freezeTimer = freezeTimerMax
checkHit = False                # Hit detection between player and imp
tmpImpId = 0                    # Used to get the imp ID to remove from screen
impsOnScreen = 13               # Initla qty of level mips on screen
rndLevel = 0                    # Used to choose a random platform/teleporter combo
bulletVisible = False           # To limit ram usage, just have one bullet on-screen and no instantiation
bulletX = -10
bulletY = -10
bulletSpeed = 2
bulletDir = 1
bonusItem = []
bonusItemDropRate = 100         # Higher value is less drops, default 120

# Audio effects
snd_select = sounds.select_8b
snd_bonus = sounds.bonus_8b
snd_extralife = sounds.extralife_8b
snd_extratime = sounds.extratime_8b
snd_freeze = sounds.freeze_8b
snd_hurt = sounds.injury_8b
snd_shoot = sounds.shoot_8b
snd_complete = sounds.complete_8b

# Animation setup - Array of graphic images and the speed of the animation (lower = faster)
playerAnimWalk = Anim([graphics.g_player.ply01, graphics.g_player.ply02, graphics.g_player.ply03, graphics.g_player.ply04, graphics.g_player.ply05], 4 // moveSpeed)
playerIdle = graphics.g_player.ply03
playerWarp = graphics.g_player.ply06
enemy1 = Anim([graphics.g_enemies.enemy0_0, graphics.g_enemies.enemy0_1, graphics.g_enemies.enemy0_2], 4)
enemy2 = Anim([graphics.g_enemies.enemy1_0, graphics.g_enemies.enemy1_1, graphics.g_enemies.enemy1_2], 2)
enemy3 = Anim([graphics.g_enemies.enemy2_0, graphics.g_enemies.enemy2_1, graphics.g_enemies.enemy2_2], 4)
item_stop = Anim([graphics.g_collectibles.stop_0, graphics.g_collectibles.stop_1], 20)
item_heart = Anim([graphics.g_collectibles.heart_0, graphics.g_collectibles.heart_1], 5)
item_clock = Anim([graphics.g_collectibles.clock_0, graphics.g_collectibles.clock_1], 7)
item_bonus = Anim([graphics.g_collectibles.bonus_0, graphics.g_collectibles.bonus_1, graphics.g_collectibles.bonus_2], 1)
instructionsGraphic1 = [graphics.g_player.ply01, graphics.g_player.arrow_left, graphics.g_player.arrow_right, graphics.g_player.arrow_up]
instructionsGraphic4 = [graphics.g_collectibles.stop_0, graphics.g_collectibles.heart_0, graphics.g_collectibles.clock_0, graphics.g_collectibles.bonus_0, graphics.g_imps.imp0_0]
imp1Anim = Anim([graphics.g_imps.imp0_0, graphics.g_imps.imp0_1], 10)
imp2Anim = Anim([graphics.g_imps.imp1_0, graphics.g_imps.imp1_1], 11)
imp3Anim = Anim([graphics.g_imps.imp2_0, graphics.g_imps.imp2_1], 12)
imp4Anim = Anim([graphics.g_imps.imp3_0, graphics.g_imps.imp3_1], 13)
imp5Anim = Anim([graphics.g_imps.imp4_0, graphics.g_imps.imp4_1], 14)
imp6Anim = Anim([graphics.g_imps.imp5_0, graphics.g_imps.imp5_1], 15)

# 15 map platform designs to be chosen at random by code, when building levels
levelMaps = [
            [1,1,0,0,1,1,0,0,1,1,0,0,1,1],
            [0,0,1,1,0,0,1,1,0,0,1,1,0,0],
            [0,1,1,1,0,0,0,1,1,0,0,0,1,1],
            [1,0,0,0,1,1,1,0,0,1,1,1,0,0],
            [1,1,1,0,0,0,1,1,1,0,0,0,1,1],
            [0,0,0,1,1,1,0,0,0,1,1,1,0,0],
            [1,1,1,1,1,1,0,0,1,1,1,1,0,0],
            [0,0,1,1,1,1,1,1,1,1,0,0,1,1],
            [0,0,0,1,0,0,1,1,0,0,1,1,1,1],
            [1,1,1,0,1,1,0,0,1,1,0,0,0,1],
            [1,1,1,0,0,1,0,0,1,1,1,0,0,1],
            [1,0,0,1,1,1,1,1,1,1,1,0,0,1],
            [0,0,0,0,0,1,1,1,1,1,0,0,0,0],
            [1,1,1,1,1,1,1,0,0,0,1,1,1,1],
            [1,1,0,0,0,0,1,1,0,0,0,0,1,1],
            [0,0,1,0,0,1,0,0,1,0,0,1,0,0]
        ]
       
# General graphics
livesImg = graphics.g_player.lives
numbers = [graphics.g_numbers.n0, graphics.g_numbers.n1, graphics.g_numbers.n2, graphics.g_numbers.n3, graphics.g_numbers.n4, graphics.g_numbers.n5, graphics.g_numbers.n6, graphics.g_numbers.n7, graphics.g_numbers.n8, graphics.g_numbers.n9]
impImages = [graphics.g_imps.imp0_0, graphics.g_imps.imp1_0, graphics.g_imps.imp2_0, graphics.g_imps.imp3_0, graphics.g_imps.imp4_0, graphics.g_imps.imp5_0]
levelImages = [[graphics.g_tiles.tile01, graphics.g_teleporters.tele01], [graphics.g_tiles.tile02, graphics.g_teleporters.tele02], [graphics.g_tiles.tile03, graphics.g_teleporters.tele03], [graphics.g_tiles.tile04, graphics.g_teleporters.tele04], [graphics.g_tiles.tile05, graphics.g_teleporters.tele05], [graphics.g_tiles.tile06, graphics.g_teleporters.tele06]]
bullet = graphics.g_enemies.bullet

# Init classes
instructions = Interface()
bg = Background(0, 0)
player = Player(0, 2, -12, 106)
audio = Audio(g_sound)
lvlEnemies = Enemy(0, -20, -20, 0, 0)
bonusItem.append(Drops(-20, -20, 0))
aLevel = Levels([levelMaps[random.getrandbits(4)], levelMaps[random.getrandbits(4)], levelMaps[random.getrandbits(4)], levelMaps[random.getrandbits(4)], levelMaps[random.getrandbits(4)]])
levelImps = Imps(-20, -20, impImages[0], 0)
flashText = Text(1, 1, "", True, -5)

tmpImpId = random.getrandbits(2)
impId = tmpImpId + random.getrandbits(2)
if impId > 5:
    impId = 5
#############################################
def update():
    global gameState, levelComplete, movePlayerX, impsOnScreen, impId, rndLevel, bonusItem, playerLives, bonusItemDropRate, score, aLevel, tmpImpId
    global cheatsOn, flashPlayer, flashText, freezeTimer, freezeTimerMax, freezeEnemies, bulletVisible, bulletX, bulletY, bulletDir, bulletSpeed, warpPlayed
    
    # Randomize imps during splash
    if gameState == STATE_MENU:
        # Create the random imps
        tmpImpId = random.getrandbits(2)
        impId = tmpImpId + random.getrandbits(2)
        if impId > 5:
            impId = 5
            
        # Create random level graphics
        rndLevel = random.getrandbits(3)
        if rndLevel > 5:
            rndLevel = 5
    
    elif gameState == STATE_GAME:
        # Player position
        playerPos = player.getPlayerPos()
        # Update imp collection
        if not levelComplete:
            tmpImpType = 0
            
            # Update anims then break out
            for localImp in levelImps:
                if localImp.getState():
                    tmpImpType = localImp.getType()
                    if tmpImpType == 0:
                        imp1Anim.update()
                        break
                    elif tmpImpType == 1:
                        imp2Anim.update()
                        break
                    elif tmpImpType == 2:
                        imp3Anim.update()
                        break
                    elif tmpImpType == 3:
                        imp4Anim.update()
                        break
                    elif tmpImpType == 4:
                        imp5Anim.update()
                        break
                    else:
                        imp6Anim.update()
                        break
                    
            # Has player hit imp?
            for localImp in levelImps:
                if localImp.getState():
                    if localImp.update(playerPos[0] + 8, playerPos[1]):
                        score += 1
                        localImp.deleteImp()
                        impsOnScreen -= 1
                        willWeDropItem = random.getrandbits(7)
                        
                        if willWeDropItem > bonusItemDropRate:
                            if len(bonusItem) > 0:
                                del bonusItem[0]
                                gc.collect()
                            bonusDropType1 = random.getrandbits(2)
                            bonusItem.append(Drops(50, 55, bonusDropType1))
            
            # Update bonus items if on screen - use temp vars to ensure animatiosn don't get updated more than once per update
            tStop = False
            tHeart = False
            tClock = False
            tBonus = False
            for item in bonusItem:
                if item.getType() == 0:
                    if not tStop:
                        item_stop.update()
                        tStop = True
                elif item.getType() == 1:
                    if not tHeart:
                        item_heart.update()
                        tHeart = True
                    
                elif item.getType() == 2:
                    if not tClock:
                        item_clock.update()
                        tClock = True
                    
                else:
                    if not tBonus:
                        item_bonus.update()
                        tBonus = True
                
                ##################################
                # Check player hit an item?
                if playerPos[1] == 50:
                    tItemPos = item.getPosition()
                    tText = ""
                    if playerPos[0] + 8 > tItemPos[0] and playerPos[0] < tItemPos[0] + 8:
                        # Now do what depends on the item
                        if len(bonusItem) > 0:
                            del bonusItem[0]
                            gc.collect()
                            
                        if tClock:
                            timer.setTimer(30)
                            tText = "Time bonus"
                            audio.playSfx(snd_extratime)
                            
                        if tHeart:
                            if playerLives < 9:
                                playerLives += 1
                            tText = "Extra life"
                            audio.playSfx(snd_extralife)
                            
                        if tBonus:
                            score += 50
                            tText = "Bonus"
                            audio.playSfx(snd_bonus)
                            
                        if tStop:
                            tText = "Freeze"
                            freezeEnemies = True
                            audio.playSfx(snd_freeze)
                            
                        flashText = Text(flashTextTimer, 0, tText, True, tItemPos[1])
            # Update timer
            timer.update()
            
            # Update flash text
            flashText.update()
            
            # Update enemies and positions and animations
            tEnemy1 = False
            tEnemy2 = False
            tEnemy3 = False
            
            # Keep animating enemies
            for localEnemies in lvlEnemies:
                if localEnemies.getType() == 0:
                    if not tEnemy1:
                        enemy1.update()
                        tEnemy1 = True
                    
                elif localEnemies.getType() == 1:
                    if not tEnemy2:
                        enemy2.update()
                        tEnemy2 = True
                    
                else:
                    if not tEnemy3:
                        enemy3.update()
                        tEnemy3 = True
                        # Shoot at player if not frozen
                        if not freezeEnemies:
                            localEnemyPos = localEnemies.getEnemyPos()
                            if not bulletVisible:
                                if localEnemyPos[1] == playerPos[1]:
                                    audio.playSfx(snd_shoot)
                                    bulletVisible = True
                                    bulletX = localEnemyPos[0]
                                    bulletY = localEnemyPos[1] + 4
                                    if localEnemies.getDirection() > 0:
                                        bulletDir = 1
                                    else:
                                        bulletDir = -1
                            
            # Update enemy bullet if on-screen
            if bulletVisible:
                if bulletX > -10 and bulletX < 120:
                    if bulletDir == 1:
                        bulletX += bulletSpeed
                    else:
                        bulletX += -bulletSpeed
                        
                else:
                    #  Bullet has hit edge of screen, disable it
                    bulletX = -10
                    bulletY = -10
                    bulletVisible = False
                    bulletDir = 0
            
            # Update twice to double up speed
            if timer.getTime() <= 20:
                if not freezeEnemies:
                    for localEnemies in lvlEnemies:
                        localEnemies.update(playerPos[0], playerPos[1])
                
            # Only move enemies if not frozen
            if freezeEnemies:
                if freezeTimer > 0:
                    freezeTimer -= 1
                else:
                    freezeTimer = freezeTimerMax
                    freezeEnemies = False
            else:
                for localEnemies in lvlEnemies:
                    localEnemies.update(playerPos[0], playerPos[1])
                    
            ##################################
            # Has enemy hit player?
            for localEnemies in lvlEnemies:
                if not cheatsOn:
                    if not flashPlayer:
                        tmpPlayerHit = False
                        # Check player hit by bullet
                        if bulletX > playerPos[0] + 4 and bulletX < playerPos[0] + 12:
                            if bulletY > playerPos[1] and bulletY < playerPos[1] + 16:
                                tmpPlayerHit = True
                                
                        # Check player hit by enemy
                        localEnemyPos = localEnemies.getEnemyPos()
                        if playerPos[1] == localEnemyPos[1]:
                            if (playerPos[0] + 8 >= localEnemyPos[0] and playerPos[0] + 8 <= localEnemyPos[0] + 16) or (playerPos[0] + 8 <= localEnemyPos[0] + 16 and playerPos[0] + 8 >= localEnemyPos[0]):
                                tmpPlayerHit = True
                                        
                        if tmpPlayerHit:
                            audio.playSfx(snd_hurt)
                            if playerLives > 0:
                                    playerLives -= 1
                                    player.resetPlayer()
                                    flashPlayer = True
                                    
                                    # Set imp splash
                                    player.setImpSplash(playerPos[0] +8, playerPos[1] + 8)
                                    # Lose 5 imps
                                    score -= 5
                                    if score < 0:
                                        score = 0
                                        
                                    # Is player dead
                                    if playerLives <= 0:
                                        gameState = STATE_GAMEOVER
            
            # Update imp splash
            if flashPlayer:
                player.updateImpSplash()
            
            # Update player
            if movePlayerX != 0:
                # Update only when walking
                playerAnimWalk.update()
            
                # Update player position
                player.update(movePlayerX)
                
        else:
            if not warpPlayed:
                audio.playSfx(snd_complete)
                warpPlayed = True
                
            # Level complete, so move player up out of screen
            movePlayerX = 0
            player.warpPlayer()
            # Do timer to score count
            if playerPos[1] < 0:
                if timer.getTime() > 0:
                    score += 1
                    timer.depleteTimer()

        # Is level complete?
        if impsOnScreen <= 0:
            levelComplete = True
    
#############################################
def render():
    global levelComplete, rndLevel, levelImages, flashPlayer, flashTime, flashTimeMax
    
    # Render instruction pages
    if gameState >= STATE_INSTRUCTIONS and gameState < STATE_GAME:
        instructions.showInstructions(screen, 2, gameState, instructionsGraphic1, levelImages[0], instructionsGraphic4)
        
    # Render splash
    if gameState == STATE_MENU:
        screen.blit(graphics.g_splash.splash, 0, 0)
        umachine.draw_text(86, 81, "v0." + str(version), 2)
    
    # Render game
    elif gameState == STATE_GAME:
        # Render platforms
        aLevel.drawLevel(screen, levelImages[rndLevel])
        
        # Render imps
        for localImp in levelImps:
            # Update anims
            if localImp.getState():
                tmpImpType = localImp.getType()
                tmpImpPos = localImp.getPosition()
                tmpImpVisible = localImp.getState()
                if tmpImpVisible:
                    if tmpImpType == 0:
                        imp1Anim.draw(screen, tmpImpPos[0], tmpImpPos[1], 1)
                    elif tmpImpType == 1:
                        imp2Anim.draw(screen, tmpImpPos[0], tmpImpPos[1], 1)
                    elif tmpImpType == 2:
                        imp3Anim.draw(screen, tmpImpPos[0], tmpImpPos[1], 1)
                    elif tmpImpType == 3:
                        imp4Anim.draw(screen, tmpImpPos[0], tmpImpPos[1], 1)
                    elif tmpImpType == 4:
                        imp5Anim.draw(screen, tmpImpPos[0], tmpImpPos[1], 1)
                    else:
                        imp6Anim.draw(screen, tmpImpPos[0], tmpImpPos[1], 1)
        
        if not levelComplete:
            
            # Display bonus items if on screen
            for localItem in bonusItem:
                localitemPos = localItem.getPosition()
                if localItem.getType() == 0:
                    item_stop.draw(screen, localitemPos[0], localitemPos[1], 1)
                    
                elif localItem.getType() == 1:
                    item_heart.draw(screen, localitemPos[0], localitemPos[1], 1)
                
                elif localItem.getType() == 2:
                    item_clock.draw(screen, localitemPos[0], localitemPos[1], 1)
                    
                else:
                    item_bonus.draw(screen, localitemPos[0], localitemPos[1], 1)
                    
            # Render enemies
            for localEnemies in lvlEnemies:
                localEnemyPos = localEnemies.getEnemyPos()
                if localEnemies.getType() == 0:
                    enemy1.draw(screen, localEnemyPos[0], localEnemyPos[1], localEnemies.getDirection())
                    
                elif localEnemies.getType() == 1:
                    enemy2.draw(screen, localEnemyPos[0], localEnemyPos[1], localEnemies.getDirection())
                    
                else:
                    enemy3.draw(screen, localEnemyPos[0], localEnemyPos[1], localEnemies.getDirection())
                    
            # Render bullet
            if bulletVisible:
                if bulletDir > 0:
                    screen.blit(bullet, bulletX, bulletY)
                else:
                    screen.blit(bullet, bulletX, bulletY, 0, True)
            
        # Lives
        screen.blit(numbers[playerLives], 0, 0)
        screen.blit(livesImg, 10, 0)
        
        # Timer
        if timer.getTime() < 0:
            umachine.draw_text(74, 1, "Time up!", 2)
        else:
            timer.drawTime(screen, numbers, 92, 0, 8)      # x, y, fontspace
            
        # Flash text
        flashText.draw()
        
        # Score/Imps collected
        if score < 10:
            umachine.draw_text(20, 1, "00", 2)
            umachine.draw_text(30, 1, str(score), 2)
        elif score < 100:
            umachine.draw_text(20, 1, "0", 2)
            umachine.draw_text(27, 1, str(score), 2)
        else:
            umachine.draw_text(20, 1, str(score), 2)
        
        # Render player
        if levelComplete:
            # Warp image
            player.draw(screen, playerWarp)
            
            # Render level complete
            umachine.draw_text(30, 41, "Level clear!", 2)
            
        else:
            # Flash player counter if player hit
            if flashPlayer:
                if flashTime > 0:
                    flashTime -= 1
                else:
                    flashTime = flashTimeMax
                    flashPlayer = False
                    
                # Also draw imp splash
                player.drawImpSplash(screen, impImages[impId])
                
            # Draw player
            if flashTime % 2 == 0:
                if movePlayerX != 0:
                    playerPos = player.getPlayerPos()
                    playerAnimWalk.draw(screen, playerPos[0], playerPos[1], movePlayerX)    # Anim when moving
                else:
                    player.draw(screen, playerIdle) # Otherwise just draw idle image
            
    # Render imp screen
    elif gameState == STATE_IMPSCREEN:
        levelImps[0].drawStats(screen, level + 1)
        
    # Render game over
    elif gameState == STATE_GAMEOVER:
        umachine.draw_text(35, 20, "Game over", 2)
        umachine.draw_text(12, 30, "Your final score was", 12)
        umachine.draw_text(50, 40, str(score), 13)
        
#############################################
def startLevel():
    global level, levelComplete, impsOnScreen, flashPlayer, playerAnimDone, flashTime, flashTimeMax, warpPlayed
    
    warpPlayed = False
    levelComplete = False
    playerAnimDone = False
    flashPlayer = False
    flashTime = flashTimeMax
    player.resetPlayer()
    level += 1
    timer = Timer(59) # Reset level timer
    impsOnScreen = 13
    
#############################################
def resetGame():
    global level, score, playerLives, flashTime, flashTimeMax
    
    level = 0
    score = 0
    playerLives = 9
    flashPlayer = False
    flashTime = flashTimeMax
    
#############################################
# Create level imps on load
def createLevelImps(impId):
    global levelImps, gc

    levelImps = []
    gc.collect()
    startX = 10
    startY = 10
    y = 0
    levelImps.append(Imps(-10, -10, impImages[impId], impId))  # hack
    
    for row in range(3):
        x = 0
        for col in range(3):
            levelImps.append(Imps(startX + x, startY + y, impImages[impId], impId))
            x += 40
            
        y += 32
       
    y = 16
    
    for row in range(2):
        x = 20
        for col in range(2):
            levelImps.append(Imps(startX + x, startY + y, impImages[impId], impId))
            x += 40
            
        y += 32
            
#############################################
def createEnemies(level):
    global lvlEnemies
    
    lvlEnemies = []
    enemyTypes = []
    gc.collect()
    thisXLeft = 0
    thisXRight = 100
    thisY = 2
    
    if level == 0:
        enemyTypes.append([0, 0, 0, 0, 0])

    elif level == 1:
        enemyTypes.append([0, 0, 0, 0, 1])
        
    elif level == 2:
        enemyTypes.append([0, 1, 0, 1, 0])
        
    elif level == 3:
        enemyTypes.append([0, 0, 2, 0, 2])
        
    elif level == 4:
        enemyTypes.append([1, 1, 0, 2, 2])
        
    elif level == 5:
        enemyTypes.append([1, 1, 0, 2, 2])
    
    else:
        enemyTypes.append([random.getrandbits(2), random.getrandbits(2), random.getrandbits(2), random.getrandbits(2), random.getrandbits(2)])
    
    for slot in range(5):
        if slot == 0 or slot == 2 or slot == 4:
            if slot == 0:
                lvlEnemies.append(Enemy(enemyTypes[0][slot], thisXLeft + 20, thisY, 1, 1))
            else:
                lvlEnemies.append(Enemy(enemyTypes[0][slot], thisXLeft, thisY, 1, 1))
        else:
            lvlEnemies.append(Enemy(enemyTypes[0][slot], thisXRight, thisY, -1, 1))
        
        thisY += 16
            
#print ("bytes: ", gc.mem_free())

# Initial imp build
createLevelImps(impId)

# Main loop
while True:
    # Read keys
    eventtype = pygame.event.poll()
    if eventtype != pygame.NOEVENT:

				# Keydown events
        if eventtype.type == pygame.KEYDOWN:
        		if eventtype.key == pygame.K_UP:
        		    upPressed = True
        		    if gameState != STATE_GAMEOVER:
        		        if not levelComplete:
        		            playerPos = player.getPlayerPos()
        		            if aLevel.getPlatformType(playerPos[0] + 12, playerPos[1]) == 0:
        		                player.checkUp()

        		if eventtype.key == pygame.K_RIGHT:
        		    rightPressed = True
        		    if gameState != STATE_GAMEOVER:
        		        if not levelComplete:
        		            movePlayerX = moveSpeed

        		if eventtype.key == pygame.K_DOWN:
        		    downPressed = True
        		    if gameState != STATE_GAMEOVER:
        		        if not levelComplete:
        		            playerPos = player.getPlayerPos()
        		            if aLevel.getPlatformType(playerPos[0] + 12, playerPos[1]) == 0:
        		                player.checkDown()

        		if eventtype.key == pygame.K_LEFT:
        		    leftPressed = True
        		    if gameState != STATE_GAMEOVER:
        		        if not levelComplete:
        		            movePlayerX = -moveSpeed

        		if eventtype.key == pygame.BUT_B:
        		    if not bPressed:
        		        bPressed = True
        		        if gameState != STATE_GAMEOVER:
        		            # Show instructions, only from menu
        		            if gameState == STATE_MENU:
        		                gameState = STATE_INSTRUCTIONS
        		                audio.playSfx(snd_select)

        		if eventtype.key == pygame.BUT_A:
        		    if not aPressed:
        		        aPressed = True
        		        
        		        # Move from Imp stats to game
        		        if gameState == STATE_IMPSCREEN:
        		            audio.playSfx(snd_select)
        		            gameState = STATE_GAME
        		            startLevel()
        		            timer = Timer(59) # Level timer in seconds
                            bonusItem = []
                            
                        # Move from Splash to Imp stats
                        if gameState == STATE_GAME and levelComplete:
                            if timer.getTime() <= 0:
                                gameState = STATE_IMPSCREEN
                                
                                tmpImpId = random.getrandbits(2)
                                impId = tmpImpId + random.getrandbits(2)
                                if impId > 5:
                                    impId = 5
                                    
                                # Set enemies
                                createEnemies(level)
    						    
                                # Reset imps
                                for i in levelImps:
    						        i.resetImp()
    						        i.setImage(impImages[impId], impId)
    						        
                                # Freeze enemies at the start to give player a chance to view the level layout
                                freezeEnemies = True
    						    
                                rndLevel = random.getrandbits(3)
                                if rndLevel > 5:
    						        rndLevel = 5
    						    
                                gc.collect()
                                aLevel = Levels([levelMaps[random.getrandbits(4)], levelMaps[random.getrandbits(4)], levelMaps[random.getrandbits(4)], levelMaps[random.getrandbits(4)], levelMaps[random.getrandbits(4)]])
						    
                        # Menu state
                        if gameState == STATE_MENU:
                            audio.playSfx(snd_select)
                            gameState = STATE_IMPSCREEN
                            
                            tmpImpId = random.getrandbits(2)
                            impId = tmpImpId + random.getrandbits(2)
                            if impId > 5:
                                impId = 5
                                
                            # Set enemies
                            createEnemies(level)
                            # Freeze enemies at the start to give player a chance to view the level layout
                            freezeEnemies = True
                            
                            # Reset imps
                            for i in levelImps:
						        i.resetImp()
						        i.setImage(impImages[impId], impId)
        		            
                        # Instructions
                        if gameState >= STATE_INSTRUCTIONS and gameState < STATE_GAME:
                            audio.playSfx(snd_select)
                            gameState += 1
                            if gameState > STATE_INSTRUCTIONS4:
                                gameState = STATE_MENU
        	                    
        	                    
                        # Game over
                        if gameState == STATE_GAMEOVER:
                            audio.playSfx(snd_select)
                            gameState = STATE_MENU
                            resetGame()
        		                
        		if eventtype.key == pygame.BUT_C:
        		    if not cPressed:
        		        cPressed = True
            		    
            		    # Return to menu
            		    if gameState == STATE_GAME:
            		        gameState = STATE_GAMEOVER
            		        
        # Keyup events
        if eventtype.type == pygame.KEYUP:
        		if eventtype.key == pygame.K_UP:
        		    upPressed = False

        		if eventtype.key == pygame.K_RIGHT:
        		    rightPressed = False
        		    movePlayerX = 0

        		if eventtype.key == pygame.K_DOWN:
        		    downPressed = False

        		if eventtype.key == pygame.K_LEFT:
        		    leftPressed = False
        		    movePlayerX = 0

        		if eventtype.key == pygame.BUT_C:
        		    cPressed = False

        		if eventtype.key == pygame.BUT_B:
        		    bPressed = False

        		if eventtype.key == pygame.BUT_A:
        		    aPressed = False

	
	#############################################
	# Update classes/objects
	#############################################
    update()
    #############################################
    # Render
    #############################################
    screen.fill(0)
    render()
	# Sync screen
    pygame.display.flip()
