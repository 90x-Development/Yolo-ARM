import serial

# Replace '/dev/ttyUSB0' with the appropriate serial port on your Linux system
port = '/dev/ttyACM0'

try:
    connection = serial.Serial(port, 9600)
    print(f"Serial {port} is working well")

    def base_turn(ang):
        rounded_ang = round(ang)
        data = f"b{rounded_ang}"
        connection.write(data.encode())

    def shoulder(ang):
        rounded_ang = round(ang) + 60
        data = f"s{rounded_ang}"
        connection.write(data.encode())

    def elbow(ang):
        rounded_ang = round(ang) + 34
        data = f"e{rounded_ang}"
        connection.write(data.encode())

    def gripper(ang):
        rounded_ang = round(ang)
        data = f"h{rounded_ang}"
        connection.write(data.encode())

except serial.SerialException as e:
    print(f"Failed to open serial port {port}: {e}")

# Add error handling and close the serial connection when done
finally:
    if 'connection' in locals() and connection.is_open:
        connection.close()
