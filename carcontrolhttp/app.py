#!/usr/bin/env python
from flask import Flask, render_template, Response, redirect
from video.camera import Camera 
import cv2
from carcontrol.run import forward, reverse, left, right, stop

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/forward')
def forward_():
    forward()
    return redirect('/')

@app.route('/reverse')
def reverse_():
    reverse()
    return redirect('/')

@app.route('/left')
def left_():
    left()
    return redirect('/')

@app.route('/right')
def right_():
    right()
    return redirect('/')

@app.route('/stop')
def stop_():
    stop()
    return redirect('/')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)