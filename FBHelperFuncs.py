import pygame, random

############################################
# 1) Importing Images Helper Functions     #
############################################
def getTransparentImage(directory):
    """Returns a transparent image and performs a 2x scale on it given
       a file directory specified by the user"""
    sprite = pygame.image.load(str(directory)).convert_alpha()
    sprite = pygame.transform.scale2x(sprite)
    return sprite

def getImage(directory):
   """Returns an image and performs a 2x scale on it given
      a file directory specified by the user"""
   sprite = pygame.image.load(str(directory)).convert()
   sprite = pygame.transform.scale2x(sprite)
   return sprite

###########################################
#  2) Animate Moving Floor Function       #
###########################################
def animate_floor(screenRes,floor_texture,floor_pos):
    """Animates Moving floor"""
    screenRes.blit(floor_texture, (floor_pos,900))
    screenRes.blit(floor_texture, (floor_pos + 576, 900))

############################################
#  3)  Collision Function                  #
############################################
def verify_collision(player,die_sound,pipes):
    """Checks if player collided with a pipe, floor, or ceiling"""
    for pipe in pipes:
        if player.rect.colliderect(pipe):
            die_sound.play()
            print("HIT PIPE")
            return False
    if player.rect.top <= -100 or player.rect.bottom >= 900:
       die_sound.play()
       print("HIT FLOOR OR CEILING")
       return False

##################################################
#  4) Pipe Helper Functions and Score Function   #
##################################################
def create_pipe(pipe_list,pipe_height,pipe_texture):
    """Returns coordinates needed to create top and bottom pipe on screen"""
    random_pipe_pos = random.choice(pipe_height)
    top_pipe = pipe_texture.get_rect(midbottom = (700,random_pipe_pos - 300))
    bottom_pipe = pipe_texture.get_rect(midtop = (700,random_pipe_pos))
    return bottom_pipe, top_pipe

def move_pipes(pipes):
    """Moves the pipe five pixels for every frame"""
    for pipe in pipes:
        pipe.centerx -= 5
    return pipes

def draw_pipes(pipes,pipe_texture,screenRes):
    """Draws Pipes to screen"""
    for pipe in pipes:
        if pipe.bottom >= 1024:
         screenRes.blit(pipe_texture,pipe)
        else:
            flip_pipe = pygame.transform.flip(pipe_texture,False,True)
            screenRes.blit(flip_pipe,pipe)

def displayScore(text, font, text_col,x,y,screenRes):
    """Displays user score on screen"""
    img = font.render(text,True,text_col)
    screenRes.blit(img,(x,y))