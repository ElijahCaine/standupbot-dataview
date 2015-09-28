#!/usr/bin/env python

import requests
import json
import time
from datetime import datetime, date
from flask import Flask, render_template

app = Flask(__name__)
standupbot_url = # url goes here

def sort_by_names(data):
    """
    Sorts StandupBot data into a dict of `name: [{info}, {info}, {...}, ...]`.
    """
    by_names = {}

    for s in data['statuses']:
        # If the name matches the currently sorted name
        name = s['name']
        try:
            by_names[name].append(s)
        except KeyError:
            by_names[name] = []
            by_names[name].append(s)

    return by_names


def convert_datetimes(data):
    """
    Converts iso timestamps into python datetimes.
    """
    for entry in data['statuses']:
        entry['time'] = datetime\
                        .fromtimestamp(entry['time'] / 1e3)\
                        .strftime("%A %m-%d %H:%M")

    return data


def main():
    """
    Main. Deals with initial data processing and retrieval.
    """
    # Make a request to standupbot's historical data page
    r = requests.get(standupbot_url+'/api/historical/')

    # Load the JSON into a dictionary
    d = json.loads(r.text)

    # Convert unixtimestamps into python datetimes
    d = convert_datetimes(d)

    # Sort time entries by user
    s_n = sort_by_names(d)

    # Reverse the array so the most recent entry is the 0th element
    for k in s_n:
        s_n[k].reverse()

    return s_n


@app.route('/')
@app.route('/<name>/')
def root(name=None):
    return render_template('template.jinja', d=main(), name=name)


if __name__ == "__main__":
    app.run()
