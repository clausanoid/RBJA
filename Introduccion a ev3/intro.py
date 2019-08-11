#!/usr/bin/env pybricks-micropython
from pybricks import ev3brick as brick
from pybricks.ev3devices import Motor, UltrasonicSensor
from pybricks.parameters import Port
from pybricks.tools import wait
from pybricks.robotics import DriveBase

# Sonido de beep - Nos indica que el programa esta iniciando
brick.sound.beep()

# Hacemos sonar el brick
brick.sound.file(SoundFile.HELLO)

# Beep
brick.sound.beep()

# Beep a 1500hz por un segundo
brick.sound.beep(1500, 1000, 50)

# prendemos los leds de color rojo
brick.light(Color.RED)

# prendemos los leds de color verde
brick.light(Color.GREEN)

# prendemos los leds de color Amber
brick.light(Color.AMBER)

# inicializamos 2 motores y un tanque
left = Motor(Port.B)
right = Motor(Port.C)
robot = DriveBase(left, right, 56, 114)