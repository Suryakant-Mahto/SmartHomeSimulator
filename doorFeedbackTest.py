from machine import Pin
import time
import _thread

led_green = machine.PWM(machine.Pin(25))
pot = machine.ADC(1)
motor_pins = [Pin(10, Pin.OUT), Pin(11, Pin.OUT), Pin(12, Pin.OUT), Pin(13, Pin.OUT)]   # pins connected to the ULN2003 driver

m1 = machine.Pin(16, Pin.OUT)
m2 = machine.Pin(17, Pin.OUT)
m3 = machine.Pin(18, Pin.OUT)
m4 = machine.Pin(19, Pin.OUT)
m5 = machine.Pin(20, Pin.OUT)



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


steps_per_90_degrees = 100  # Steps for 90 degree

def move_forward():          # Function to move the motor forward
    t = 2
    for s in range(steps_per_90_degrees):
        if s > 90:
            t=t+1
        for step in full_step_sequence:
            for i in range(4):
                motor_pins[i].value(step[i])
            time.sleep_ms(t)             # delay based on motor's speed
            

def move_backward():           # Function to move the motor backward
    t = 2
    for s in range(steps_per_90_degrees):
        if s > 90:
            t = t+1
        for step in reversed(full_step_sequence):
            for i in range(4):
                motor_pins[i].value(step[i])
            time.sleep_ms(t)             # delay based on your motor's speed
def print_value():
    f=100          # frequency of led
    onPer = 100	  # intensity of led range[0-100]
    led_green.freq(f)
    dutycycle = int((onPer/100)*65000)
    while True:
        value = pot.read_u16()
        dutycycle = int((onPer/100)*value)
        led_green.duty_u16(dutycycle)
        val = (dutycycle/65535) * 100
        print(pot.read_u16() , val)
        time.sleep(.3)



def read_value():
    value = pot.read_u16()
    dutycycle = int((100/100)*value)
    val = (dutycycle/65535) * 100
    print(pot.read_u16() , val)
    
#_thread.start_new_thread(print_value, ())

m1.value(0)
m2.value(0)
m3.value(0)
m4.value(0)
m5.value(0)

m4.value(1)
# Move the motor back and forth
while True:
    move_forward()
    time.sleep(3)
    print("start")
    read_value()
    time.sleep(2)  # Pause for 1 second
    
    move_backward()
    time.sleep(3)
    read_value()
    time.sleep(2)  # Pause for 1 second
    
    move_backward()
    time.sleep(3)
    read_value()
    time.sleep(2)  # Pause for 1 second
    
    move_forward()
    time.sleep(3)
    read_value()
    time.sleep(2)  # Pause for 1 second


