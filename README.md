# Lepus API on Docker

Dockerized Lepus Score Server


## Requirements

Docker + Docker Compose


### Linux

* `curl -sSL https://get.docker.com/ | sh`
* See https://docs.docker.com/compose/install/ or `pip install -U docker-compose`


### Mac

Use [Docker Toolbox](https://www.docker.com/toolbox)


## Quick Start

* `git clone https://github.com/lepus-ctf/lepus-api-docker.git`
* `cd lepus-api-docker`
* `docker-compose up` or `docker-compose -d up` for daemonize.
* Open `http://hostname:8000/api/` for testing.


### for The First Time Only

* `docker-compose run api python manage.py migrate` to create tables.
* `docker-compose run api python manage.py createsuperuser` to create superuser.
