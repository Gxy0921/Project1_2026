from gpiozero import LED,Button
from time import sleep,time
from random import uniform
import os

led=LED(4)
right_button=Button(15,bounce_time=0.1)
left_button=Button(14,bounce_time=0.1)
<<<<<<< HEAD
=======

left_name=input('left player name is')
right_name=input('right player name is')
>>>>>>> yxy

left_name=input("Left plater name is:")
right_name=input("Right plater name is:")

left_score=0
right_score=0
round_num=1

round_active=True

<<<<<<< HEAD
game_over=False

def pressed(button):
<<<<<<< HEAD
    global round_active,left_score,right_score
=======
round_start_time=0

def pressed(button):
    global round_active,left_score,right_score,round_start_time
>>>>>>> yxy2
    if round_active:
       round_active=False

       reaction_time=time()-round_start_time

       if button.pin.number==14:
          print(left_name+'won the game')
          left_score+=1
          print(f"Reaction time:{reaction_time:.3f}seconds")
       else:
          print(right_name+'won the game')
          right_score+=1
          print(f"Reaction time:{reaction_time:.3f}seconds")

       print(f"Score-{left_name}:{left_score},{right_name}:{right_score}")
=======
    global game_over
    if game_over:
       return
    game_over=True

    if button.pin.number==14:
       print(left_name+'won the game')
    else:
       print(right_name+'won the game')
    os._exit(0)
>>>>>>> yxy

try:
    while True:
       round_active=True

       print(f"\n the{round_num}round")
       sleep(1)

       led.on()
       wait_time=uniform(5,10)
       sleep(wait_time)

       led.off()
       round_start_time=time()

       right_button.when_pressed=pressed
       left_button.when_pressed=pressed

       while round_active:
           sleep(0.05)

       round_num+=1
       sleep(1)

except KeyboardInterrupt:
    print('Game over')
    print(f"Final Score-{left_name}:{left_score},{right_name}:{right_score}")
    led.close()
