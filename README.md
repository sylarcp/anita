

This repository contains the source code examples for my O'Reilly book [Flask Web Development](http://www.flaskbook.com).

## Install webanita instruction
```
git clone https://github.com/sylarcp/anita.git
```

install ``` python-devel ```  and ``` postgresql-devel ```
```
sudo yum install python-devel postgresql-devel
```
went to this link and chose your operating system then install 'pip' in your computer.  pip is a python package for installing other python packages.
http://python-packaging-user-guide.readthedocs.io/en/latest/install_requirements_linux/#installing-pip-setuptools-wheel-with-linux-package-managers

Start the virtual envirenment so any installation below here won't affect your system lib.
```
cd anita
source venv/bin/activate
```
use pip to install all required python packages.

```
pip install -r requirements.txt
```
if permission denied, use following sudo to override.
```
sudo pip install -r requirements.txt
python manage.py runserver
```
Go to 127.0.0.1:5000 in your web browser, now you set up a local website!

If you want to run the website in background(devel model) and want other people to access, use this command:
```
gunicorn -w 1 -k gevent -t 100 --log-level=DEBUG manage:app -b gse1.bartol.udel.edu:5000 -D
```
change the gse1.bartol.udel.edu to the domain name(or just IP) of your current machine.
You need open port 5000 in your firewall settings.
gse1.bartol.udel.edu:5000 is the website domain name.

## For developer's use only
```
git remote add upstream https://github.com/sylarcp/anita
```
For git push origin to work:
```
get the ~/.ssh/id_dsa (private key) and put it into ~/.ssh/id_dsa
```
//remove exsiting ssh private key

```
ssh-add -D 
```
// add ssh private key
```
ssh-add ~/.ssh/id_dsa
```
//display ssh private key in use
```
ssh-add -l
vi .git/config
```
change origin's https:// to ssh://

