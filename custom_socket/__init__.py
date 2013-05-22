#!/usr/bin/env python
HOST = '192.168.69.100'
PORT = 6004 #< 0 for kernel choice @todo support for port assignment recognition
PROXY_HOST = None #< None if none, or 'Host'
PROXY_PORT = 8080 #< Ignored if None for above

import logging
logging.basicConfig(format='%(asctime)s %(message)s', level=logging.DEBUG)