# NetOS - Monitoring application
Device monitoring application using SNMP protocol

## Features
- Login + registration panel
- View network port statistics
- Network infrastructure management - adding devices
- Managed users
- Network infrastructure management - adding IP addresses


## Configuring the environment. Necessary Linux tools
Ubuntu ~$ apt update ~$ apt install python3-pip python3-venv git sqlite3 ~$ pip3 install virtualenv

## Libraries 
~$ apt install ipython3-qtconsole python3-tk python3-sip python3-pyqt5 ~$ sudo pip3 install django

## Project root directory:
"Monitoring" /home/monitoring/

## Creating a work environment:
~$ virtualenv -p python3 pve3 ~$ source pve3/bin/activate (pve3) ~$ pip install -r requirements.txt

## Create a Django project called monitoring:
(pve3) ~/$ django-admin.py startproject monitoring (pve3) ~$ cd monitoring (pve3) ~$ python manage.py migrate

## Methodology

Increments

## Language

Python

## TEAM

- Paweł Zborowski s16217, zboro121
- Filip Krzysztofik s16664
- Maciej Sochalski s17817

## KANBAN

https://trello.com/b/itbJodVw/dyplomsnmp
