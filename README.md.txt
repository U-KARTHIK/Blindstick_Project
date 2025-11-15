# Blindstick Project

This project is a **Blindstick** using Raspberry Pi Pico and MicroPython.  
It uses:
- Ultrasonic sensor (HC-SR04) to detect obstacles
- Buzzer to alert the user
- LED as a status indicator

**How it works:**
- The ultrasonic sensor measures distance continuously.
- If an object is detected closer than 100 cm, the buzzer is activated.
- LED toggles every 0.1 seconds for visual feedback.

**Hardware:**
- Raspberry Pi Pico
- Ultrasonic sensor
- Buzzer
- LED
- Connecting wires

**Usage:**
1. Connect the hardware as per the circuit.
2. Copy `main.py` to the Raspberry Pi Pico using Thonny IDE or similar.
3. Run the code to start obstacle detection.

** Demo Video:**

You can watch the demo of the Blindstick project:

[Click here to view video](videos/demo.mp4)
