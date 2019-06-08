#!/usr/bin/env python3

import socket
import string
from time import sleep
from random import randint
import logging
from logging import handlers
import argparse

slen = string.ascii_letters.__len__()

def randstr(mlen):

    out = ''
    for n in range(0,randint(3,mlen)):
        out += string.ascii_letters[randint(0,slen-1)]

    return out

if __name__ == '__main__':

    parser = argparse.ArgumentParser('Send logs to a syslog server')

    parser.add_argument('--host',
        required=True,
        help='''Host to send the logs.''')
    parser.add_argument('--port',
        default=514,
        help='''Port to send the logs.''')

    args = parser.parse_args()

    # ===================================
    # INITIALIZE AND CONFIGURE THE LOGGER
    # ===================================

    syslogger = logging.getLogger('syslogger')
    syslogger.setLevel(logging.INFO)
    handler = handlers.SysLogHandler(address=(args.host,args.port))
    syslogger.addHandler(handler)

    template = 'GET DangerZone/username/{}/password/{}'

    print('[+] Beginning log loop')

    try:

        while True:

            record = template.format(randstr(15),randstr(15))
            print(f'- logging: {record}')
            syslogger.info(record)
            sleep(1)

    except KeyboardInterrupt:

        print('\n[+] CTRL+C\n[+] Exiting')


