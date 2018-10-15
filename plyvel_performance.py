import plyvel
import time
import random
import string
from functools import wraps

def fn_timer(function):
    @wraps(function)
    def function_timer(*args, **kwargs):
        t0 = time.time()
        result = function(*args, **kwargs)
        t1 = time.time()
        print ("Total time running %s: %s seconds" %
                (function.func_name, str(t1-t0))
                )
        return result
    return function_timer

def initialize():
    db = plyvel.DB('/home/jiapeng/leveldb')
    return db

def id_generator(size=8, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def insert(db, key, value):
    db.put(key, value)

# Experiment 1 – performance to write a key-value pair

# The calculated time to write key-value pairs (ms).
# Memory usages for write operation (MB).
#
# Experiment 2 – performance to read value corresponding to a given key
#
# The elapsed time to read value corresponding to a given key per database (ms).
# Memory usages of in-memory databases for read operation (MB).
#
# Experiment 3 – performance to delete key-value pair corresponding to a given key
#
# The elapsed time to delete the data corresponding to a given key per database (ms).
# Memory usages of in-memory databases for delete operation (MB).
#
# Experiment 4 – performance to fetch all the data
#
# The elapsed time to fetch all the data per database (ms).
# Memory usages of in-memory databases to get all the data (MB).