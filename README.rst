DCPython Website
================

About
-----
The site is built with the `Django web framework <http://www.djangoproject.org>`_. The two major advantages of Django are it gives us an admin site out of the box and many people already know it.

We use **Git version control** and `GitHub <http://www.github.com>`_ for project hosting. Github provides git hosting, bug tracking and wiki.

We use the `Vagrant <http://www.vagrantup.com>`_ development environment. Vagrant allows us to standardize our development and production environments and makes it easy for everybody to get up and running. Vagrant creates a virtual machine, sets up django, database, and everything, then mirrors and syncs the project source code on both your machine and the vm. That way, you make changes to the code on your machine, the changes are mirrored in the vm. Then you run Django on the VM. Now, you can do local development, but you don't have to set up Django and the Database. Very cool.

Installation
------------
You will need to install

 * `VirtualBox <http://www.virtualbox.org>`_ (I found that I needed to restart my computer to get VirtualBox working properly)
 * `Vagrant 1.3.4 <http://www.vagrantup.com>`_ (you cannot use ubuntu package - too old)

Create a `GitHub <http://www.github.com>`_ account.

while signed into github, go to https://github.com/DCPython/dcpython-django and click the "fork" button. This will create a fork (or copy) of the dcpython-django application in your github account.

from the commandline:

::
	# clone your copy of github repository to your working directory (replace <your-username> with  your github username)
	git clone git@github.com:<your-username>/dcpython-django.git 

	cd dcpython-django

	# install Vagrant caching plugin:
	vagrant plugin install vagrant-cachier
	
	# create a new ubuntu virtual machine called precise32
    vagrant box add precise32 http://files.vagrantup.com/precise32.box

    # start the vagrant environment
    vagrant up

    # TODO - shouldn't have to do anything else, but getting a permissions issue with postgres - help needed

    # ssh into the vagrant vm
    vagrant ssh

    cd /vagrant

    # sync the db
    /vagrant/manage.py syncdb --noinput

    # start the django server
    foreman start

You can now visit the django site at localhost:5000

Basic Vagrant
-------------

::
	# all these commands need to be performed from the dcpython-django directory

	# create a new development environment
	vagrant up

	# destroy the development environment
	vagrant destroy

	# ssh into the development environment
	vagrant ssh

	# from the vagrant ssh command line

	# start django
	cd /vagrant
	foreman start

	# django manage.py
	cd /vagrant
	./manage.py <params>

	# you can visit the django site at localhost:5000

Basic Git
---------
We will be using this git branching model: http://nvie.com/posts/a-successful-git-branching-model/

::
	# START NEW FEATURE

	# merge any changes from master
	git pull https://github.com/DCPython/dcpython-django.git develop

	# list all the changes in this branch
	git log

	# create a new feature branch in which to make changes
	git checkout -b "descriptive-name-of-branch"

	# list branches
	git branch

	# switch to another branch
	git checkout "name-of-branch"

	# view status of your files (which have changed, which are staged for commit)
	git status

	# add files to be committed
	git add name-of-file

	# commit changes
	git commit
	# you must add a commit message. first line short title (~50 characters); skip line; detailed description of changes

	
	# MERGE FEATURE

	# merge any changes from master that have occurred while you were programming
	git pull https://github.com/DCPython/dcpython-django.git develop

	# push changes to your github repo
	git push -u origin name-of-branch

	# now, go to github, select the branch you just pushed from the drop-down, then click "pull request" to request your changes be merged with master.

