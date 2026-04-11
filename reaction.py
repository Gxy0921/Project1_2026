from gpiozero import LED,Button
from time import sleep
from random import uniform
import os

led=LED(4)
right_button=Button(15,bounce_time=0.1)
left_button=Button(14,bounce_time=0.1)

left_name=input('left player name is')
right_name=input('right player name is')

led.on()
sleep(uniform(5,10))
led.off()

game_over=False

def pressed(button):
    global game_over
    if game_over:
       return
    game_over=True

    if button.pin.number==14:
       print(left_name+'won the game')
    else:
       print(right_name+'won the game')
    os._exit(0)

right_button.when_pressed=pressed
left_button.when_pressed=pressed

while True:
    sleep(0.1)
