import machine

led = machine.Pin(1, machine.Pin.OUT)

led.value(1)