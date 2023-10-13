from flask import jsonify, render_template, request, redirect, url_for, flash, abort, Blueprint
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import requests
from . import vale
import os
import json
from requests.exceptions import HTTPError
from werkzeug.utils import secure_filename

#configure database
db = SQLAlchemy()
bp = Blueprint("sprintr", __name__)
cwd = os.getcwd()

# compile list of 3d models in 3dmodels directory and store in models
models = []
for root, dir, files, in os.walk(cwd):
    for file in files:
        if file.endswith(".stl"):
            models.append(file[:-4])

# render template for connect page
@bp.route('/', methods=["POST", "GET"])
@bp.route("/connect", methods=["POST", "GET"])
def connect():
    return render_template("connect.html")

#connect to printer
@bp.route("/connect_printer", methods=["POST", "GET"])
def connect_printer():
    print('Attemping to Connect to Printer')
    params = {'password' : 'reprap'}
    try:    
        r = requests.get('http://172.20.10.7/rr_connect', params=params)
        r.raise_for_status()
        jsonRep = r.json()
        print(jsonRep)
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}') 
    except Exception as err:
        print(f'Other error occurred: {err}')
    return jsonify({'result' : 'success'})

#disconnect from printer
@bp.route("/disconnect_printer", methods=["POST", "GET"])
def disconnect_printer():
    try: 
        r = requests.get('http://172.20.10.7/rr_disconnect')
        print("disconnect request sent")
        jsonResp = r.json()
        print(jsonResp)
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
    return jsonify({'result' : 'success'})

#connect to robot
@bp.route("/connect_robot", methods=["POST", "GET"])
def connect_robot():
    #get robot ip from form and connect
    robot_ip = request.form['robot']
    global rc 

    if robot_ip: 
        robot_url = robot_ip + ":80"
        return jsonify({'result' : 'success',
                        'robot_url' : robot_url})
    return jsonify({'result' : 'failure'})


@bp.route("/plan", methods=["POST", "GET"])
def home(): 
    return render_template(
        "valetudoTest.html", models=models
    )

@bp.route("/view/<string:model>", methods=["POST", "GET"])
def view(model):
    print("Viewing model: ", model)
    if os.path.exists(cwd + "/sprintr/static/3dmodels/" + model + ".stl"):
        print("Model found, attempting to render")
        return render_template("view.html", model=model)
        # return render_template("temp.html", model=model)
    print("Model not found")

# delete model from 3dmodels directory when button pressed on plan page
@bp.route("/delete/<string:model>", methods=["POST", "GET"])
def delete(model):
    print("Deleting model: ", model)
    if model in models:
        models.remove(model)
        return redirect(url_for("sprintr.home"))
    print("Model not found")


@bp.route("/home_robot", methods=["POST", "GET"])
def home_robot():
    print("home robot")
    rc.home()
    return jsonify({'result' : 'success' })

#get rc and stop robot
@bp.route("/stop_robot", methods=["POST", "GET"])
def stop_robot():
    print("stop robot")
    rc.stop()
    return jsonify({'result' : 'success' })


# test page to see if I can import and render map
@bp.route("/map", methods=["POST", "GET"])
def map():
    print("map")
    return render_template("map.html")

#parse gcode and send to printer
@bp.route("/send_gcode", methods=["POST", "GET"])
def send_gcode():
    # send gcode to printer
    gcode = request.form['command']
    params = {'gcode': gcode}
    print(f'gcode: {gcode}')
    try:    
        r = requests.get("http://172.20.10.7/rr_gcode", params=params)
        r.raise_for_status()
        print(r.content)
        jsonResp = r.json()
        print(jsonResp)
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}') 
    except Exception as err:
        print(f'Other error occurred: {err}')
    return jsonify({'result' : 'success'})

#Debug screen for 3D Printers
@bp.route("/printer_debug", methods=["POST", "GET"])
def printer_debug():
    return render_template("printer_debug.html")

#Handle Home All button
@bp.route("/home_all", methods=["POST", "GET"])
def home_all():
    print("Home All Axes")
    params = {'gcode': 'G28'}
    try:
        r = requests.get(f'http://172.20.10.7/rr_gcode', params=params)
        r.raise_for_status()
        jsonResp = r.json()
        print(jsonResp)
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
    return jsonify({'result' : 'success'})

#Handle Home X button
@bp.route("/home_x", methods=["POST", "GET"])
def home_x():
    print("Home X Axis")
    params = {'gcode': 'G28 X'}
    try:    
        r = requests.get("http://172.20.10.7/rr_gcode", params=params)
        r.raise_for_status()
        print(r.content)
        jsonResp = r.json()
        print(jsonResp)
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}') 
    except Exception as err:
        print(f'Other error occurred: {err}')
    return jsonify({'result' : 'success'})

#Handle Home Y button
@bp.route("/home_y", methods=["POST", "GET"])
def home_y():
    print("Home Y Axis")
    params = {'gcode': 'G28 Y'}
    try:    
        r = requests.get("http://172.20.10.7/rr_upload", params=params)
        r.raise_for_status()
        print(r.content)
        jsonResp = r.json()
        print(jsonResp)
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}') 
    except Exception as err:
        print(f'Other error occurred: {err}')
    return jsonify({'result' : 'success'})

#Handle Home Z button
@bp.route("/home_z", methods=["POST", "GET"])
def home_z():
    print("Home Z Axis")
    params = {'gcode': 'G28 Z'}
    try:
        r = requests.get(f'http://172.20.10.7/rr_gcode', params=params)
        r.raise_for_status()
        jsonRep = r.json()
        print(jsonRep)
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
    return jsonify({'result' : 'success'})

#Handle Pause button
@bp.route("/pause", methods=["POST", "GET"])
def pause():
    print("Pause")
    params = {'gcode': 'M25'}
    try:
        r = requests.post(f'http://172.20.10.7/rr_gcode', params=params)
        r.raise_for_status()
        jsonRep = r.json()
        print(jsonRep)
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
    return jsonify({'result' : 'success'})

#Handle Resume button
@bp.route("/resume", methods=["POST", "GET"])
def resume():
    print("Resume")
    params = {'gcode': 'M24'}
    try:
        r = requests.post(f'http://172.20.10.7/rr_gcode', params=params)
        r.raise_for_status()
        jsonRep = r.json()
        print(jsonRep)
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
    return jsonify({'result' : 'success'})

#Handle Stop button
@bp.route("/stop", methods=["POST", "GET"])
def stop():
    print("Stop")
    params = {'gcode': 'M0'}
    try:
        r = requests.post(f'http://172.20.10.7/rr_gcode', params=params)
        r.raise_for_status()
        jsonRep = r.json()
        print(jsonRep)
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
    return jsonify({'result' : 'success'})

# print files buttong
@bp.route("/print_files", methods=["POST", "GET"])
def print_files():
    print("Print Files")
    try:    
        r = requests.get("http://172.20.10.7/rr_files")
        r.raise_for_status()
        print(r.content)
        jsonResp = r.json()
        print(jsonResp)
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}') 
    except Exception as err:
        print(f'Other error occurred: {err}')
    return jsonify({'result' : 'success'})