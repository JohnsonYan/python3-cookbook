#!/usr/bin/env python
# encoding: utf-8

from multiprocessing.connection import Client


c = Client(('localhost', 25000), authkey=b'peekaboo')
c.send('hello')
print(c.recv())

c.send(42)
print(c.recv())

c.send([i for i in range(5)])
print(c.recv())
