import os
import os.path
import time
import argparse

import redis


def main():
    # Parse command line
    parser = argparse.ArgumentParser(description='Wait until redis has '
            'finished loading the dataset, then run another program',
            formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--port', '-p', default=6379, type=int, 
            help='redis port')
    parser.add_argument('--host', '-H', default='localhost', help='redis host')
    parser.add_argument('--timeout', '-t', help='timeout before giving up; '
            'the default is to wait forever')
    parser.add_argument('command', help='the command to run')
    parser.add_argument('args', nargs=argparse.REMAINDER, 
            help='the command arguments')
    options = parser.parse_args()

    # Connect to redis and wait until it's ready
    client = redis.StrictRedis(host=options.host, port=options.port)
    start_time = time.time()
    while (options.timeout is None or 
            time.time() - start_time < options.timeout):
        try:
            client.time()
        except redis.ResponseError as exc:
            if exc.args[0].startswith('LOADING'):
                time.sleep(0.1)
            else:
                raise
        else:
            break

    # Start command, replacing the current process
    args = [options.command] + options.args
    os.execvp(options.command, args)
