from machine import Pin
import time


motor_pins = [Pin(10, Pin.OUT), Pin(11, Pin.OUT), Pin(12, Pin.OUT), Pin(13, Pin.OUT)]   # pins connected to the ULN2003 driver
data = machine.Pin(7, Pin.OUT)
refresh = machine.Pin(8, Pin.OUT)
clk = machine.Pin(9, Pin.OUT)
sig = [0,1,0,0,0,0,0,1] 


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

data.value(sig[7])
clk.high()
clk.low()
data.value(sig[6])
clk.high()
clk.low()
data.value(sig[5])
clk.high()
clk.low()
data.value(sig[4])
clk.high()
clk.low()
data.value(sig[3])
clk.high()
clk.low()
data.value(sig[2])
clk.high()
clk.low()
data.value(sig[1])
clk.high()
clk.low()
data.value(sig[0])
clk.high()
clk.low()
refresh.high()
refresh.low()

# Move the motor back and forth
while True:
    move_forward()
    time.sleep(1)  # Pause for 1 second
    move_backward()
    time.sleep(1)  # Pause for 1 second

