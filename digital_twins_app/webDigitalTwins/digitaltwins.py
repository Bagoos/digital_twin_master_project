import requests
from flask import Flask, render_template
import json

app = Flask(__name__)
azureToken = ''
azureUrl = ""



@app.route('/fournisseurMatPremiere')
def digitalTwinsFournisseurMatPremiere():
    token = azureToken
    authorization = 'Bearer ' + token

    req = requests.post(
    url= azureUrl,
    headers={
        'Authorization': authorization,
        'Content-Type': 'application/json',
    },
    json={
        "query" : "SELECT * FROM DIGITALTWINS T WHERE T.$dtId IN  ['fournisseurMiel', 'fournisseurEtiquette', 'fournisseurPot']"
    })

    resp = json.loads(req.text)

    return render_template('fournisseurMatPremiere.html', data=resp['value'])



@app.route('/transporteurMatPremiere')
def digitalTwinsTransporteurMatPremiere():
    token = azureToken
    authorization = 'Bearer ' + token

    req = requests.post(
    url= azureUrl,
    headers={
        'Authorization': authorization,
        'Content-Type': 'application/json',
    },
    json={
        "query" : "SELECT * FROM DIGITALTWINS T WHERE T.$dtId IN  ['transportMiel', 'transportEtiquette', 'transportPot', 'fournisseurMiel', 'fournisseurEtiquette', 'fournisseurPot']"
    })

    resp = json.loads(req.text)

    return render_template('transporteurMatPremiere.html', data=resp['value'])



@app.route('/fabricant')
def digitalTwinsFabricant():
    token = azureToken
    authorization = 'Bearer ' + token

    req = requests.post(
    url= azureUrl,
    headers={
        'Authorization': authorization,
        'Content-Type': 'application/json',
    },
    json={
        "query" : "SELECT * FROM DIGITALTWINS T WHERE T.$dtId IN  ['stockageMiel', 'stockageEtiquette', 'stockagePot', 'fabricationPotDeMiel', 'testQualiteProduit', 'stockagePotDeMiel', 'transportMiel', 'transportEtiquette', 'transportPot']"
    })

    resp = json.loads(req.text)

    return render_template('fabricant.html', data=resp['value'])



@app.route('/transporteurProduit')
def digitalTwinsTransporteurProduit():
    token = azureToken
    authorization = 'Bearer ' + token

    req = requests.post(
    url= azureUrl,
    headers={
        'Authorization': authorization,
        'Content-Type': 'application/json',
    },
    json={
        "query" : "SELECT * FROM DIGITALTWINS T WHERE T.$dtId IN  ['transportPotDeMiel', 'stockagePotDeMielTransporteur', 'stockagePotDeMiel']"
    })

    resp = json.loads(req.text)

    return render_template('transporteurProduit.html', data=resp['value'])



@app.route('/distributeurProduit')
def digitalTwinsDistributeurProduit():
    token = azureToken
    authorization = 'Bearer ' + token

    req = requests.post(
    url= azureUrl,
    headers={
        'Authorization': authorization,
        'Content-Type': 'application/json',
    },
    json={
        "query" : "SELECT * FROM DIGITALTWINS T WHERE T.$dtId IN  ['stockagePotDeMielDistributeur', 'transportPotDeMiel']"
    })

    resp = json.loads(req.text)

    return render_template('distributeurProduit.html', data=resp['value'])



if __name__ == '__main__':
   app.run(debug=True)
