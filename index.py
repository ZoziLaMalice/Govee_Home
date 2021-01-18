from flask import Flask, render_template, redirect, request
from govee_btled import BluetoothLED
from flask_colorpicker import colorpicker

app = Flask(__name__, template_folder='.')
colorpicker(app, local=['static/spectrum.js', 'static/spectrum.css'])

led = BluetoothLED('a4:c1:38:53:b5:c9')

@app.route('/')
def root():
    return render_template('index.html')


@app.route('/color', methods=['POST'])
def color():
    color = request.form.get('rgb')
    led.set_color(color)
    return redirect('/')


@app.route('/switch', methods=['POST'])
def switch():
    switch = request.form.get('switcher')
    if switch:
        print(switch)
        led.set_state(True)
    # return redirect('/')
        return render_template('index.html', switch="checked")
    else:
        led.set_state(False)
        return render_template('index.html', switch="")


@app.route("/slider", methods=["POST"])
def slider():
    slider = request.form["warm"]
    print(slider)
    return redirect('/')


@app.route("/brightness", methods=["POST"])
def brightness():
    bright = request.form["bright"]
    led.set_brightness(bright)
    return redirect('/')

app.run(debug=True, port=4000, host="0.0.0.0")
