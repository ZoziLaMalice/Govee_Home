from flask import Flask, render_template, redirect, request
# from govee_btled import BluetoothLED
from flask_colorpicker import colorpicker

app = Flask(__name__, template_folder='.')
colorpicker(app, local=['static/spectrum.js', 'static/spectrum.css'])

# led = BluetoothLED('a4:c1:38:53:b5:c9')

@app.route('/')
def root():
    return render_template('index.html')


@app.route('/color', methods=['POST'])
def color():
    color = request.form.get('rgb')
    print(color)
    # led.set_state(True)
    # led.set_color(color_hex)
    # led.set_state(False)
    return redirect('/')


@app.route("/slider", methods=["POST"])
def slider():
    slider = request.form["warm"]
    print(slider)
    return redirect('/')

app.run(debug=True, port=4000)
