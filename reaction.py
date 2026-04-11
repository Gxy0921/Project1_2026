from gpiozero import LED,Button
from time import sleep
from random import uniform

led=LED(4)
right_button=Button(15,bounce_time=0.1)
left_button=Button(14,bounce_time=0.1)

left_name=input("Left plater name is:")
right_name=input("Right plater name is:")

round_num=1

round_active=True

def pressed(button):
    global round_active
    if round_active:
       round_active=False
       if button.pin.number==14:
          print(left_name+'won the game')
       else:
          print(right_name+'won the game')

try:
    while True:
       round_active=True

       print(f"\n the{round_num}round")
       sleep(1)

       led.on()
       sleep(uniform(5,10))
       led.off()

       right_button.when_pressed=pressed
       left_button.when_pressed=pressed

       while round_active:
           sleep(0.05)

       round_num+=1
       sleep(1)

except KeyboardInterrupt:
    print('Game over')
    led.close()
