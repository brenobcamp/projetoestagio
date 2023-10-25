from flask import Flask, render_template, url_for, request, jsonify
import netmiko
import subprocess


def ping_equipamento(ip):
    try:
        result = subprocess.run(["ping", ip, '-c', "4"], stdout=subprocess.PIPE, check=True)
        return result.stdout
    except subprocess.CalledProcessError as error:
        return error.output

def executar_comando(comando, ip, user, senha, device_type):
    try:
        equipamento = netmiko.ConnectHandler(device_type=device_type, host=ip, username=user, password=senha)
        output = equipamento.send_command(comando)
        return output
    except Exception as e:
        return str(Exception(f"Erro desconhecido: {str(e)}"))


app = Flask(__name__, static_url_path='/static')


def database(procurar_hostname=False, hostname=None):
    database = [
    {'hostname': 'switch01',
    'ip': '192.168.30.2',
    'username': 'user1',
    'password': 'suquinho',
    'device_type': 'cisco_ios'},
    {'hostname': 'switch02',
    'ip': '192.168.20.2',
    'username': 'user1',
    'password': 'suquinho',
    'device_type': 'cisco_ios'},
    ]
    if procurar_hostname:
        for item in database:
            if item['hostname'] == hostname:
                return item
    
    return database

@app.route('/', methods=['GET'])
def home():
    data = database()
    return render_template('home.html', database=data)

@app.route('/post', methods=['GET', 'POST'])
def post():
    return 'yes'

@app.route('/ping', methods=['GET', 'POST'])
def pingar():
    if request.method == 'POST':
        ip = request.form['ip']
        resultados = ping_equipamento(ip)
        return resultados

@app.route('/sendcommand', methods=['GET', 'POST'])
def comando():
    if request.method == 'POST':
        formulario = request.form
        equipamento_dict = database(True, formulario['equipamento'])
        resultados = executar_comando(formulario['comando'], equipamento_dict['ip'], equipamento_dict['username'], equipamento_dict['password'], equipamento_dict['device_type'])
        return resultados

app.run()

