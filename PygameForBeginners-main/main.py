import pygame
import os
import random
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

BORDER = pygame.Rect(WIDTH//2 - 5, 0, 10, HEIGHT)
#BULLET_HIT_SOUND = pygame.mixer.Sound('Assets/Grenade+1.mp3')
#BULLET_FIRE_SOUND = pygame.mixer.Sound('Assets/Gun+Silencer.mp3')

HEALTH_FONT = pygame.font.SysFont('comicsans', 40)
WINNER_FONT = pygame.font.SysFont('comicsans', 100)

FPS = 60
VEL = 5
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


SPACE = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'space.png')), (WIDTH, HEIGHT))

DOMAIN = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'DomainExpand.jpg')), (WIDTH, HEIGHT))

GOJO1img = pygame.image.load(
    os.path.join('Assets', 'gojo1.gif'))
GOJO1 = pygame.transform.rotate(pygame.transform.scale(
    GOJO1img, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)

GOJO2img = pygame.image.load(
    os.path.join('Assets', 'gojo2.gif'))
GOJO2 = pygame.transform.rotate(pygame.transform.scale(
    GOJO2img, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)




def draw_window(red, yellow, red_bullets, yellow_bullets,yellow_bullets1, red_health, yellow_health, yel_parry, red_parry, yel_heat, red_heat):
    #Heat Bars
    red_heat_text = HEALTH_FONT.render(
        "Heat: " + str(red_heat), 1, WHITE)
    yellow_heat_text = HEALTH_FONT.render(
        "Heat: " + str(yel_heat), 1, WHITE)
    
    WIN.blit(red_heat_text, (WIDTH - red_heat_text.get_width() - 10, 50))
    WIN.blit(yellow_heat_text, (10, 50))
    
    
    SPACE.set_alpha(128)
    WIN.blit(SPACE, (0, 0))
    pygame.draw.rect(WIN, BLACK, BORDER)
    

    red_health_text = HEALTH_FONT.render(
        "Health: " + str(red_health), 1, WHITE)
    yellow_health_text = HEALTH_FONT.render(
        "Health: " + str(yellow_health), 1, WHITE)
    WIN.blit(red_health_text, (WIDTH - red_health_text.get_width() - 10, 10))
    WIN.blit(yellow_health_text, (10, 10))

    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP, (red.x, red.y))
    if red_parry:
        WIN.blit(SHIELD, (red.x, red.y))
    if yel_parry:
        WIN.blit(INFINITY, (yellow.x - 25, yellow.y - 25))

    for bullet in red_bullets:
        pygame.draw.rect(WIN, RED, bullet)

    for bullet in yellow_bullets:
        pygame.draw.rect(WIN, YELLOW, bullet)
    for bullet in yellow_bullets1:
        pygame.draw.rect(WIN, YELLOW, bullet)

    pygame.display.update()

def draw_windowDomain(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health):
    randomiser = random.randint(1,3)
    if randomiser == 3:
        YELLOW = (255,0, 0)
    elif randomiser == 2:
        YELLOW = (0,0, 255)
    elif randomiser == 1:
        YELLOW = (255,255,255)
    
    s = pygame.Surface((WIDTH,HEIGHT))
    s.set_alpha(128)
    s.fill(BLACK)
    SPACE.set_alpha(10)
    WIN.blit(s, (0, 0))
    pygame.draw.rect(WIN, BLACK, BORDER)

    red_health_text = HEALTH_FONT.render(
        "Health: " + str(red_health), 1, WHITE)
    yellow_health_text = HEALTH_FONT.render(
        "Health: " + str(yellow_health), 1, WHITE)
    WIN.blit(red_health_text, (WIDTH - red_health_text.get_width() - 10, 10))
    WIN.blit(yellow_health_text, (10, 10))

    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP, (red.x, red.y))

    for bullet in red_bullets:
        pygame.draw.rect(WIN, RED, bullet)

    for bullet in yellow_bullets:
        pygame.draw.rect(WIN, YELLOW, bullet)

    pygame.display.update()

def draw_windowDomainWhite(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health, domainTransparency):
    randomiser = random.randint(1,3)
    if randomiser == 3:
        YELLOW = (255,0, 0)
    elif randomiser == 2:
        YELLOW = (0,0, 255)
    elif randomiser == 1:
        YELLOW = (255,255,255)
    print(domainTransparency)
    s = pygame.Surface((WIDTH,HEIGHT))
    s.set_alpha(domainTransparency)
    s.fill(WHITE)
    WIN.blit(s,(0,0))
    #pygame.draw.rect(WIN, BLACK, BORDER)

    red_health_text = HEALTH_FONT.render(
        "Health: " + str(red_health), 1, WHITE)
    yellow_health_text = HEALTH_FONT.render(
        "Health: " + str(yellow_health), 1, WHITE)
    WIN.blit(red_health_text, (WIDTH - red_health_text.get_width() - 10, 10))
    WIN.blit(yellow_health_text, (10, 10))

    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP, (red.x, red.y))

    for bullet in red_bullets:
        pygame.draw.rect(WIN, RED, bullet)

    for bullet in yellow_bullets:
        pygame.draw.rect(WIN, YELLOW, bullet)

    pygame.display.update()

def draw_windowSpaceDomain(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health, GojoStatus):
    randomiser = random.randint(1,3)
    if randomiser == 3:
        YELLOW = (255,0, 0)
    elif randomiser == 2:
        YELLOW = (0,0, 255)
    elif randomiser == 1:
        YELLOW = (255,255,255)
    DOMAIN.set_alpha(50)
    WIN.blit(DOMAIN, (0, 0))

    red_health_text = HEALTH_FONT.render(
        "Health: " + str(red_health), 1, WHITE)
    yellow_health_text = HEALTH_FONT.render(
        "Health: " + str(yellow_health), 1, WHITE)
    WIN.blit(red_health_text, (WIDTH - red_health_text.get_width() - 10, 10))
    WIN.blit(yellow_health_text, (10, 10))


    if GojoStatus == 1:
        yellIMG = GOJO2
    elif GojoStatus == 0:
        yellIMG = GOJO1
    WIN.blit(yellIMG, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP, (red.x, red.y))

    for bullet in red_bullets:
        pygame.draw.rect(WIN, RED, bullet)

    for bullet in yellow_bullets:
        pygame.draw.rect(WIN, YELLOW, bullet)

    pygame.display.update()

def yellow_handle_movement(keys_pressed, yellow,red,stunned,infinity, domainActive):
    if not stunned:
        velocity = 1
        if domainActive:
            yellow.x = red.x -30
            yellow.y = red.y
        if keys_pressed[pygame.K_a] and yellow.x - VEL > 0:  # LEFT
            yellow.x -= velocity
            infinity.x -= velocity
        if keys_pressed[pygame.K_d] and yellow.x + VEL + yellow.width < BORDER.x:  # RIGHT
            yellow.x += velocity
            infinity.x += velocity
        if keys_pressed[pygame.K_w] and yellow.y - VEL > 0:  # UP
            yellow.y -= velocity
            infinity.y -= velocity
        if keys_pressed[pygame.K_s] and yellow.y + VEL + yellow.height < HEIGHT - 15:  # DOWN
            yellow.y += velocity
            infinity.y += velocity
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


def handle_bullets(yellow_bullets,yellow_bullets1, red_bullets, yellow, red, yellow_vel, infinity, infinityActive, red_parry):
    for bullet in yellow_bullets:
        angle = 95
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            if red_parry == True:
                pygame.event.post(pygame.event.Event(red_counter))
                bullet.x += -(yellow_vel)
                print('reflect main')
                yellow_bullets.remove(bullet)
            else:
                bullet.x += yellow_vel
               
            #yellow_bullets.remove(bullet)
        elif bullet.x > WIDTH+ 1000:
            yellow_bullets.remove(bullet)
        else:
            xAngle = math.sin(math.radians(angle)) * yellow_vel
            yAngle = math.cos(math.radians(angle)) * yellow_vel
            #bullet.x += yellow_vel
            bullet.x += xAngle
            bullet.y -= yAngle

    for bullet in yellow_bullets1:
        angle = 85
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            if red_parry == True:
                pygame.event.post(pygame.event.Event(red_counter))
                bullet.x += -(yellow_vel)
                print('reflect main')
                yellow_bullets1.remove(bullet)
            else:
                bullet.x += yellow_vel
               
            #yellow_bullets.remove(bullet)
        elif bullet.x > WIDTH+ 1000:
            yellow_bullets1.remove(bullet)
        else:
            xAngle = math.sin(math.radians(angle)) * yellow_vel
            yAngle = math.cos(math.radians(angle)) * yellow_vel
            #bullet.x += yellow_vel
            bullet.x += xAngle
            bullet.y -= yAngle


    for bullet in red_bullets:
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            bullet.x -= 50
            #red_bullets.remove(bullet)
        elif infinity.colliderect(bullet) and infinityActive:
            bullet.x -= 1
            print("infinity")

        elif bullet.x < -1000:
            red_bullets.remove(bullet)
        else:
            red_vel = 50
            bullet.x -= red_vel
    

def draw_winner(text):
    draw_text = WINNER_FONT.render(text, 1, WHITE)
    WIN.blit(draw_text, (WIDTH/2 - draw_text.get_width() /
                         2, HEIGHT/2 - draw_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(5000)


#Metraletta Events
metraletta = pygame.USEREVENT + 3
metralettaInitiate = pygame.USEREVENT + 4

#Domain Events
domainExpand = pygame.USEREVENT + 5
domainInitiate = pygame.USEREVENT + 6
domainWhite = pygame.USEREVENT + 7
domainWhiteBeams = pygame.USEREVENT + 19
domainBeams = pygame.USEREVENT + 8
domainBreak = pygame.USEREVENT + 9
domainSpace = pygame.USEREVENT + 10 

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
    infinity.center = yellow.center

    red_bullets = []
    yellow_bullets = []
    yellow_bullets1 = []

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

    yellow_vel = 10

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
    GojoStatus = 0
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == metralettaInitiate:
                pygame.time.set_timer(metraletta, 20, loops=500)
            #Metraletta Events
            if event.type == metraletta:
                bullet = pygame.Rect(
                red.x - 500, red.y + random.randint(-200,200)//2 - 2, 1000, 20)
                red_bullets.append(bullet)
                red_health -= 1

            #Domain Events
            if event.type == domainInitiate:
                pygame.time.set_timer(domainExpand, 1, loops=1)
                yellow_vel = 30
                domainBeamSpeed = 10
                red_stunned = True

            if event.type == domainExpand:
                domain = True
                domainWhiteActive = False
                pygame.time.set_timer(domainBeams, domainBeamSpeed, loops= 1000)

            if event.type == domainBreak:
                domain = False
                domainActive = False
                red_stunned = False
                yel_heatActive = True
                yellow.x = 100
                yellow.y = 300
                
            
            if event.type == domainBeams:
                yellow_damage = 0
                bullet = pygame.Rect(
                yellow.x -800, yellow.y + random.randint(-1000,1000)//2 - 2, 1000, 1)
                yellow_bullets.append(bullet)
                yellow_vel += 0.1
                domainBeamSpeed -= 0.05 

            if event.type == domainSpace:
                domain = False
                domainActive = True
                yellow_damage = 5
                yellow_vel = 30

            if event.type == domainWhite:
                domainWhiteBegin += 0.1
                yellow_damage = 0

            if event.type == domainWhiteBeams:
                bullet = pygame.Rect(
                -200, domainWhiteBeamDistance//50 - 2, 20, 50)
                yellow_bullets.append(bullet)
                domainWhiteBeamDistance += 3000

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


            if event.type == red_counter:
                red_damage = 5
                bullet = pygame.Rect(
                     red.x , red.y + red.height//2 - 2, 20, 100)
                red_bullets.append(bullet)
                bullet.centery = red.centery
                #BULLET_FIRE_SOUND.play()
            #Stun end

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
                #metraletta
                if event.key == pygame.K_m and not red_stunned and red_heat >=100:
                    mSound.play()
                    pygame.time.set_timer(metralettaInitiate, 9400, loops=1)
                    red_heat = 0
                #domain expansion
                if event.key == pygame.K_LSHIFT:
                    if not domain and not domainActive and yel_heat >= 100:
                        domainSound.play()
                        yel_heatActive = False
                        yel_heat = 0
                        pygame.time.set_timer(domainInitiate, 5000, loops=1)
                        pygame.time.set_timer(domainBreak, 33000, loops =1)
                        pygame.time.set_timer(domainSpace, 17000, loops =1)
                        pygame.time.set_timer(domainWhite, 19, loops =255)
                        pygame.time.set_timer(domainWhiteBeams, 200, loops=9)
                        domainWhiteBegin = 0
                        domainWhiteBeamDistance = 0
                        domainWhiteActive = True
                    else:
                        print('domain in use')
                #yellow shoot
                if event.key == pygame.K_LCTRL and not yel_stunned:# and len(yellow_bullets) < MAX_BULLETS:
                    
                    bullet = pygame.Rect(
                        yellow.x + yellow.width, yellow.y + yellow.height//50 - 2, 20, 50)
                    yellow_bullets.append(bullet)

                    leftbullet = pygame.Rect(
                        yellow.x + yellow.width, yellow.y + yellow.height//50 - 2, 20, 50)
                    yellow_bullets1.append(leftbullet)
                    #BULLET_FIRE_SOUND.play()
                #red shoot
                if event.key == pygame.K_RCTRL and not red_stunned:# and len(red_bullets) < MAX_BULLETS:
                    red_damage = 1
                    bullet = pygame.Rect(
                        red.x , red.y + red.height//2 - 2, 1000, 20)
                    red_bullets.append(bullet)
                    #BULLET_FIRE_SOUND.play()
            

            #parry 1 unused
            parry_sound_chooser = random.randint(2,3)
            if parry_sound_chooser == 1:
                parry_sound = parry1
            elif parry_sound_chooser == 2:
                parry_sound = parry2
            elif parry_sound_chooser == 3:
                parry_sound = parry3

            if event.type == RED_HIT:
                if red_parryStatus == True:
                    if not red_parrySoundsOnCD:
                        parry_sound.play()
                        pygame.time.set_timer(red_parry, 100,loops=1)
                        red_parrySoundsOnCD = True
                else:
                    red_health -= yellow_damage
                    if yel_heatActive and yel_heat < 100:
                        yel_heat += yellow_damage/2
                    #BULLET_HIT_SOUND.play()

            if event.type == YELLOW_HIT:
                if yel_parryStatus == True:
                    if not yel_parrySoundsOnCD:
                        parry_sound.play()
                        yel_parrySoundsOnCD = True
                        pygame.time.set_timer(yel_parry, 100,loops=1)
                else:
                    yellow_health -= red_damage
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

        if winner_text != "" and not domainActive:
            draw_winner(winner_text)
            break
        

        if GojoStatus == 1:
            GojoStatus = 0
        elif GojoStatus == 0:
            GojoStatus = 1


        keys_pressed = pygame.key.get_pressed()
        yellow_handle_movement(keys_pressed, yellow,red, yel_stunned, infinity, domainActive)
        red_handle_movement(keys_pressed, red, red_stunned)

        handle_bullets(yellow_bullets,yellow_bullets1, red_bullets, yellow, red, yellow_vel, infinity, infinityActive, red_parryStatus)


        if domain == True:
            draw_windowDomain(red, yellow, red_bullets, yellow_bullets,
                red_health, yellow_health)
        elif domainActive == True:
            draw_windowSpaceDomain(red, yellow, red_bullets, yellow_bullets,
                red_health, yellow_health, GojoStatus)
            if GojoStatus == 1:
                red_health -= 0.5
        elif domainWhiteActive == True:
            draw_windowDomainWhite(red, yellow, red_bullets, yellow_bullets,
                red_health, yellow_health, domainWhiteBegin)
        else: 
            draw_window(red, yellow, red_bullets, yellow_bullets,yellow_bullets1,
                red_health, yellow_health, yel_parryStatus, red_parryStatus, yel_heat, red_heat)

    main()


if __name__ == "__main__":
    main()