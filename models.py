from  peewee import *
db=SqliteDatabase("/Users/waltersanchez/PycharmProjects/sampler/products.db")
class Product(Model):
      name =CharField()
      quantity= IntegerField()
      price = IntegerField()
      class Meta:
          database=db
