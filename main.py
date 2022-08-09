#Author: Binary Bills
#Creation Date: August 6, 2022
#Date Modified: August 8, 2022
#Purpose: The purpose of this program is to remake Flappy Bird. 
#Note: For the best experience using this application, please use a monitor with 
#a resolution of 1920x1080 or higher.

import pygame, sys, FBHelperFuncs, bird

############################################
#              Window Setup                #
############################################
"Initializes all imported pygame modules, sets framerate, and assigns resolution."
pygame.init()
fps = pygame.time.Clock()
screen_width = 576
screen_height = 1024
screenRes = pygame.display.set_mode((screen_width,screen_height))

############################################
#   Variables used throughout the program  #
############################################
"Miscellaneous variables used throughout my code"
gravity = 0.5
current_floor_pos = 0
score = 0
resumeLoop = True
game_active = False
count_once = True
tempMem1 = []
tempMem2 = []

############################################
#            Choosing Sprites              #
############################################
"Initializes the sprites and animations needed for GUI"

#Main Menu
menu = FBHelperFuncs.getTransparentImage("assets/message.png")
menu_Pos = menu.get_rect(center=(288,512))

#Flappy Bird's Animation Frames
midflap = FBHelperFuncs.getTransparentImage("assets/bluebird-midflap.png")
upflap = FBHelperFuncs.getTransparentImage("assets/bluebird-upflap.png")
downflap = FBHelperFuncs.getTransparentImage("assets/bluebird-downflap.png")


#Flappy Bird Animation Set Container
player = bird.Bird(100, int(screen_height/2),[midflap,upflap,downflap])
bird_sprite_container = pygame.sprite.Group()
bird_sprite_container.add(player)

#Background Artwork, Moving Floor, and Pipes
background_image = FBHelperFuncs.getTransparentImage('sprites/background-day.png')
moving_floor_texture = FBHelperFuncs.getImage('sprites/base.png')
pipe_texture = FBHelperFuncs.getTransparentImage('sprites/pipe-green.png')

############################################
#               Game Sound                 #
############################################
"Initializes the sound effects used in the game"
flap_sfx = pygame.mixer.Sound("gameaudio/wing.wav")
die_sfx = pygame.mixer.Sound("gameaudio/hit.wav")
point_sfx = pygame.mixer.Sound("gameaudio/point.ogg")

############################################
#                Pipe Spawn                #
############################################
"Initializes all variables needed for pipes"
pipe_list = []
pipe_height = [400,600,800]
CREATEPIPE = pygame.USEREVENT
pygame.time.set_timer(CREATEPIPE,1200)

############################################
#               Score Font                 #
############################################
"Initializes font used for the score counter"
font = pygame.font.SysFont('Bauhaus 93',60)
white = (255, 255, 255)

############################################
#               Game Loop                  #
############################################
"Main loop for the game"
while(resumeLoop):

    #Draws Background Image to the top left corner of the Screen
    screenRes.blit(background_image,(0,0))

    #Handles Moving Floor For Menu
    current_floor_pos -= 1
    FBHelperFuncs.animate_floor(screenRes,moving_floor_texture,current_floor_pos)
    if current_floor_pos <= (screen_width * -1):
          current_floor_pos = 0

    #Handles events/inputs from the user and the spawning of the pipes
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and game_active == True:
                #User Jumps
                 player.player_movement(gravity,-12)
                 flap_sfx.play()
            if event.button == 1 and game_active == False:
                game_active = True
        if event.type == CREATEPIPE and game_active:
            pipe_list.extend(FBHelperFuncs.create_pipe(pipe_list,pipe_height,pipe_texture))

    #Checks if player has lost. If so, we return to menu screen and reset variables to default values.  
    if (FBHelperFuncs.verify_collision(player,die_sfx,pipe_list) == False):
         player.rect.center = (100,int(screen_height/2))
         player.vel = 0
         score = 0
         pipe_list.clear()
         game_active = False
         count_once = True
         print("PLAYER LOST!")

    #Game is played if true. If false, we go back to main menu.
    if game_active:
       bird_sprite_container.draw(screenRes)

       #Gravity pulls player downward
       player.player_movement(gravity)

      #Handles the pipes appearing on the screen
       pipe_list = FBHelperFuncs.move_pipes(pipe_list)
       FBHelperFuncs.draw_pipes(pipe_list,pipe_texture,screenRes)

       #Handles counting how many pipes the player passed through
       if len(pipe_list) > 0 and count_once:
         if (player.rect.right > pipe_list[-1][0] + 70) and player.rect.left > pipe_list[-1][0] + 70:
             score +=1
             point_sfx.play()
             print("PASSED:", score)
             count_once = False

       #Handles the number of pipes stored in memory at one time
       if (len(pipe_list) > 2 and pipe_list[-1][0] <= 0):
         tempMem1.clear()
         tempMem2.clear()
         tempMem1.extend(pipe_list.pop(0))
         tempMem2.extend(pipe_list.pop(0))
         count_once = True

       FBHelperFuncs.displayScore(str(score),font, white, int(screen_width/2),25, screenRes)
       #Handles Moving Floor In-Game
       current_floor_pos -= 1
       FBHelperFuncs.animate_floor(screenRes,moving_floor_texture,current_floor_pos)
       if current_floor_pos <= (screen_width * -1):
          current_floor_pos = 0
    else:
        #Menu Screen
        screenRes.blit(menu,menu_Pos)
    pygame.display.update()
    fps.tick(120)
  




