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

# bathroom Door

def bathroomDoorRed(inp):
    deviceArray[4] = inp;

def bathroomDoorGreen(inp):
    deviceArray[3] = inp;

def bathroomDoorBlue(inp):
    deviceArray[2] = inp;

def bathroomDoorMagenta(inp):
    bathroomDoorRed(inp)
    bathroomDoorBlue(inp)
    
def bathroomDoorCyan(inp):
    bathroomDoorGreen(inp)
    bathroomDoorBlue(inp)
    
def bathroomDoorYellow(inp):
    bathroomDoorGreen(inp)
    bathroomDoorRed(inp)
    
def bathroomDoorWhite(inp):
    bathroomDoorRed(inp)
    bathroomDoorGreen(inp)
    bathroomDoorBlue(inp)

def bathroomDoorClear():
    bathroomDoorRed(0)
    bathroomDoorGreen(0)
    bathroomDoorBlue(0)
    
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
    
# bedroom Door

def bedroomDoorRed(inp):
    deviceArray[27] = inp;

def bedroomDoorGreen(inp):
    deviceArray[26] = inp;

def bedroomDoorBlue(inp):
    deviceArray[25] = inp;

def bedroomDoorMagenta(inp):
    bedroomDoorRed(inp)
    bedroomDoorBlue(inp)
    
def bedroomDoorCyan(inp):
    bedroomDoorGreen(inp)
    bedroomDoorBlue(inp)
    
def bedroomDoorYellow(inp):
    bedroomDoorGreen(inp)
    bedroomDoorRed(inp)
    
def bedroomDoorWhite(inp):
    bedroomDoorRed(inp)
    bedroomDoorGreen(inp)
    bedroomDoorBlue(inp)

def bedroomDoorClear():
    bedroomDoorRed(0)
    bedroomDoorGreen(0)
    bedroomDoorBlue(0)
    
# studyroom Door

def studyroomDoorRed(inp):
    deviceArray[30] = inp;

def studyroomDoorGreen(inp):
    deviceArray[29] = inp;

def studyroomDoorBlue(inp):
    deviceArray[28] = inp;

def studyroomDoorMagenta(inp):
    studyroomDoorRed(inp)
    studyroomDoorBlue(inp)
    
def studyroomDoorCyan(inp):
    studyroomDoorGreen(inp)
    studyroomDoorBlue(inp)
    
def studyroomDoorYellow(inp):
    studyroomDoorGreen(inp)
    studyroomDoorRed(inp)
    
def studyroomDoorWhite(inp):
    studyroomDoorRed(inp)
    studyroomDoorGreen(inp)
    studyroomDoorBlue(inp)

def studyroomDoorClear():
    studyroomDoorRed(0)
    studyroomDoorGreen(0)
    studyroomDoorBlue(0)
    
#--------------------- T.V. controls -------------------------

def hallTvPower(inp):
    deviceArray[14] = inp;
def hallTv(inp):
    deviceArray[65] = inp;

def bedroomTvPower(inp):
    deviceArray[57] = inp;
def bedroomTv(inp):
    deviceArray[58] = inp;

#-------------- Washing machine controls --------------------

def washingMachineDrumLight(inp):
    deviceArray[15] = inp;
def washingMachineControlPanel(inp):
    deviceArray[16] = inp;
def washingMachineDrumMotor(inp):
    deviceArray[39] = inp;
    
def washingMachine(inp):
    washingMachineDrumLight(inp)
    washingMachineControlPanel(inp)
    washingMachineDrumMotor(inp)

#------------- Geyser control ----------------------
    
def geyserLightGreen(inp):
    deviceArray[17] = inp;
def geyserLightRed(inp):
    deviceArray[18] = inp;

# ------------ Oven Control --------------------------

def ovenMainLight(inp):
    deviceArray[22] = inp;

def ovenIndicatorRed(inp):
    deviceArray[21] = inp;
    
def ovenIndicatorGreen(inp):
    deviceArray[20] = inp;
    
def ovenIndicatorBlue(inp):
    deviceArray[19] = inp;

def ovenIndicatorMagenta(inp):
    ovenIndicatorRed(inp)
    ovenIndicatorBlue(inp)

def ovenIndicatorCyan(inp):
    ovenIndicatorGreen(inp)
    ovenIndicatorBlue(inp)

def ovenIndicatorYellow(inp):
    ovenIndicatorRed(inp)
    ovenIndicatorGreen(inp)

def ovenIndicatorWhite(inp):
    ovenIndicatorRed(inp)
    ovenIndicatorGreen(inp)
    ovenIndicatorBlue(inp)

def ovenIndicatorClear():
    ovenIndicatorRed(0)
    ovenIndicatorGreen(0)
    ovenIndicatorBlue(0)

# --------------- chimney control -------------------

def chimneyLightRed(inp):
    deviceArray[24] = inp
def chimneyLightBlue(inp):
    deviceArray[23] = inp
    
# -------------- sleep indicator control -------------
# bedroom
def user1BedroomSleep(inp):
    deviceArray[34] = inp;
def user2BedroomSleep(inp):
    deviceArray[33] = inp;
def user3BedroomSleep(inp):
    deviceArray[32] = inp;
    
# hall
def user1HallSleep(inp):
    deviceArray[37] = inp;
def user2HallSleep(inp):
    deviceArray[36] = inp;
def user3HallSleep(inp):
    deviceArray[35] = inp;
    
# studyroom
def user1StudyroomSleep(inp):
    deviceArray[38] = inp;
def user2StudyroomSleep(inp):
    deviceArray[40] = inp;
def user3StudyroomSleep(inp):
    deviceArray[64] = inp; 
    