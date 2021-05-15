# Monitoring
- GIT 
Creating a repository https://github.com/netoperatingsystem/Monitoring.git

- Configuring the environment. Necessary Linux tools
Ubuntu ~$ apt update ~$ apt install python3-pip python3-venv git sqlite3 ~$ pip3 install virtualenv

- Libraries 
~$ apt install ipython3-qtconsole python3-tk python3-sip python3-pyqt5 ~$ sudo pip3 install django

- Project root directory:
"Monitoring" /home/monitoring/

- Creating a work environment:
~$ virtualenv -p python3 pve3 ~$ source pve3/bin/activate (pve3) ~$ pip install -r requirements.txt

- Create a Django project called monitoring:
(pve3) ~/$ django-admin.py startproject monitoring (pve3) ~$ cd monitoring (pve3) ~$ python manage.py migrate
