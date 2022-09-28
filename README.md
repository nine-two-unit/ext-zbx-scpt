# Zabbix API

## Codes for use Zabbix API
  - ack_event_zabbix.py
  - itservices_zabbix.py
  - auto-add-hosts.py
   
## Installation

You need lib zabbix-api and pip

```sh
# apt-get install python-pip git
# pip install zabbix-api

$ git clone https://github.com/janssenlima/api-zabbix
```

## How to use - examples

#### auto-add-hosts.py
>Change the file path in the code

>Structure hosts.csv file

```sh
hostautomatico1;192.168.0.1
hostautomatico2;192.168.0.2
hostautomatico3;192.168.0.3
hostautomatico4;192.168.0.4
hostautomatico5;192.168.0.5
.
.
.
hostautomatico100;192.168.0.100
```

>Just run

```sh
$ python auto-add-hosts.py
```

#### ack_event_zabbix.py
>Inform the Event ID generated in Zabbix as a parameter

```sh
$ python ack_event_zabbix.py <event.id>
```
#### itservices_zabbix.py
>Inform the function to be used

##### list groups
Syntaxy: get_hostgroups()

By default, it returns all groups. Optionally, you can enter a name to search for the group, including using the wildcard *.
```sh
$ python -c "execfile('itservices_zabbix.py'); get_hostgroups()"
$ python -c "execfile('itservices_zabbix.py'); get_hostgroups('Linux servers')"
$ python -c "execfile('itservices_zabbix.py'); get_hostgroups('*servers*')"
```
##### list hosts of specific group
Syntax:  get_hosts('<name_of_group>')"
Returns all active hosts in a given group. Search only for the exact name of the group.
```sh
$ python -c "execfile('itservices_zabbix.py');  get_hosts('Linux servers')"
```
##### list items of a specific host that has associated trigger
Syntax:  get_items_hosts('<name_of_host>')"
```sh
$ python -c "execfile('itservices_zabbix.py');  get_items_hosts('Apache Web Server')"
```
##### list triggers of a specific host
Syntax:  get_triggers_hosts('<name_of_host>')"
```sh
$ python -c "execfile('itservices_zabbix.py');  get_triggers_hosts('Apache Web Server')"
```
##### delete full service tree
Syntax:  delete_tree_itservices()

Deletes the entire tree
```sh
$ python -c "execfile('itservices_zabbix.py');  delete_tree_itservices()"
```
You can pass groups separated by commas.
```sh
$ python -c "execfile('itservices_zabbix.py');  delete_tree_itservices('Linux servers, Zabbix servers')"
```
##### automatically create service tree
Syntax:  mk_populate()

Included all groups that have enabled hosts, with items and triggers.
```sh
$ python -c "execfile('itservices_zabbix.py');  mk_populate()"
```
You can pass groups separated by commas.
```sh
$ python -c "execfile('itservices_zabbix.py');  mk_populate('Linux servers, Zabbix servers')"
```

### Development

Want to contribute? Great!

Send suggestions, problems, errors etc for janssenreislima@gmail.com

### Todos

 - Create menu for selecting options and call the internal modules
 - Create Docker image 
 - And others

