# -*- coding: utf-8 -*-

"""
stathat-async

A simple multithreaded async wrapper around Kenneth Reitz's stathat.py

Usage:

    >>> from stathatasync import StatHat
    >>> stats = StatHat('email@example.com')
    >>> stats.count('wtfs/minute', 10)
    >>> stats.value('connections.active', 85092)

The calls to count and value won't block your program while the HTTP
request to the StatHat API is made. Instead, the requests will be made in a
separate thread.

Enjoy!

"""

import requests
from queue import Queue
from threading import Thread

STATHAT_API="http://api.stathat.com/ez"


def worker(email, session, queue):

    while True:
        command, key, value = queue.get()
        if command == 'value':
            session.post(url=STATHAT_API, data={
                "ezkey": email,
                "stat": key,
                "value": value
            })
        if command == 'count':
            session.post(url=STATHAT_API, data={
                "ezkey": email,
                "stat": key,
                "count": value
            })
        queue.task_done()


class StatHat(object):

    def __init__(self, email):
        session = requests.session()
        self.queue = Queue()
        thread = Thread(target=worker, args=(email, session, self.queue))
        thread.daemon = True
        thread.start()

    def value(self, key, value):
        self.queue.put(('value', key, value))

    def count(self, key, count):
        self.queue.put(('count', key, count))
