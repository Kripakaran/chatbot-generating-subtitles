from flask import Flask
from flask import render_template,jsonify,request
import json,ast
import requests
from models import *
from response import *
import random
import os
from sys import argv

@app.route('/')
def hello_world():
    """
    Sample hello world
    """
    return render_template('home.html')

get_random_response = lambda intent:random.choice(response[intent])



@app.route('/chat',methods=["POST"])
def chat():
    """
    chat end point that performs NLU using rasa.ai
    and constructs response from response.py
    """
    try:
        print (request.form["text"])
        response = requests.get("http://localhost:5000/parse",params={"q":request.form["text"]})
        response = response.json()
        jdata = ast.literal_eval(json.dumps(response))
        intent = jdata["intent"]
        intentname=intent["name"]
        if intentname == "translate":
            response_text="Wait for a few minutes till we process the Video"
            cmd2='python auto_run.py /home/aravinth/rasa-site-bot/bot-application'
            os.system(cmd2)
            cmd='python run.py /home/aravinth/Downloads 40 yandex en ta'
            os.system(cmd)
            cmd2='ffmpeg -i /home/aravinth/Downloads/subtitles_en_to_ta.srt /home/aravinth/Downloads/subtitles1.ass'
            os.system(cmd2)
            cmd1='ffmpeg -i /home/aravinth/rasa-site-bot/bot-application/videoplayback.mp4 -vf ass=/home/aravinth/Downloads/subtitles1.ass /home/aravinth/Downloads/tasubtitledmovie.mp4'
            os.system(cmd1)
            cmd2='vlc /home/aravinth/Downloads/tasubtitledmovie.mp4'
            os.system(cmd2)
        else:
            response_text = get_random_response(intentname)
        return jsonify({"status":"success","response":response_text})
    except Exception as e:
        print (e)
        return jsonify({"status":"success","response":"Sorry I am not trained to do that yet..."})


app.config["DEBUG"] = True
if __name__ == "__main__":
    app.run(port=8000)
