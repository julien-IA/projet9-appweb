from flask import Flask, render_template, redirect, url_for, request
import os
import requests, base64
import json
# import matplotlib.pyplot as plt

app = Flask(__name__)
# API_GET_ID_USER = "http://localhost:7071/api/HttpGetIdUser"
API_GET_ID_USER = "https://funcp9app.azurewebsites.net/api/HttpGetIdUser"
# API_GET_RECO = "http://localhost:7071/api/HttpContentBaseReco"
API_GET_RECO = "https://funcp9app.azurewebsites.net/api/HttpContentBaseReco"

@app.route('/')
def index():
    response = requests.get(url = API_GET_ID_USER)
    # On récupère la liste des id des utilisateurs et on la passe à notre render
    liste_id = json.loads(response.text)
    return render_template('index.html', liste_id=liste_id)

@app.route('/reco', methods=["POST"])
def get_reco():
    print("get_reco")
    id_user = request.form.get('id_user')
    param_reco = request.form.get('param_reco')
    param_ref = request.form.get('param_ref')
    param_nb_reco1 = request.form.get('param_nb_reco1')
    param_nb_reco2 = request.form.get('param_nb_reco2')

    data = {"iduser": id_user,"paramreco": param_reco,"paramref": param_ref,"nbreco1": param_nb_reco1,"nbreco2": param_nb_reco2}
    data_json = json.dumps(data)
    r = requests.post(url = API_GET_RECO, json = data_json)
    result = json.loads(r.text)
    print(result)
    return result
    

if __name__ == "__main__":
    app.run(host ='0.0.0.0', port = 5000)