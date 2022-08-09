from flask import Flask, send_file,send_from_directory,jsonify,redirect,abort,request,render_template
import json
import os
import uuid
import api

template_dir = os.path.abspath('www')
app = Flask(__name__,template_folder=template_dir)

@app.route("/<path:path>")
def static_dir(path):
    return send_from_directory("www", path)

if __name__ == "__main__":
    app.run()
