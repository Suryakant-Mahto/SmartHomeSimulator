import machine
import utime
import _thread

data = machine.Pin(0, machine.Pin.OUT)    #data for 48 bit ICs(horizontral led line)
clk = machine.Pin(1, machine.Pin.OUT)     #clock for 48 bit ic(clock to feed horizontal led ICs)
refresh = machine.Pin(4, machine.Pin.OUT) #refresh for 48 bit ICs(to be refreshed once every 48 bits of data passed)

data_ve = machine.Pin(2, machine.Pin.OUT) #for selecting vertical power line
clk_ve = machine.Pin(3, machine.Pin.OUT)  #clock for 8 bit IC(to be connected with refresh of 48 bit later)

st = .05
ht = .03

def t2():
    segm = [a48,b48,c48,d48,e48,f48]
    
    while True:
        
        for seg in segm:
            highblue(seg)
        for seg in segm:
            lowblue(seg)
            
            
            
        for seg in segm:
            highgreen(seg)
        for seg in segm:
            lowgreen(seg)
            
            
            
        for seg in segm:
            highred(seg)
        for seg in segm:
            lowred(seg)
         
         
        for seg in segm:
            highblue(seg)
        for seg in segm:
            highgreen(seg)
        for seg in segm:
            lowblue(seg)

        for seg in segm:
            highred(seg)
        for seg in segm:
            lowgreen(seg)

        for seg in segm:
            highblue(seg) 
 
            
 
        for seg in segm:
            highgreen(seg)
        for seg in segm:
            lowblue(seg)
        for seg in segm:
            lowgreen(seg)
        for seg in segm:
            lowred(seg)
            
def highblue(y):
    for i in range(0,48,3):
        y[i] = True
        utime.sleep(st)
def lowblue(y):
    for i in range(0,48,3):
        y[i] = False
        utime.sleep(ht)
        
def highgreen(y):
    for i in range(1,48,3):
        y[i] = True
        utime.sleep(st)
def lowgreen(y):
    for i in range(1,48,3):
        y[i] = False
        utime.sleep(ht)
        
def highred(y):
    for i in range(2,48,3):
        y[i] = True
        utime.sleep(st)
def lowred(y):
    for i in range(2,48,3):
        y[i] = False
        utime.sleep(ht)
        

def setmem(inp):
    for i in range(48):
        data.value(inp[i])
        clk.high()
        clk.low()
    clk_ve.high()
    clk_ve.low()
    refresh.high()
    refresh.low()
    utime.sleep(.001)

a48 = [True] * 48
b48 = [False] * 48
c48 = [False] * 48
d48 = [False] * 48
e48 = [False] * 48
f48 = [False] * 48

_thread.start_new_thread(t2,())

#b48[40] = True

while True:
    data_ve.value(1)
    setmem(a48)
    data_ve.value(0)
    setmem(b48)
    setmem(c48)
    setmem(d48)
    setmem(e48)
    setmem(f48)


