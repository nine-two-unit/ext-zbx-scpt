#!/usr/bin/env python
# -*- coding: utf-8 -*-

#author: Janssen dos Reis Lima

from pyzabbix import ZabbixAPI
import csv
from progressbar import ProgressBar, Percentage, ETA, ReverseBar, RotatingMarker, Timer


ZABBIX_SERVER = 'http://localhost:8080'

zapi = ZabbixAPI(ZABBIX_SERVER, user='Admin', password='zabbix')
#zapi.login("Admin", "zabbix")

hosts_file = '/Users/gabrielguimaraessilva/Documents/Códigos/api-zabbix/hosts.csv'

arq = csv.reader(open(hosts_file))

linhas = sum(1 for linha in arq)

f = csv.reader(open(hosts_file), delimiter=';')
bar = ProgressBar(maxval=linhas,widgets=[Percentage(), ReverseBar(), ETA(), RotatingMarker(), Timer()]).start()
i = 0

for [hostname,ip] in f:
    hostcriado = zapi.host.create(
        host= hostname,
        status= 1,
        interfaces=[{
            "type": 1,
            "main": 1,
            "useip": 1,
            "ip": ip,
            "dns": "",
            "port": 10050
        }],
        groups=[{
            "groupid": "20"
        }],
        templates=[{
            "templateid": "10186"
        }]
    )


    i += 1
    bar.update(i)

bar.finish
#print " "
