import machine
import time

led1 = machine.Pin(1, machine.Pin.OUT)
led2 = machine.Pin(2, machine.Pin.OUT)
led3 = machine.Pin(3, machine.Pin.OUT)
led4 = machine.Pin(4, machine.Pin.OUT)

#machine.Pin(1, machine.Pin.OUT).value(1)
while True:
    led1.value(1)
    time.sleep(0.2)
    led2.value(1)
    time.sleep(0.2)
    led3.value(1)
    time.sleep(0.2)
    led4.value(1)
    time.sleep(0.2)
    led1.value(0)
    time.sleep(0.2)
    led2.value(0)
    time.sleep(0.2)
    led3.value(0)
    time.sleep(0.2)
    led4.value(0)
    time.sleep(0.2)

