from flask import Flask, render_template, url_for
import cv2
import numpy as np
import webbrowser
import threading

app = Flask(__name__)

def run_code():
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        lower_purple = np.array([125, 50, 50])
        upper_purple = np.array([155, 255, 255])

        mask = cv2.inRange(hsv, lower_purple, upper_purple)

        if cv2.countNonZero(mask) > 150:
            webbrowser.open('https://zen-banz-info.w3spaces.com/')
            break

    cap.release()


@app.route('/')
def index():
    threading.Thread(target=run_code).start()
    return render_template('loading.html', css_file=url_for('static', filename='css/styles.css'))

if __name__ == '__main__':
    app.run()
