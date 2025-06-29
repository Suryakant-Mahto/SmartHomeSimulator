import serial
import time
import random

# --- UART Configuration ---
# The serial port device name for UART0 on Raspberry Pi OS.
# If you configured raspi-config as instructed, this should be correct.
SERIAL_PORT = '/dev/ttyS0'
BAUD_RATE = 115200

# --- Communication Protocol ---
# Start marker to indicate the beginning of a data packet
START_MARKER = b'\x02\x05' # Using two unique bytes (STX and ENQ as per ASCII)
# Length of the boolean array in bits
BOOLEAN_ARRAY_LENGTH_BITS = 400
# Calculate the number of bytes needed to store the boolean array
DATA_PAYLOAD_LENGTH_BYTES = (BOOLEAN_ARRAY_LENGTH_BITS + 7) // 8 # Ceiling division

# --- Function to convert boolean list to bytearray ---
def bits_to_bytes(bit_list):
    """
    Converts a list of booleans (or 0/1 integers) into a bytearray.
    Bits are packed LSB first into each byte.
    """
    byte_array = bytearray(DATA_PAYLOAD_LENGTH_BYTES)
    for i, bit in enumerate(bit_list):
        byte_index = i // 8
        bit_position_in_byte = i % 8
        if bit:
            byte_array[byte_index] |= (1 << bit_position_in_byte)
    return byte_array

# --- Main Sender Logic ---
def main():
    try:
        # Initialize serial connection
        ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
        print(f"Serial port {SERIAL_PORT} opened successfully at {BAUD_RATE} baud.")
        time.sleep(2) # Give some time for the serial connection to establish

        while True:
            # 1. Generate a sample 400-bit boolean array
            # For demonstration, let's create a dynamic pattern
            # For example, a simple "on/off" alternating pattern
            #boolean_data = [(i % 2 == 0) for i in range(BOOLEAN_ARRAY_LENGTH_BITS)]

            # Or a random pattern
            boolean_data = [0] * 400
            boolean_data[0]=1
            boolean_data[1]=1

            boolean_data[399]=1
            # boolean_data = [random.choice([0, 1]) for _ in range(BOOLEAN_ARRAY_LENGTH_BITS)]

            print(f"Generated {BOOLEAN_ARRAY_LENGTH_BITS} bits of boolean data (first 10): {boolean_data[:10]}...")

            # 2. Convert the boolean array to bytes
            data_bytes = bits_to_bytes(boolean_data)
            print(f"Converted to {len(data_bytes)} bytes (first 5): {[hex(b) for b in data_bytes[:5]]}...")

            # 3. Construct the packet
            # Packet format: START_MARKER (2 bytes) + DATA_PAYLOAD_LENGTH_BYTES (1 byte) + data_bytes (50 bytes)
            # Ensure data payload length fits in 1 byte (max 255 bytes).
            # Our 50 bytes fits.
            if DATA_PAYLOAD_LENGTH_BYTES > 255:
                print("Error: Data payload length exceeds 255 bytes, single byte length indicator insufficient.")
                break

            packet = START_MARKER + bytes([DATA_PAYLOAD_LENGTH_BYTES]) + data_bytes
            print(f"Sending packet of total size {len(packet)} bytes...")

            # 4. Send the packet over UART
            ser.write(packet)
            print("Packet sent.")

            # Wait before sending the next packet
            time.sleep(1) # Send a new frame every second

    except serial.SerialException as e:
        print(f"Serial port error: {e}")
        print("Please check your serial port configuration and connections.")
    except KeyboardInterrupt:
        print("\nSender stopped by user.")
    finally:
        if 'ser' in locals() and ser.is_open:
            ser.close()
            print("Serial port closed.")

if __name__ == "__main__":
    main()


