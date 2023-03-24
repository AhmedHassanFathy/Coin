import pgzrun
import time
from random import randint
#variables
WIDTH = 600
HEIGHT = 600
score = 0
timer = 60
game_over = False
#Actors positions
player = Actor('player')
player.pos = 300,300
coin = Actor('coin')
coin.pos = 150,150
guard = Actor('enemy')
guard.pos = 525,525

def draw ():
    screen.fill("black")
    player.draw()
    coin.draw()
    guard.draw()
    screen.draw.text('score ' + str(score),topleft = (10,10),fontsize = 50)
    screen.draw.text('timer ' + str(round(timer)),topleft = (350,10),fontsize=50)
    if game_over == True:
       screen.fill('black')
       screen.draw.text('Game over: ' + str(score),(200,300),fontsize = 50)
def place_coin ():
    coin.x = randint(50,(WIDTH -50))
    coin.y = randint(50,(HEIGHT -50))

def update (delta):
    global score
    global timer
    global game_over
    if keyboard.left:
        player.x=player.x-3
    if keyboard.right:
        player.x=player.x+3
    if keyboard.up:
        player.y=player.y-3
    if keyboard.down:
        player.y=player.y+3
    if player.colliderect(coin):
        score+=10
        timer+=3
        place_coin ()
    if  timer > 0:
        timer-=delta
    if timer <= 0:
        time_up ()
    if guard.x<player.x:
       guard.x+=0.3
    if guard.x>player.x:
       guard.x-=0.3
    if guard.y<player.y:
       guard.y+=0.3
    if guard.y>player.y:
       guard.y-=0.3
    if player.colliderect(guard):
       time_up()
def time_up():
    global game_over
    game_over = True
    time.sleep(1)
    
    
       
    

pgzrun.go()

    
