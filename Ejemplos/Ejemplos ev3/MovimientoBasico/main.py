#!/usr/bin/env pybricks-micropython

# Estas son las librerias que usara nuestro brick
from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase
import time
# Aqui empezaremos nuestro programa
brick.sound.beep()

# Asignamos el motor izquierdo al puerto A del brick
left_motor = Motor(Port.A)
# Asignamos el motor Derecho al puerto D del brick
right_motor = Motor(Port.D)
# Asignamos el motor de la cabeza al puerto C del brick
head_motor = Motor(Port.C)
# Creamos un par motriz(Par de motores) para que funcionn al unisono
robot = DriveBase(left_motor,right_motor,56,114)
# Este ciclo infinito tendra al brick esperando instrucciones
# De manera que ejecute su programacion adecuadamente
while True:
    # Manejamos hacia adelante a 200 milimetros por segundo
    robot.drive(200, 0)
    # Le damos un tiempo al robot para que procese los comandos
    time.sleep(10)
    # El robot gira 90 grados durante 3 segundos
    robot.drive(0, 90, 3000)
     # Le damos un tiempo al robot para que procese los comandos
    time.sleep(10)
    # El robot retrocede 100 milimetros por segundo durante 2 segundos
    robot.drive_time(-100, 0, 2000)
     # Le damos un tiempo al robot para que procese los comandos
    time.sleep(10)
    # El robot gira 60 grados durante 2 segundos
    robot.drive_time(0, 60, 2000)
     # Le damos un tiempo al robot para que procese los comandos
    time.sleep(10)
    # Corre el motor de la cabeza hasta 500 grados por segundos hasta llegar a 90 grados
    head_motor.run_target(500, 90)
    # Corre el motor de la cabesza hasta 500 grados, en un angulo de 90 grados
    # frenando el motor (0) esperando 10 segundos antes de continuar el ciclo
    head_motor.run_angle(500,90,0,10)
    


    """ Metodos utilizados
    brick.sound.beep 
    Hace que el brick haga un pitido
    
    Motor(Puerto.Letra)
    Asigna un motor a un puerto de letras o numeros
    
    Drivebase(motor1,motor2,distancia_ejes,diametro_ruedas)
    Crea un par motriz, para que los motores funcionen al unisono,
    el brick calcula automaticamente la fuerza que debe poner con la
    distancia entre los ejes y el diametro
    
    drive(velocidad, angulo)
    Mueve un par motriz a cierta velocidad, en cierto angulo
    
    time.sleep(segundos)
    Detiene la aplicacion por el numero de segundos
    
    drive_time(velocidad, angulo, tiempo)
    Mueve un par motriz a cierta velocidad, en un cierto angulo, por 
    un cierto tiempo
    
    run_target(velocidad, angulo)
    Mueve un motor a cierta velocidad hasta llegar a cierto angulo
    
    run_angle(velocidad,angulo,tipo_alto,esperar)
    Mueve un motor a cierta velocidad, a cierto angulo, detieniendo la marcha
    y esperando cierto tiempo antes de ejecutar lo que resta del programa
    
     """