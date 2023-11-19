import pygame
import os
import random
import spritesheet  
import math
pygame.font.init()
pygame.mixer.init()

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First Game!")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (0, 100, 255)
YELLOW = (255, 255, 0)
PURPLE =(128,0,128)

BORDER = pygame.Rect(WIDTH//2 - 5, 0, 10, HEIGHT)
#BULLET_HIT_SOUND = pygame.mixer.Sound('Assets/Grenade+1.mp3')
#BULLET_FIRE_SOUND = pygame.mixer.Sound('Assets/Gun+Silencer.mp3')

HEALTH_FONT = pygame.font.SysFont('comicsans', 40)
WINNER_FONT = pygame.font.SysFont('comicsans', 100)

FPS = 60
VEL = 5
BALL_VEL = 1
BULLET_VEL = 100
MAX_BULLETS = 3
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40

YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2

YELLOW_SPACESHIP_IMAGE = pygame.image.load(
   os.path.join('Assets', 'spaceship_yellow.png'))

YELLOW_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('Assets', 'gojo-backshots.gif'))   
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)

RED_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('Assets', 'spaceship_red.png'))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)

SHIELD_IMAGE = pygame.image.load(
    os.path.join('Assets', 'Shield.png'))
SHIELD = pygame.transform.rotate(pygame.transform.scale(
    SHIELD_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)

INFINITY = pygame.transform.rotate(pygame.transform.scale(
    SHIELD_IMAGE, (SPACESHIP_WIDTH + 50, SPACESHIP_HEIGHT + 50)), 270)
BALL_IMAGE = pygame.image.load(
    os.path.join('Assets', 'ball.png'))
BALL = pygame.transform.rotate(pygame.transform.scale(BALL_IMAGE, (50,50)), 270)


SPACE = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'space.png')), (WIDTH, HEIGHT))

DOMAIN = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'DomainExpand.jpg')), (WIDTH, HEIGHT))




def draw_window(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health, yel_parry, red_parry, yel_heat, red_heat, ball):
    #Heat Bars
    red_heat_text = HEALTH_FONT.render(
        "Heat: " + str(red_heat), 1, WHITE)
    yellow_heat_text = HEALTH_FONT.render(
        "Heat: " + str(yel_heat), 1, WHITE)
    
    WIN.blit(red_heat_text, (WIDTH - red_heat_text.get_width() - 10, 50))
    WIN.blit(yellow_heat_text, (10, 50))
    
    
    SPACE.set_alpha(128)
    WIN.blit(SPACE, (0, 0))
    WIN.blit(BALL, (ball.x, ball.y))
    pygame.draw.rect(WIN, BLACK, BORDER)
    

    red_health_text = HEALTH_FONT.render(
        "Health: " + str(red_health), 1, WHITE)
    yellow_health_text = HEALTH_FONT.render(
        "Health: " + str(yellow_health), 1, WHITE)
    WIN.blit(red_health_text, (WIDTH - red_health_text.get_width() - 10, 10))
    WIN.blit(yellow_health_text, (10, 10))

    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP, (red.x, red.y))
    #if red_parry:
        #WIN.blit(INFINITY, (red.x - 25, red.y -25))

    if yel_parry:
        WIN.blit(INFINITY, (yellow.x - 25, yellow.y - 25))

    for bullet in red_bullets:
        pygame.draw.rect(WIN, RED, bullet)

    for bullet in yellow_bullets:
        pygame.draw.rect(WIN, YELLOW, bullet)

    pygame.display.update()



def yellow_handle_movement(keys_pressed, yellow, stunned, infinity):
    if not stunned:
        if keys_pressed[pygame.K_a] and yellow.x - VEL > 0:  # LEFT
            yellow.x -= VEL
            infinity.x -= VEL
        if keys_pressed[pygame.K_d] and yellow.x + VEL + yellow.width < BORDER.x:  # RIGHT
            yellow.x += VEL
            infinity.x += VEL
        if keys_pressed[pygame.K_w] and yellow.y - VEL > 0:  # UP
            yellow.y -= VEL
            infinity.y -= VEL
        if keys_pressed[pygame.K_s] and yellow.y + VEL + yellow.height < HEIGHT - 15:  # DOWN
            yellow.y += VEL
            infinity.y += VEL

def red_handle_movement(keys_pressed, red, stunned):
    if not stunned:
        if keys_pressed[pygame.K_LEFT] and red.x - VEL > BORDER.x + BORDER.width:  # LEFT
            red.x -= VEL
        if keys_pressed[pygame.K_RIGHT] and red.x + VEL + red.width < WIDTH:  # RIGHT
            red.x += VEL
        if keys_pressed[pygame.K_UP] and red.y - VEL > 0:  # UP
            red.y -= VEL
        if keys_pressed[pygame.K_DOWN] and red.y + VEL + red.height < HEIGHT - 15:  # DOWN
            red.y += VEL


def handle_bullets(yellow_bullets, red_bullets, yellow, red, yellow_vel, infinity, infinityActive, red_parry):
    for bullet in yellow_bullets:
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            
            bullet.x += yellow_vel
            #yellow_bullets.remove(bullet)
        elif bullet.x > WIDTH+ 1000:
            yellow_bullets.remove(bullet)
        else:
            bullet.x += yellow_vel


    for bullet in red_bullets:
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            bullet.x -= 50
            #red_bullets.remove(bullet)

        elif bullet.x < -1000:
            red_bullets.remove(bullet)
        else:
            bullet.x -= 50
    
def ballHandle(ball, red, yellow, red_parryStatus, yel_parryStatus, redCD, yelCD):
    if red.colliderect(ball):
        if red_parryStatus and not redCD:
            pygame.event.post(pygame.event.Event(RED_HIT))
            pygame.event.post(pygame.event.Event(playerSwitch))
            print('red has been touched')
        else:
            pygame.event.post(pygame.event.Event(RED_HIT))
        

    if yellow.colliderect(ball) and not yelCD:
        if yel_parryStatus:
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            pygame.event.post(pygame.event.Event(playerSwitch))
            print('yel has been touched')
        else:
            pygame.event.post(pygame.event.Event(YELLOW_HIT))

def draw_winner(text):
    draw_text = WINNER_FONT.render(text, 1, WHITE)
    WIN.blit(draw_text, (WIDTH/2 - draw_text.get_width() /
                         2, HEIGHT/2 - draw_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(5000)

def ballPlay(ball, player,BALL_VEL):
    #Values distance x
    distancex = 0
    distanceY = 0
    if ball.x > player.x:
        distancex = ball.x - player.x
    if ball.x < player.x:
        distancex = player.x - ball.x
    #Values distance y
    if ball.y > player.y:
        distanceY = ball.y - player.y
    if ball.y < player.y:
        distanceY = player.y - ball.y

    #Overshoot prevention
    if distancex <= BALL_VEL:
        ball.x = player.x
    if distanceY <= BALL_VEL:
        ball.y = player.y
    #Default movement
    if ball.x > player.x:
        ball.x -= BALL_VEL
    if ball.x < player.x:
        ball.x += BALL_VEL
    if ball.y > player.y:
        ball.y -= BALL_VEL
    if ball.y < player.y:
        ball.y += BALL_VEL

    


#Parry Events
yel_parry = pygame.USEREVENT + 11
yel_parryEnd = pygame.USEREVENT + 12
yel_parryStunned = pygame.USEREVENT + 13
red_parry = pygame.USEREVENT + 14
red_parryEnd = pygame.USEREVENT + 15
red_parryStunned = pygame.USEREVENT + 16

yel_parryStunnedEnd = pygame.USEREVENT + 17
yel_parryStunnedEnd = pygame.USEREVENT + 18
#20 is next
red_counter = pygame.USEREVENT + 20
playerSwitch = pygame.USEREVENT + 21

mSound = pygame.mixer.Sound('Assets/CeroMetraletta.mp3')
domainSound = pygame.mixer.Sound('Assets/DomainExpand.mp3')
parry1 = pygame.mixer.Sound('Assets/Parry1.mp3')
parry2 = pygame.mixer.Sound('Assets/Parry2.mp3')
parry3  = pygame.mixer.Sound('Assets/Parry3.mp3')


def main():

   
    infinityActive = False
    red = pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    infinity = pygame.Rect(100, 300, 300 ,150)
    ball = pygame.Rect(450, 250, 50 ,50)
    player = red

    infinity.center = yellow.center

    red_bullets = []
    yellow_bullets = []

    red_health = 1000
    yellow_health = 1000

    clock = pygame.time.Clock()
    run = True
    domain = False
    domainActive = False
    domainBeamSpeed = 20
    domainWhiteBegin = 0
    domainWhiteActive = False
    domainWhiteBeamDistance = 0

    yellow_vel = 30

    yel_stunned = False
    red_stunned = False

    yel_parryStatus = False
    red_parryStatus = False

    yel_parryFollowUp = False
    red_parryFollowUp = False

    red_parrySoundsOnCD = False
    yel_parrySoundsOnCD = False

    yel_heat = 0
    red_heat = 0

    yel_heatActive = True
    red_heatActive = True
    #next goal heat bar
    yellow_damage = 5
    red_damage = 1
    BALL_VEL = 5
    maxBALL_VEL = 200

    red_slash = pygame.USEREVENT + 30
    red_slash_frame_num = 1
    red_slash_frame = ''

    import spritesheet
    sprite_sheet_slash = pygame.image.load('Assets/slashsheet.png').convert_alpha()
    sprite_sheet = spritesheet.SpriteSheet(sprite_sheet_slash)
    
    while run:


        frame0 = sprite_sheet.get_image(0,320,320,0.5,BLACK)
        frame1 = sprite_sheet.get_image(1,320,320,0.5,BLACK)
        frame2 = sprite_sheet.get_image(2,320,320,0.5,BLACK)
        frame3 = sprite_sheet.get_image(3,320,320,0.5,BLACK)
        frame4 = sprite_sheet.get_image(4,320,320,0.5,BLACK)
        frame5 = sprite_sheet.get_image(5,320,320,0.5,BLACK)
        WIN.blit(frame0, (0,0))
        WIN.blit(frame1, (100,0))
        WIN.blit(frame2, (200,0))
        WIN.blit(frame3, (300,0))
        WIN.blit(frame4, (400,0))
        WIN.blit(frame5, (500,0))

        red_slash_frames = {
            1:frame0,
            2:frame1,
            3:frame2,
            4:frame3,
            5:frame5,
        
        }

        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()


            if event.type == red_slash:
                if red_slash_frame_num >= 6:
                    red_slash_frame_num = 1
                print(red_slash_frame_num)
                red_slash_frame = red_slash_frames[red_slash_frame_num]
                WIN.blit(red_slash_frame, (red.x-50,red.y-60))
                red_slash_frame_num += 1

            if event.type == playerSwitch:
                if player == red:
                    player = yellow
                else:
                    player = red

                if BALL_VEL <= maxBALL_VEL:
                        BALL_VEL += 0.5
                        print(BALL_VEL)
            #Parry Events
            if event.type == yel_parry:
                yel_parrySoundsOnCD = False
            if event.type == yel_parryEnd:
                yel_parryStatus = False
                infinityActive = False
            if event.type == yel_parryStunned:
                print('blank')
            if event.type == red_parry:
                red_parrySoundsOnCD = False
            if event.type == red_parryEnd:
                red_parryStatus = False
            if event.type == red_parryStunned:
                print('blank')


           

            #Keybinded Events
            if event.type == pygame.KEYDOWN:

                #parry keys
                if event.key == pygame.K_f:
                    yel_parryStatus = True
                    pygame.time.set_timer(yel_parryEnd, 500, loops = 1)
                    infinityActive = True
                if event.key == pygame.K_l:
                    red_parryStatus = True
                    pygame.time.set_timer(red_parryEnd, 500, loops = 1)
                    pygame.time.set_timer(red_slash,20,loops=5)
               
            

            #parry 1 unused
            parry_sound_chooser = random.randint(2,3)
            if parry_sound_chooser == 1:
                parry_sound = parry1
            elif parry_sound_chooser == 2:
                parry_sound = parry2
            elif parry_sound_chooser == 3:
                parry_sound = parry3

            if event.type == RED_HIT:
                if red_parryStatus == True and player == red:
                    if not red_parrySoundsOnCD:
                        parry_sound.play()
                        pygame.time.set_timer(red_parry, 100,loops=1)
                        red_parryStatus = False
                        red_parrySoundsOnCD = True
                else:
                    if player == red:
                        red_health -= 1000
                        if yel_heatActive and yel_heat < 100:
                            yel_heat += yellow_damage/2
                    #BULLET_HIT_SOUND.play()

            if event.type == YELLOW_HIT:
                if yel_parryStatus == True and player == yellow:
                    if not yel_parrySoundsOnCD:
                        parry_sound.play()
                        yel_parrySoundsOnCD = True
                        yel_parryStatus = False
                        pygame.time.set_timer(yel_parry, 100,loops=1)
                else:
                    if player == yellow:
                        yellow_health -= 1000
                        if red_heatActive and red_heat < 100:
                            red_heat += red_damage/2
                        #BULLET_HIT_SOUND.play()
        if yel_heat > 100:
            yel_heat = 100

        if red_heat > 100:
            red_heat = 100

        winner_text = ""
        if red_health <= 0:
            winner_text = "Yellow Wins!"

        if yellow_health <= 0:
            winner_text = "Red Wins!"

        if winner_text != "":
            draw_winner(winner_text)
            break

        keys_pressed = pygame.key.get_pressed()
        yellow_handle_movement(keys_pressed, yellow, yel_stunned, infinity)
        red_handle_movement(keys_pressed, red, red_stunned)

        handle_bullets(yellow_bullets, red_bullets, yellow, red, yellow_vel, infinity, infinityActive, red_parryStatus)

        ballHandle(ball, red, yellow, red_parryStatus, yel_parryStatus, red_parrySoundsOnCD, yel_parrySoundsOnCD)
        ballPlay(ball, player, BALL_VEL)

        draw_window(red, yellow, red_bullets, yellow_bullets,
                red_health, yellow_health, yel_parryStatus, red_parryStatus, yel_heat, red_heat, ball)

    main()


if __name__ == "__main__":
    main()