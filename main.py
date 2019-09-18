import json
import logging
from dateutil import parser
from flask import Flask, render_template, request
from os import listdir
from os.path import isfile, join


app = Flask(__name__)
logger = logging.getLogger('__main__')

LOG_DIR = 'logs'

def get_files():
    return [f for f in listdir(LOG_DIR) if isfile(join(LOG_DIR, f))]

def read_file_as_json(path):
    f = open(path, "r")
    contents = f.readlines()
    f.close()
    json_data = []
    for content in contents:
        try:
            data = json.loads(content)
            data['timestamp'] = data.pop('@timestamp')
            json_data.append(data)
        except json.decoder.JSONDecodeError as e:
            logger.warning('failed to decode content', e)
    return json_data

def read_files(files):
    json_data = []
    for file in files:
        json_data.extend(read_file_as_json(join(LOG_DIR, file)))
    return json_data

def filter_start_date(x, start):
    start = parser.parse(start + " 00:00:00.000000+07:00")
    v = parser.parse(x['timestamp'])
    return v >= start

def filter_end_date(x, end):
    end = parser.parse(end + " 23:59:59.000000+07:00")
    v = parser.parse(x['timestamp'])
    return v <= end

@app.route('/')
def index():
    level = request.args.get('level', None)
    start = request.args.get('start', None)
    end = request.args.get('end', None)
    msg = request.args.get('message', '')

    logs = read_files(get_files())
    if level and level != 'ALL':
        logs = list(filter(lambda x: x['level'] == level, logs))
    if start:
        logs = list(filter(lambda x: filter_start_date(x, start), logs))
    if end:
        logs = list(filter(lambda x: filter_end_date(x, end), logs))
    if msg != '':
        logs = list(filter(lambda x: msg in x['message'], logs))

    return render_template('index.html', level=level, logs=logs, start=start, end=end, message=msg)


if __name__ == '__main__':
    app.run()
