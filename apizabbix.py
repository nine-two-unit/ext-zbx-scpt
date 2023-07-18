from pyzabbix import ZabbixAPI
import configparser

# Comentarios aleatorios de teste
# Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer tempus diam id iaculis convallis. Sed non commodo eros. Suspendisse eu convallis enim. In posuere rutrum tristique. Morbi nec quam id est feugiat ultrices. Vestibulum pellentesque eu augue vel ultricies. Donec non nisi euismod, suscipit massa consectetur, gravida felis.

def connect():
    config = configparser.ConfigParser()
    config.read("config.ini")
    
    user = config.get('zabbix', 'user')
    password = config.get('zabbix', 'password')
    server = config.get('zabbix', 'server')
    
    zapi = ZabbixAPI(server)
    zapi.session.verify = False
    zapi.login(user, password)
    
    return zapi