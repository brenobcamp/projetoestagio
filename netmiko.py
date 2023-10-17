import netmiko

def executar_comando(comando, ip, user, senha, device_type):
    equipamento = netmiko.ConnectHandler(device_type=device_type, host=ip, username=user, password=senha)
    output = equipamento.send_command(comando)
    return output