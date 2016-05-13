Flasky
======

This repository contains the source code examples for my O'Reilly book [Flask Web Development](http://www.flaskbook.com).

The commits and tags in this repository were carefully created to match the sequence in which concepts are presented in the book. Please read the section titled "How to Work with the Example Code" in the book's preface for instructions.
Install the webserver:
#install github
git clone https://github.com/sylarcp/anita.git
git remote add upstream https://github.com/sylarcp/anita

#install python devel and postgresql-devel
sudo yum install python-devel postgresql-devel
# went to this link and chose your operating system then install 'pip' in your computer.  pip is a python package for installing other python packages.
# http://python-packaging-user-guide.readthedocs.io/en/latest/install_requirements_linux/#installing-pip-setuptools-wheel-with-linux-package-managers

cd anita
#use pip to install all required python packages.
pip install -r requirements.txt
#if permission denied, use following sudo to override.
sudo pip install -r requirements.txt
