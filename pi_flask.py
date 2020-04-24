from flask import Flask, render_template, redirect, url_for
import psutil
import datetime
#import ble_map         #change lib here ------------------
import os

app = Flask(__name__)

def template(title = "HELLO!", text = ""):
    now = datetime.datetime.now()
    timeString = now
    templateDate = {
        'title' : title,
        'time' : timeString,
        'text' : text
        }
    return templateDate

@app.route("/START")
def action():
    message = "oh yeah"
    #message = ble_map.monitor()
    templateData = template(text = message)
    return render_template('pi_01.html', **templateData)



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)