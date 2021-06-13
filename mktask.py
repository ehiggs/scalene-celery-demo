#!/usr/bin/env python3

from flask import Flask

import app

flask_app = Flask(__name__)

@flask_app.route('/memory', methods=['POST'])
def submit_memory():
    app.loadsamemory.apply_async()
    return 'OK'

@flask_app.route('/cpu', methods=['POST'])
def submit_cpu():
    app.loadsacpu.apply_async()
    return 'OK'

if __name__ == '__main__':
    flask_app.run(host='0.0.0.0')
