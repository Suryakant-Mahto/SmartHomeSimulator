from machine import UART, Pin
import time

# --- UART Configuration ---
# Use UART0. GP0 is TX, GP1 is RX by default for UART0.
# Make sure these match your wiring from the Zero 2 W.
UART_ID = 0
TX_PIN = 0 # GP0
RX_PIN = 1 # GP1
BAUD_RATE = 115200

# --- Communication Protocol (must match sender) ---
START_MARKER = b'\x02\x05'
START_MARKER_LEN = len(START_MARKER)
# Define BOOLEAN_ARRAY_LENGTH_BITS here as well for consistency
BOOLEAN_ARRAY_LENGTH_BITS = 400
EXPECTED_DATA_PAYLOAD_LENGTH_BYTES = (BOOLEAN_ARRAY_LENGTH_BITS + 7) // 8 # 50 bytes for 400 bits

# --- Function to convert bytearray to boolean list ---
def bytes_to_bits(byte_array, num_bits):
    """
    Converts a bytearray back into a list of booleans (0/1 integers).
    Assumes bits were packed LSB first.
    """
    bit_list = [0] * num_bits
    for i in range(num_bits):
        byte_index = i // 8
        bit_position_in_byte = i % 8
        if byte_array[byte_index] & (1 << bit_position_in_byte):
            bit_list[i] = 1
    return bit_list

# --- Main Receiver Logic ---
def main():
    # Initialize UART
    uart = UART(UART_ID, baudrate=BAUD_RATE, tx=Pin(TX_PIN), rx=Pin(RX_PIN))
    print(f"UART{UART_ID} initialized on GP{TX_PIN} (TX) and GP{RX_PIN} (RX) at {BAUD_RATE} baud.")

    buffer = bytearray()
    last_receive_time = time.ticks_ms()

    while True:
        if uart.any():
            data = uart.read()
            if data:
                buffer.extend(data)
                last_receive_time = time.ticks_ms()
                # print(f"Received {len(data)} bytes, buffer size: {len(buffer)}")
                # print(f"Buffer content: {[hex(b) for b in buffer]}")

        # Check for timeout to clear buffer if no full packet is received
        if time.ticks_diff(time.ticks_ms(), last_receive_time) > 2000 and len(buffer) > 0:
            print("Buffer timeout: Clearing incomplete buffer.")
            buffer = bytearray()

        # Try to find the start marker and process a packet
        if len(buffer) >= START_MARKER_LEN + 1 + EXPECTED_DATA_PAYLOAD_LENGTH_BYTES:
            marker_index = buffer.find(START_MARKER)

            if marker_index != -1:
                # Found the start marker
                # print(f"Start marker found at index {marker_index}.")

                # Remove any junk before the marker
                if marker_index > 0:
                    print(f"Discarding {marker_index} junk bytes before marker.")
                    buffer = buffer[marker_index:]

                # Now buffer should start with the marker
                # Extract length byte (1 byte after marker)
                payload_length_indicator = buffer[START_MARKER_LEN]
                # print(f"Payload length indicator: {payload_length_indicator} bytes.")

                # Check if the indicated length matches our expected length
                if payload_length_indicator == EXPECTED_DATA_PAYLOAD_LENGTH_BYTES:
                    # Check if we have enough bytes for the full packet
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

                        # Remove the processed packet from the buffer
                        buffer = buffer[full_packet_length:]
                    else:
                        # Not enough data for the full payload yet, wait for more
                        # print("Incomplete packet, waiting for more data...")
                        pass # Continue reading
                else:
                    print(f"Error: Mismatched payload length. Expected {EXPECTED_DATA_PAYLOAD_LENGTH_BYTES}, got {payload_length_indicator}.")
                    # Discard the start marker and length, try to find next marker
                    buffer = buffer[START_MARKER_LEN + 1:]
            else:
                # No start marker found in the current buffer, discard a portion
                # print("No start marker found, discarding partial buffer.")
                buffer = buffer[max(0, len(buffer) - START_MARKER_LEN):] # Keep only potential marker part
                time.sleep_ms(10) # Small delay to prevent busy-waiting
        else:
            time.sleep_ms(10) # Small delay to prevent busy-waiting if no data

if __name__ == "__main__":
    main()
