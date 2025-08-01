# ------------ GPU source code (RP2040) ---------------


#  Libraries & Dependencies Import

import time
import machine
import utime
import _thread
from machine import UART, Pin


#   ----------------GPIO Pin Initialization---------------

# GPIO initializatoin user indicator lights
data = machine.Pin(0, machine.Pin.OUT)    #data for 48 bit ICs(horizontral led line)
clk = machine.Pin(1, machine.Pin.OUT)     #clock for 48 bit ic(clock to feed horizontal led ICs)
latch = machine.Pin(4, machine.Pin.OUT)   #latch for 48 bit ICs(to be pulsated once for every 48 bits of data passed)

data_ve = machine.Pin(2, machine.Pin.OUT) #for selecting vertical power line
clk_ve = machine.Pin(3, machine.Pin.OUT)  #clock for 8 bit IC
 
# GPIO initialization for devices control
deviceData = machine.Pin(5, machine.Pin.OUT)
deviceClk = machine.Pin(6, machine.Pin.OUT)
deviceLatch = machine.Pin(7, machine.Pin.OUT)

# GPIO initialization for 7-seg display pairs
acMLatch = machine.Pin(8, machine.Pin.OUT)
acWLatch = machine.Pin(9, machine.Pin.OUT)
acBLatch = machine.Pin(10, machine.Pin.OUT)
verLatch = machine.Pin(11, machine.Pin.OUT)

display7Seg_Clk = machine.Pin(14, machine.Pin.OUT) 
display7Seg_Data = machine.Pin(15, machine.Pin.OUT) 


    
TX_PIN = 12 # GP12
RX_PIN = 13 # GP13

# --- UART Configuration ---
UART_ID = 0
BAUD_RATE = 115200 #speed in  bits/second (115200 bits/sec)

# --- Communication Protocol  ---
START_MARKER = b'\x02\x05'
START_MARKER_LEN = len(START_MARKER)

BOOLEAN_ARRAY_LENGTH_BITS = 400 #Length of data to be recieved in bits
EXPECTED_DATA_PAYLOAD_LENGTH_BYTES = (BOOLEAN_ARRAY_LENGTH_BITS + 7) // 8 # 50 bytes for 400 bits

#---------Global Variables Declaration (for communication between core 0 & core 1) --------------
received_boolean_data = [0] * BOOLEAN_ARRAY_LENGTH_BITS
a48 = [0] * 48
b48 = [0] * 48
c48 = [0] * 48
d48 = [0] * 48
e48 = [0] * 48
f48 = [0] * 48

# function to prepare recieved data for further transmission to hardware compatiblity
def updateFrameData(received_boolean_data):
    global a48,b48,c48,d48,e48,f48
    #print(received_boolean_data)
    print("updatecalled")
    a48 = received_boolean_data[0:48]
    b48 = received_boolean_data[48:96]
    c48 = received_boolean_data[96:144]
    d48 = received_boolean_data[144:192]
    e48 = received_boolean_data[192:240]
    f48 = received_boolean_data[240:288]



# --- Function to convert bytearray to boolean list ---
def bytes_to_bits(byte_array, num_bits):
    bit_list = [0] * num_bits
    for i in range(num_bits):
        byte_index = i // 8
        bit_position_in_byte = i % 8
        if byte_array[byte_index] & (1 << bit_position_in_byte):
            bit_list[i] = 1
    return bit_list

# --- Main Receiver Logic ---

# Initialize UART
uart = UART(UART_ID, baudrate=BAUD_RATE, tx=Pin(TX_PIN), rx=Pin(RX_PIN))
print(f"UART{UART_ID} initialized on GP{TX_PIN} (TX) and GP{RX_PIN} (RX) at {BAUD_RATE} baud.")

buffer = bytearray()
last_receive_time = time.ticks_ms()

def readBuffer():
    global buffer
    global last_receive_time
    global received_boolean_data
    if uart.any():
        data = uart.read()
        if data:
            buffer.extend(data)
            last_receive_time = time.ticks_ms()

    # Check for timeout to clear buffer if no full packet is received
    if time.ticks_diff(time.ticks_ms(), last_receive_time) > 2000 and len(buffer) > 0:
        print("Buffer timeout: Clearing incomplete buffer.")
        buffer = bytearray()

    # Try to find the start marker and process a packet
    if len(buffer) >= START_MARKER_LEN + 1 + EXPECTED_DATA_PAYLOAD_LENGTH_BYTES:
        marker_index = buffer.find(START_MARKER)

        if marker_index != -1:
            # Found the start marker

            # Remove any junk before the marker
            if marker_index > 0:
                print(f"Discarding {marker_index} junk bytes before marker.")
                buffer = buffer[marker_index:]

  
            payload_length_indicator = buffer[START_MARKER_LEN]

            # Check if the indicated length matches the expected length
            if payload_length_indicator == EXPECTED_DATA_PAYLOAD_LENGTH_BYTES:
                # Checks bytes if it contains full packet
                full_packet_length = START_MARKER_LEN + 1 + payload_length_indicator
                if len(buffer) >= full_packet_length:
                    # Extract the data payload
                    data_payload_bytes = buffer[START_MARKER_LEN + 1 : full_packet_length]

                    # Reconstruct the boolean array
                    received_boolean_data = bytes_to_bits(data_payload_bytes, BOOLEAN_ARRAY_LENGTH_BITS)

                    print(f"\n--- Packet Received ---")
                    print(f"Received {len(received_boolean_data)} bits (first 10): {received_boolean_data[:10]}...")
                    print(f"Last 10 bits: {received_boolean_data[-10:]}")
                    print("-----------------------")
                    updateFrameData(received_boolean_data) 
                    # Remove the processed packet from the buffer
                    buffer = buffer[full_packet_length:]
                else:
                    # Not enough data for the full payload yet, wait for more
                    pass # Continue reading
            else:
                print(f"Error: Mismatched payload length. Expected {EXPECTED_DATA_PAYLOAD_LENGTH_BYTES}, got {payload_length_indicator}.")
                # Discard the start marker and length, try to find next marker
                buffer = buffer[START_MARKER_LEN + 1:]
        else:
            # No start marker found in the current buffer, discard a portion
            # print("No start marker found, discarding partial buffer.")
            buffer = buffer[max(0, len(buffer) - START_MARKER_LEN):] # Keep only potential marker part
            
     
    


# Codes to be executed at core 1 (High CPU Utilization)

def Start_scanMatrix():
    
    def setmem(inp):
        for i in range(48):
            data.value(inp[i])
            clk.high()
            clk.low()
        clk_ve.high()
        clk_ve.low()
        latch.high()
        latch.low()
        utime.sleep(.001)
    

    while True:
        data_ve.value(1)
        setmem(a48)
        data_ve.value(0)
        setmem(b48)
        setmem(c48)
        setmem(d48)
        setmem(e48)
        setmem(f48)


def setData():
    dataArray = device_control.deviceArray;
    for x in range (96):
        deviceData.value(dataArray[288 + x])
        deviceClk.high()
        time.sleep(.01)
        deviceClk.low()
        time.sleep(.01)
    latch.high()
    time.sleep(.1)
    latch.low()
    #print("Transmitted")
# ----------- Codes below executes at core 0 (default) -----------------

#initializeUART() # Starts listening for incoming data
_thread.start_new_thread(Start_scanMatrix,()) # Starts matrixScanning Code at core 1



# Optional - program/code hardware state machine using assembly language for sleep animation to split CPU load
while True:
    readBuffer() # Reads any recived data and process it for further transmission to hardware driver circuit 
    if(received_boolean_data[288]):         # flag bit index (devices/door)
        # ----------  Device Output Update -----------------------
        
        
        
        # set 5v and 3.3v serial registor with recieved data
        setData();
        # set 4 pairs of 7-segment display (common data and clock pin , seperate 4 latch pin)
        
        
    else:
        # -----------  Door Management code -------------------
        # Clockwise stepper sequence function
        # Anti-Clockwise stepper sequence function
        # FeedBack Logic Analog to digital converted
        #   ---> Relay control and pin selection
        #   ---> Feeding external 8-bit registor with live door status data for communication with main CPU
        #   ---> Protection Logic against uncontrolled/beyond safe angle door movements
        #   ---> Auto Calibration logic for unusual door movement response
        #   ---> Disable mechanical door movement if Calibration fails in runtime
        
        
    
    
