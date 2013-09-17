waitredis
=========

This is a simple wrapper script that starts a command once redis has finished
loading its dataset in memory.

Installation::

    $ pip install waitredis

Sample usage::

    $ sudo restart redis-server && waitredis redis-cli time
    redis-server start/running, process 20573
    1) "1379426556"
    2) "512325"

Without the wrapper script (and if redis takes a significant amount of time to
load its dataset from disk), you get an error::

    $ sudo restart redis-server && redis-cli time
    redis-server start/running, process 20504
    (error) LOADING Redis is loading the dataset in memory
    
