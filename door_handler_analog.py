# 11 GPIO pins utilized (10,11,12,13,14,15,16,17,18,19,20)

import machine
from machine import Pin
import time

motor_pins = [Pin(10, Pin.OUT), Pin(11, Pin.OUT), Pin(12, Pin.OUT), Pin(13, Pin.OUT)]   # pins connected to the ULN2003 driver

relay1 = machine.Pin(14, machine.Pin.OUT, machine.Pin.PULL_DOWN)
relay2 = machine.Pin(15, machine.Pin.OUT, machine.Pin.PULL_DOWN)

m1 = machine.Pin(16, Pin.OUT)      # Studyroom Door
m2 = machine.Pin(17, Pin.OUT)      # Bathroom Door
m3 = machine.Pin(18, Pin.OUT)      # Bedroom Door
m4 = machine.Pin(19, Pin.OUT)      # Kitchen Door
m5 = machine.Pin(20, Pin.OUT)      # Main Door

sensor0 = machine.ADC(0)
sensor1 = machine.ADC(1)
sensor2 = machine.ADC(2)

def relay_reset():
    relay1.value(0)
    relay2.value(0)
    
def door_selector_reset():
    m1.low()
    m2.low()
    m3.low()
    m4.low()
    m5.low()
    
relay_reset()                   # Initialize relays with default state
door_selector_reset()

full_step_sequence = [          # the order sequence in which the coils are energized for stepping
    [1, 0, 0, 0],
    [1, 1, 0, 0],
    [0, 1, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 1, 0],
    [0, 0, 1, 1],
    [0, 0, 0, 1],
    [1, 0, 0, 1],
]

def move_AntiClock():
    for step in full_step_sequence:
        for i in range(4):
            motor_pins[i].value(step[i])
        time.sleep_ms(2)

def move_Clock():
    for step in reversed(full_step_sequence):
        for i in range(4):
            motor_pins[i].value(step[i])
        time.sleep_ms(2)
        
def open_door(x):
    inp = x
    if True:
        if inp == "main":
            print("main_open")
            relay1.value(1)
            time.sleep(0.5)
            doorPosition = (int(sensor1.read_u16())/65535) * 100
            print(doorPosition)
            m5.high()
            while (doorPosition >= 26):
                doorPosition = (int(sensor1.read_u16())/65535) * 100
                move_AntiClock()
            
            relay_reset()
            door_selector_reset()
            
        elif inp == "kitchen":
            print("kitchen selected")
            doorPosition = (int(sensor0.read_u16())/65535) * 100
            print(doorPosition)
            m4.high()
            while (doorPosition <= 75):
                doorPosition = (int(sensor0.read_u16())/65535) * 100
                move_AntiClock()
            door_selector_reset()
            
        elif inp == "bedroom":
            doorPosition = (int(sensor1.read_u16())/65535) * 100
            m3.high()
            while (doorPosition <= 45):
                doorPosition = (int(sensor1.read_u16())/65535) * 100
                move_AntiClock()
            door_selector_reset()
            
        elif inp == "bathroom":
            doorPosition = (int(sensor2.read_u16())/65535) * 100
            m2.high()
            while (doorPosition <= 65):
                doorPosition = (int(sensor2.read_u16())/65535) * 100
                move_AntiClock()
            door_selector_reset()
            
        elif inp == "studyroom":
            relay2.value(1)
            
            doorPosition = (int(sensor2.read_u16())/65535) * 100
            m1.high()
            while (doorPosition <= 52):
                doorPosition = (int(sensor2.read_u16())/65535) * 100
                move_AntiClock()
            
            relay_reset()
            door_selector_reset()
            
def close_door(x):
    inp = x
    if True:
        if inp == "main":
            relay1.value(1)
            time.sleep(0.5)
            doorPosition = (int(sensor1.read_u16())/65535) * 100
            print("main_close")
            print(doorPosition)
            m5.high()
            while (doorPosition <= 69):
                doorPosition = (int(sensor1.read_u16())/65535) * 100
                move_Clock()
            
            relay_reset()
            door_selector_reset()
            
        elif inp == "kitchen":
            doorPosition = (int(sensor0.read_u16())/65535) * 100
            m4.high()
            while (doorPosition >= 30):
                doorPosition = (int(sensor0.read_u16())/65535) * 100
                move_Clock()
            door_selector_reset()
            
        elif inp == "bedroom":
            doorPosition = (int(sensor1.read_u16())/65535) * 100
            m3.high()
            while (doorPosition >= 9):
                doorPosition = (int(sensor1.read_u16())/65535) * 100
                move_Clock()
            door_selector_reset()
            
        elif inp == "bathroom":
            doorPosition = (int(sensor2.read_u16())/65535) * 100
            m2.high()
            while (doorPosition >= 25):
                doorPosition = (int(sensor2.read_u16())/65535) * 100
                move_Clock()
            door_selector_reset()
            
        elif inp == "studyroom":
            relay2.value(1)
            
            doorPosition = (int(sensor2.read_u16())/65535) * 100
            m1.high()
            while (doorPosition >= 24):
                doorPosition = (int(sensor2.read_u16())/65535) * 100
                move_Clock()
            
            relay_reset()
            door_selector_reset()

def open_door_rev(x):    # *Strictly for testing only (close_door function is ineffective after open_door_rev is called for any door)
    inp = x              # To reset door position first open_door must be called followed by close_door function for that very door)
    if True:
        if inp == "main":
            relay1.value(1)
            m5.high()
            doorPosition = (int(sensor1.read_u16())/65535) * 100
            while (doorPosition <= 99):
                doorPosition = (int(sensor1.read_u16())/65535) * 100
                move_Clock()
            
            relay_reset()
            door_selector_reset()
            
        elif inp == "kitchen":
            doorPosition = (int(sensor0.read_u16())/65535) * 100
            m4.high()
            while (doorPosition >= 12):
                doorPosition = (int(sensor0.read_u16())/65535) * 100
                move_Clock()
            door_selector_reset()
            
        elif inp == "bedroom":
            doorPosition = (int(sensor1.read_u16())/65535) * 100
            m3.high()
            while (doorPosition >= 4):
                doorPosition = (int(sensor1.read_u16())/65535) * 100
                move_Clock()
            door_selector_reset()
            
        elif inp == "bathroom":
            doorPosition = (int(sensor2.read_u16())/65535) * 100
            m2.high()
            while (doorPosition >= 7):
                doorPosition = (int(sensor2.read_u16())/65535) * 100
                move_Clock()
            door_selector_reset()
            
        elif inp == "studyroom":
            relay2.value(1)
            
            doorPosition = (int(sensor2.read_u16())/65535) * 100
            m1.high()
            while (doorPosition >= 8):
                doorPosition = (int(sensor2.read_u16())/65535) * 100
                move_Clock()
            
            relay_reset()
            door_selector_reset()



while True:
    '''
    relay1.high()
    time.sleep(1)
    relay1.low()
    time.sleep(1)
    relay2.high()
    time.sleep(1)
    relay2.low()
    time.sleep(1)
    
    
    
    '''
    open_door("main")
    close_door("main")
    
    open_door("kitchen")
    close_door("kitchen")
    
    open_door("bathroom")
    close_door("bathroom")
    open_door("bedroom")
    close_door("bedroom")
    open_door("studyroom")
    close_door("studyroom")
    
    
    

