from flask import Flask, render_template, url_for, request, jsonify
import netmiko
import subprocess

def ping_equipamento(ip):
    result = subprocess.run(["ping", ip, '-c', "4"], stdout=subprocess.PIPE, text=True, check=True)
    return result.stdout

app = Flask(__name__, static_url_path='/static')


@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/post', methods=['GET', 'POST'])
def post():
    return 'yes'

@app.route('/ping', methods=['GET', 'POST'])
def pingar():
    if request.method == 'POST':
        ip = request.form['ip']
        resultados = ping_equipamento(ip)
        return resultados
    # if request
    # resultados = ping_equipamento(ip)
    # return render_template("home.html", resultado=resultados)
    # return request.form['ip']
