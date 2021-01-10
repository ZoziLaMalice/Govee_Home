from flask import Flask, render_template, redirect, request

import re
from govee_btled import BluetoothLED

# from flask_colorpicker import colorpicker
# Some junk to solve loading module path from parent dir
from sys import path
from os import getcwd, name
splitter = '\\' if name == 'nt' else '/'
path.append(
    splitter.join(
        getcwd().split(
            splitter
        )[:-1]
    )
)
# End of junk
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
    colors = re.findall(r'\d+', str(color))
    color_hex = '#%02x%02x%02x' % (int(colors[0]),
                                int(colors[1]),
                                int(colors[2]))
    led.set_state(True)
    led.set_color(color_hex)
    return redirect('/')

app.run(debug=True, port=4000)
