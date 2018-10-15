import plyvel
import random
import string


def initialize():
    db = plyvel.DB('/home/jiapeng/leveldb', create_if_missing=True)
    return db


def insert(db, random_key, random_value):
    db.put(random_key, random_value)


def id_generator(size=8, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def create_random_data(min, max):
    for num in range(min, max):
        insert(db, bytes(id_generator(), encoding="utf8"), bytes(id_generator(), encoding="utf8"))


db = initialize()

sn = db.snapshot()
print(sn.get(b'S277SGBI'))

# for key, value in db:
#     print(key)
#     print(value)

db.close()
db.closed
