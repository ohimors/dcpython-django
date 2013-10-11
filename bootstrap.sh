export PYTHONPATH=$PYTHONPATH:/vagrant

# update everything
sudo apt-get update
sudo apt-get upgrade

# install Heroku
wget -qO- https://toolbelt.heroku.com/install-ubuntu.sh | sh

# install apt packages
sudo apt-get install postgresql postgresql-server-dev-all python-dev python-pip -y

# install all python modules in requirements.txt
sudo pip install -r /vagrant/requirements.txt

# have to properly set locale for postgres setup
locale-gen en_US.UTF-8
sudo update-locale LANG=en_US.UTF-8

# setup postgresql
sudo -u postgres createuser --superuser vagrant
sudo -u postgres psql -c "alter user postgres with password '1234';"
sudo -u postgres psql -c 'CREATE DATABASE dcpython;'
/vagrant/manage.py syncdb
