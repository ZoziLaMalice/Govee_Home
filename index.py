from flask import Flask, render_template, redirect, request
from govee_btled import BluetoothLED

from pygatt.exceptions import NotConnectedError
from govee_btled.errors import ConnectionTimeout

from flask_socketio import SocketIO, emit

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def root():
    try:
        global room_led
        room_led = BluetoothLED('a4:c1:38:53:b5:c9')
        room_led_status = 'connected'
        print('YEAHHHHH')
    except Exception:
        room_led_status = 'disconnected'
        print('FUCKKKKKKK')

    # try:
    #     global kitchen_led
    #     kitchen_led = BluetoothLED('a4:c1:38:e2:f4:10')
    #     kitchen_led_status = 'connected'
    # except Exception:
    #     kitchen_led_status = 'disconnected'

    return render_template('index.html', room=room_led_status, kitchen='disconnected')#kitchen_led_status)

socketio = SocketIO(app)


@socketio.on('on_off_cuisine')
def handle_power_cuisine(json):
    state = json['status']
    print('State = ', state)


@socketio.on('on_off_chambre')
def handle_power_chambre(json):
    state = json['status']
    room_led.set_state(state)


@socketio.on('cuisine')
def handle_cuisine(json):
    cuisine = json['status']
    print('State = ', cuisine)


@socketio.on('chambre')
def handle_chambre(json):
    chambre = json['status']
    print('State = ', chambre)


@socketio.on('change_rgb')
def handle_color(json):
    rgb = json['color']
    room_led.set_color(rgb)


@socketio.on('change_white')
def handle_white(json):
    white = json['white']
    room_led.set_color_white(float(white))


@socketio.on('change_brightness')
def handle_brightness(json):
    brightness = json['brightness']
    room_led.set_brightness(float(brightness))


@socketio.on('connect', namespace='/')
def test_connect():
    print('Connected')

socketio.run(app, debug=True, port=4000, host="0.0.0.0")
