import RPi.GPIO as GPIO
import time

# switch_pins = [4, 5, 6, 12, 13, 16, 17, 18, 19, 20, 21, 22]  # Example GPIOs

GPIO.setmode(GPIO.BCM)
for pin in switch_pins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)  # Ensure all switches are off

def press_button(pin, duration=0.2):
    GPIO.output(pin, GPIO.HIGH)  # "Press" the switch
    time.sleep(duration)
    GPIO.output(pin, GPIO.LOW)   # "Release" the switch

while True:
    if input("Press Enter to simulate button press (or 'q' to quit): ") == 'q':
        break
    else:
        press_button(4)  # Example: press the first button