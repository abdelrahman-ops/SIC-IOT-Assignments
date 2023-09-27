from gpiozero import LED


led_red = LED(20)

s = input()
if s == "on":
    led_red.on()
elif s == "off":
    led_red.off()
else:
    print("Invalid Command")