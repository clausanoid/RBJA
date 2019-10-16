#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase


# Asignamos un sensor de color al puerto 1 del brick
color_sensor = ColorSensor(Port.S1)
# Asignamos un sensor ultrasonico al puerto 1 del brick
ultrasonic_sensor = UltrasonicSensor(Port.S2)
# Asignamos un sensor de tacto al puerto 1 del brick
touch_sensor = TouchSensor(Port.S3)
# Asignamos un sensor de giro
gyro_sensor = GyroSensor(Port.S4)

# Obtenemos el color de nuestro sensor 
# colores a detectar: BLACK, BLUE ,GREEN, YELLOW,RED ,WHITE,BROWN
# ORANGE

color = color_sensor.color()

# Si el color es negro mandamos un mensaje a la pantalla del brick
if(color == Color.BLACK):
    print("Negro")
# Si la distancia detectada por el sensor es mayor a 60 cm
# mandamos un mensaje a la pantalla del brick
if(ultrasonic_sensor.distance() > 60):
    print("Lejos")
# Si el sensor de touch esta presionado mandamos un mensaje a la pantalla del brick
if(touch_sensor.pressed( == True)):
    print("Toque")
 # Si el angulo del robot es mayor a 90 grados   mandamos un mensaje a la pantalla del brick
if(gyro_sensor.angle() > 90):
    print("Volteo")


