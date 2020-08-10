
### nog aanpassen want dit is van het groepsproject corona!!


import os, sys
from flask import Flask, render_template, redirect, request, jsonify 
import time
import random
import json

root_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(root_path)
print(sys.path)
from src.utils.folders_tb import open_json

app = Flask(__name__)


@app.route("/")
def default():
    return "Hi, there :)"


@app.route('/get/Token', methods=['GET'])
def get_token():
    group_id_number = None
    N = "C133"
   
    if 'group_id' in request.args:
        group_id_number = str(request.args['group_id'])
    
    if group_id_number == N:
        return "{'token': C5221570662008902e}" 
        

    else:
         return "This is a message of error" + "<br>" + "<br>" + str(request.args)

#opening json file and converting to dictionary "..\\utils\Mean_per_day.json"
#path = "Roxanna\\Resources\\mean.json"
#path = "C:\\Users\\Roxan\\OneDrive\\Documentos\\Repo_August_project\\Project_August_Corona\\Roxanna\\Resources\\mean.json"
#with open(path, "r+") as outfile:
    #json_mean_total_cases = json.load(outfile)       

#json_mean_total_cases = open_json(path)


@app.route('/get/Json', methods=['GET'])
def get():
    token_id_number = None
    S =  "C5221570662008902e" 
    path = root_path + "\\Resources\\mean.json" 
    #direction to where json is saved.
    #example, still have to calculate the true value of S
    
    
    if 'token_id' in request.args:
        token_id_number = str(request.args['token_id'])
    
    if token_id_number == S:

        return open_json(path)
        #Have to add the information that is assigned to our group 

    else:
         return "This is a message of error" + "<br>" + "<br>" + str(request.args)


def main():
    
    print("STARTING PROCESS")
    print(os.path.dirname(__file__))
    

    settings_file = os.path.dirname(__file__) + "\\settings.json"
    with open(settings_file, "r") as json_file_readed:
        json_readed = json.load(json_file_readed)

    SERVER_RUNNING = json_readed["server_running"]
    
    if SERVER_RUNNING:
        DEBUG = json_readed["debug"]
        HOST = json_readed["host"]
        PORT_NUM = json_readed["port"]
        app.run(debug=DEBUG, host=HOST, port=PORT_NUM)
    else:
        print("Server settings.json doesn't allow to start server. " + 
              "Please, allow it to run it.")
            
if __name__ == "__main__":
    main()