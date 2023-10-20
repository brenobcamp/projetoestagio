from flask import Flask, render_template, url_for, request, jsonify
import netmiko
import subprocess

def ping_equipamento(ip):
    try:
        result = subprocess.run(["ping", ip, '-c', "4"], stdout=subprocess.PIPE, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as error:
        return error.output


app = Flask(__name__, static_url_path='/static')

@app.route('/', methods=['GET'])
def home():
    database = [{'hostname': "Switch", 'user': "user1", 'password': "suquinho", 'device_type': "cisco_ios", 'ip': "192.168.30.2"}]
    return render_template('home.html', database=database)

@app.route('/post', methods=['GET', 'POST'])
def post():
    return 'yes'

@app.route('/ping', methods=['GET', 'POST'])
def pingar():
    if request.method == 'POST':
        ip = request.form['ip']
        resultados = ping_equipamento(ip)
        return resultados

