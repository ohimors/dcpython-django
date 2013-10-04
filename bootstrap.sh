sudo apt-get update
sudo apt-get upgrade
wget -qO- https://toolbelt.heroku.com/install-ubuntu.sh | sh
sudo apt-get install postgresql postgresql-server-dev-all python-dev python-pip -y
sudo pip install -r /vagrant/requirements.txt

export PYTHONPATH=$PYTHONPATH:/vagrant