import os
import os.path
import time
import argparse

import redis


HOST = 'localhost'
PORT = 6379


def wait_redis(host=HOST, port=PORT, timeout=None):
    # Connect to redis and wait until it's ready
    client = redis.StrictRedis(host=host, port=port)
    start_time = time.time()
    while timeout is None or time.time() - start_time < timeout:
        try:
            client.dbsize()
        except redis.BusyLoadingError:
            time.sleep(0.1)
        else:
            break


def main():
    # Parse command line
    parser = argparse.ArgumentParser(description='Wait until redis has '
            'finished loading the dataset, then run another program',
            formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--port', '-p', default=PORT, type=int,
            help='redis port')
    parser.add_argument('--host', '-H', default=HOST, help='redis host')
    parser.add_argument('--timeout', '-t', help='timeout before giving up; '
            'the default is to wait forever')
    parser.add_argument('command', help='the command to run')
    parser.add_argument('args', nargs=argparse.REMAINDER, 
            help='the command arguments')
    options = parser.parse_args()

    wait_redis(options.host, options.port, options.timeout)

    # Start command, replacing the current process
    args = [options.command] + options.args
    os.execvp(options.command, args)
