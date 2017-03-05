# Barcode Scanner with Webserver

## First time setup:

```bash
$ pip3 install virtualenv
$ virtualenv venv
$ source venv/bin/activate
$ pip install pybuilder
$ pyb install_dependencies
$ pyb
```
## Run Flask-Server in dev-mode
    $ export FLASK_DEBUG=1;export FLASK_APP=barcodescan/barcodescanner_server.py;flask run


## Requirements:
- a runnig Redis server unter localhost




## Hints:
###mac os:
redis-server /usr/local/etc/redis.conf

## Links:
https://github.com/jezdez/Flask-RQ2

## rpi distro builder
https://github.com/RPi-Distro/pi-gen

https://en.wikipedia.org/wiki/Code_128