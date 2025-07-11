import time
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

# ------------------ Fridge control ---------------

def fridgePower(inp):
    deviceArray[42] = inp;
def fridgeDoor(inp):
    deviceArray[41] = inp;
    
# --------------- cooktop control ------------------

def cooktopIndicatorRed(inp):
    deviceArray[66] = inp;
def cooktopIndicatorOrange1(inp):
    deviceArray[67] = inp;
def cooktopIndicatorOrange2(inp):
    deviceArray[68] = inp;
def cooktopIndicatorOrange3(inp):
    deviceArray[69] = inp;

def cooktopSmallTop(inp):
    deviceArray[70] = inp;
def cooktopMediumTop(inp):
    deviceArray[72] = inp;
def cooktopLargeTop(inp):
    deviceArray[73] = inp;
    
def cooktop(inp):
    cooktopIndicatorRed(inp)
    cooktopIndicatorOrange1(0)
    cooktopIndicatorOrange2(0)
    cooktopIndicatorOrange3(0)
    cooktopSmallTop(0)
    cooktopMediumTop(0)
    cooktopLargeTop(0)
    
def cooktopSmall(inp):
    cooktopIndicatorOrange1(inp)
    cooktopSmallTop(inp)
    
def cooktopMedium(inp):
    cooktopIndicatorOrange2(inp)
    cooktopMediumTop(inp)

def cooktopLarge(inp):
    cooktopIndicatorOrange3(inp)
    cooktopLargeTop(inp)
    
# ------------------------ AC controls ---------------------------

# int to 4-bit binary conversion
def IntToBinary(i):
    binaryValue = [0] * 4
    if i == 0:
        return binaryValue;
    elif i == 1:
        binaryValue[3] = 1;
        return binaryValue;
    elif i == 2:
        binaryValue[2] = 1;
        return binaryValue;
    elif i == 3:
        binaryValue[3] = 1;
        binaryValue[2] = 1;
        return binaryValue;
    elif i == 4:
        binaryValue[1] = 1;
        return binaryValue;
    elif i == 5:
        binaryValue[3] = 1;
        binaryValue[1] = 1;
        return binaryValue;
    elif i == 6:
        binaryValue[1] = 1;
        binaryValue[2] = 1;
        return binaryValue;
    elif i == 7:
        binaryValue[3] = 1;
        binaryValue[2] = 1;
        binaryValue[1] = 1;
        return binaryValue;
    elif i == 8:
        binaryValue[0] = 1;
        return binaryValue;
    elif i == 9:
        binaryValue[0] = 1;
        binaryValue[3] = 1;
        return binaryValue;
    else:
        print("Invalid data recieved in int to binary conversion module, expected 0-9");
        return binaryValue;

# commom data
def data0(inp):
    deviceArray[46] = inp;
def data1(inp):
    deviceArray[45] = inp;
def data2(inp):
    deviceArray[44] = inp;
def data3(inp):
    deviceArray[43] = inp;
    
def dataReset():
    data0(0);
    data1(0);
    data2(0);
    data3(0);
    
def resetLatch():
    deviceArray[48] = 0;
    deviceArray[49] = 0;
    
    deviceArray[52] = 0;
    deviceArray[53] = 0;
    
    deviceArray[59] = 0;
    deviceArray[60] = 0;
    
# 7-seg display set data
def setDigit(d,t):
    resetLatch()
    binaryvalue = [0] * 4
    binaryvalue = IntToBinary(t);
    data0(binaryvalue[0]);
    data1(binaryvalue[1]);
    data2(binaryvalue[2]);
    data3(binaryvalue[3]);
    
    deviceArray[d] = 1


# 2 digit data set logic
def setDisplay(d1,d2,t):
    t1 = int(t/10);
    t2 = int(t%10);  
    setDigit(d1,t1)
    time.sleep(0.5)
    setDigit(d2,t2)
    
# Bedroom AC
def bedroomACPower(inp):
    deviceArray[51] = inp;
def bedroomACActive(inp):
    deviceArray[50] = inp;
    bedroomACSetTemp(24);
    
def bedroomACSetTemp(t):
    bedroomACDigit1Index = 48;
    bedroomACDigit2Index = 49;
    setDisplay(bedroomACDigit1Index,bedroomACDigit2Index,t);

# Studyroom AC
def studyroomACPower(inp):
    deviceArray[56] = inp;
def studyroomACActive(inp):
    deviceArray[54] = inp;
    studyroomACSetTemp(24);
    
def studyroomACSetTemp(t):
    bedroomACDigit1Index = 52;
    bedroomACDigit2Index = 53;
    setDisplay(studyroomACDigit1Index,studyroomACDigit2Index,t);

# Hall AC
def hallACPower(inp):
    deviceArray[62] = inp;
def hallACActive(inp):
    deviceArray[61] = inp;
    hallACSetTemp(24);
    
def hallACSetTemp(t):
    hallACDigit1Index = 59;
    hallACDigit2Index = 60;
    setDisplay(hallACDigit1Index,hallACDigit2Index,t);
    
# ------------------ Light controls ----------------------

# Outdoor
def outdoorLightsPower(inp):
    deviceArray(55);
    
def outdoorLight1(inp):
    deviceArray(77);
def outdoorLight2(inp):
    deviceArray(76);
def outdoorLight3(inp):
    deviceArray(75);
def outdoorLight4(inp):
    deviceArray(74);

def OutdoorLights(inp):
    outdoorLight1(inp)
    outdoorLight2(inp)
    outdoorLight3(inp)
    outdoorLight4(inp)

# Kitchen
def kitchenLightsPower(inp):
    deviceArray(63);

def kitchenLight1(inp):
    deviceArray(78);
def kitchenLight2(inp):
    deviceArray(80);
    
def kitchenLights(inp):
    kitchenLight1(inp)
    kitchenLight2(inp)

