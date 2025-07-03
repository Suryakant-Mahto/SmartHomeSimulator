# library for controlling smart home simulator devices

deviceArray = [0] * 96

# ---------------- Door Indicator Lights ------------------

# kitchen

def kitchenDoorRed(inp):
    deviceArray[1] = inp;

def kitchenDoorGreen(inp):
    deviceArray[0] = inp;

def kitchenDoorBlue(inp):
    deviceArray[31] = inp;

def kitchenDoorMagenta(inp):
    kitchenDoorRed(inp)
    kitchenDoorBlue(inp)
    
def kitchenDoorCyan(inp):
    kitchenDoorGreen(inp)
    kitchenDoorBlue(inp)
    
def kitchenDoorYellow(inp):
    kitchenDoorGreen(inp)
    kitchenDoorRed(inp)
    
def kitchenDoorWhite(inp):
    kitchenDoorRed(inp)
    kitchenDoorGreen(inp)
    kitchenDoorBlue(inp)

def kitchenDoorClear():
    kitchenDoorRed(0)
    kitchenDoorGreen(0)
    kitchenDoorBlue(0)
    
# main Door

def mainDoorRed(inp):
    deviceArray[7] = inp;

def mainDoorGreen(inp):
    deviceArray[6] = inp;

def mainDoorBlue(inp):
    deviceArray[5] = inp;

def mainDoorMagenta(inp):
    mainDoorRed(inp)
    mainDoorBlue(inp)
    
def mainDoorCyan(inp):
    mainDoorGreen(inp)
    mainDoorBlue(inp)
    
def mainDoorYellow(inp):
    mainDoorGreen(inp)
    mainDoorRed(inp)
    
def mainDoorWhite(inp):
    mainDoorRed(inp)
    mainDoorGreen(inp)
    mainDoorBlue(inp)

def mainDoorClear():
    mainDoorRed(0)
    mainDoorGreen(0)
    mainDoorBlue(0)