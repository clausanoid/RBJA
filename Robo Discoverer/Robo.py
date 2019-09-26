#!/usr/bin/env pybricks-micropython
from pybricks import ev3brick as brick
from pybricks.ev3devices import Motor, UltrasonicSensor
from pybricks.parameters import Port
from pybricks.tools import wait
from pybricks.robotics import DriveBase

# Reproducimos un sonido
brick.sound.beep()
# Inicializamos el sensor ultrasonico.
# Nos permite ver obstaculos mientras se maneja.
obstacle_sensor = UltrasonicSensor(Port.S4)
# Inicialimos 2 motores izquierdo y derecho
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
# Definimos el diametro de la rueda 56 cm.
wheel_diameter = 56
# Definimos la longitud del eje de las ruedas.
axle_track = 114
# El par motriz esta compuesto de dos motores con una llanta cada uno.
# el diametro de la rueda y la longitud del eje seran usados para hacer
# que los motores se mueven a la velocidad correcta con cada comando
robot = DriveBase(left_motor, right_motor, wheel_diameter, axle_track)
# El siguiente ciclo hace que el robot avance hasta que detecta un obstaculo
# si lo detecta se regresa y gira. 

while True:
    # Empezamos a manejar a 200 mm por segundo.
    robot.drive(200, 0)
    # Esperamos a que un obstaculo sea detectado. Hacemos esto
    # al esperar sin hacer nada 10 ms mientras que la distancia
    # sea mayor a 300 mm
    while obstacle_sensor.distance() > 300:
        wait(10)
        # Manejamos hacia atras a 100 mm/s por 2 segundos.
        robot.drive_time(-100, 0, 2000)
        # Giramos 60 grados por 2 segundos
        robot.drive_time(0, 60, 2000)





   