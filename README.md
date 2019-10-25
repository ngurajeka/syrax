# Syrax Log Viewer

Syrax is a simple tool to display your application log.
Currently, syrax is built specifically for json log created by logback (spring boot aplication).

## Dependency

- Python 3
- Flask
- python-dateutil

## How to run

- Preparation, after clone the source code. Create new virtual-environement, and logs folder to store your logs file

```shell script
$ python -m venv env
$ mkdir logs
$ source ./env/bin/activate
```

- Installing all dependencies

```shell script
(env) $ pip install -r requirements.txt 
```

- Run the web server

```shell script
(env) $ export FLASK_APP="main.py"
(env) $ flask run
```

- Open the web browser and navigate to http://localhost:5000 to access Syrax via browser

## Configuration

### Log Directory

Logs directory by default is `logs` relatively to the root folder of the app, if you want to specify to another directory you can change the `LOG_DIR` in main.py

### Development Mode

By default, the web app will be running in production mode.
If you want to set the app in development mode, maybe extending the functionality.
You can set the `FLASK_ENV` to development before running the app.

```shell script
(env) $ export FLASK_ENV="development"
``` 