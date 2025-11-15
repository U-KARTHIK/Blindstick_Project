import machine
import utime

trigger = machine.Pin(0, machine.Pin.OUT)
echo = machine.Pin(1, machine.Pin.IN, machine.Pin.PULL_DOWN)
buzzer = machine.Pin(3, machine.Pin.OUT)
led = machine.Pin(13, machine.Pin.OUT)

def get_distance():
    trigger.low()
    utime.sleep_us(2)
    trigger.high()
    utime.sleep_us(5)
    trigger.low()

    timeout = 10000  # max wait time in microseconds
    start = utime.ticks_us()
    
    while echo.value() == 0:
        if utime.ticks_diff(utime.ticks_us(), start) > timeout:
            return None  # timeout waiting for echo start

    send = utime.ticks_us()

    while echo.value() == 1:
        if utime.ticks_diff(utime.ticks_us(), send) > timeout:
            return None  # timeout waiting for echo end

    received = utime.ticks_us()
    duration = received - send
    distance = (duration * 0.0343) / 2
    return distance

while True:
    led.toggle()
    dist = get_distance()
    if dist is not None and dist < 100:
        buzzer.on()
    else:
        buzzer.off()
    utime.sleep(0.1)
