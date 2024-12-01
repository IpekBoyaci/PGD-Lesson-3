import pgzrun
import random

TITLE="Shoot The Aliens"

WIDTH=400
HEIGHT=400

#creating a new character(actor) in pygame
alien=Actor('alien')
alien.pos=50,50

message="Game Starts..."

def draw():
    screen.clear()
    screen.fill("green")
    alien.draw()
    screen.draw.text(message,center=(200,20), fontsize=30, color="black")

def place_alien():
    alien.x=random.randint(50,350)
    alien.y=random.randint(50,350)

#on_mouse_down - in built function which gets triggered, when you click on the game screen
def on_mouse_down(pos):
    print("hi")
    global message
    #collidepoint- inbuilt function -checks collision between mouse pointer and actor
    if alien.collidepoint(pos):
        message="Good Job!" 
        place_alien()   
    else:
        message="Try again!"
#place_alien function before pgzrun to place the alien at a random position at the start        
place_alien()
pgzrun.go()