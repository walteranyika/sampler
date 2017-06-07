from  peewee import *

from os import path
ROOT = path.dirname(path.realpath(__file__))
db = SqliteDatabase(path.join(ROOT, "products.db"))

class Product(Model):
      name =CharField()
      quantity= IntegerField()
      price = IntegerField()
      class Meta:
          database=db

#print(str(ROOT))