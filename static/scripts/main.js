/*Loading Function*/
function onReady(callback) {
  var intervalId = window.setInterval(function() {
    if (document.getElementsByTagName('body')[0] !== undefined) {
      window.clearInterval(intervalId);
      callback.call(this);
    }
  }, 1000);
}

function setVisible(selector, visible) {
  document.querySelector(selector).style.display = visible ? 'flex' : 'none';
}

onReady(function() {
  setVisible('.container', true);
  setVisible('#loading', false);
});

/*ColorPicker*/
$(document).ready(function() {
    $('#color-picker').spectrum({
        type: "flat",
        showAlpha: 0,
        showButtons: 0,
        allowEmpty: 0,
        showPalette: 0,
        showPaletteOnly: 1,
        togglePaletteOnly: 1,
        });
});

/*WebSocket with Python*/
var socket = io.connect('http://192.168.1.36:4000');

socket.on('connect', function () {
    console.log('connected')

    document.getElementById('switch_cuisine').addEventListener('change', () => {
        if (document.getElementById('switch_cuisine').checked) {
            socket.emit('on_off_cuisine', { status: 1 });
        } else {
            socket.emit('on_off_cuisine', { status: 0 });
        }
    });

    document.getElementById('switch_chambre').addEventListener('change', () => {
        if (document.getElementById('switch_chambre').checked) {
            socket.emit('on_off_chambre', { status: 1 });
        } else {
            socket.emit('on_off_chambre', { status: 0 });
        }
    });

    /*
    document.getElementById('cuisine').addEventListener('change', () => {
        if (document.getElementById('cuisine').checked) {
            socket.emit('cuisine', { status: 'True' });
        } else {
            socket.emit('cuisine', { status: 'False' });
        }
    });

    document.getElementById('chambre').addEventListener('change', () => {
        if (document.getElementById('chambre').checked) {
            socket.emit('chambre', { status: 'True' });
        } else {
            socket.emit('chambre', { status: 'False' });
        }
    });
    */

    $("#color-picker").on('move.spectrum', function(e, tinycolor) {
        socket.emit('change_rgb', { color: tinycolor.toHexString() });
    });

    document.getElementById('cold_warm').addEventListener('change', (x) => {
        socket.emit('change_white', { white: x.target.value });
    });

    document.getElementById('brightness').addEventListener('change', (x) => {
        socket.emit('change_brightness', { brightness: x.target.value });
    });

});