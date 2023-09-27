from flask import Flask, render_template, request
import RPi.GPIO as GPIO

app = Flask(__name__)

led_pin = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)

@app.route("/")
def led_control():
    return render_template("led_control.html")

@app.route("/led_control_act", methods=["GET"])
def led_control_act():
    action = request.form.get("action")
    if request.method == "GET":
        status = ""
        led = request.args["led"]
        if led == '1':
            GPIO.output(LED, True)
            status = "ON"
        else:
            GPIO.output(LED, False)
            status = "OFF"
               
    return render_template("led_control.html", ret=status)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
