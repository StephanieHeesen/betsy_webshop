# Models go here
import peewee
from peewee import Model

db = peewee.SqliteDatabase("databasebetsy.db")
class BaseModel(Model):

    class Meta:
        database = db


class User(BaseModel):
    first_name = peewee.CharField()
    last_name = peewee.CharField()
    street = peewee.CharField()
    house_number = peewee.IntegerField()
    zip = ...
    city = peewee.CharField()
    

class Billing(BaseModel):
    user = peewee.ForeignKeyField(User)
    iban_name = peewee.CharField()
    iban_number = peewee.CharField()


class Producttags(BaseModel):
    tagname = peewee.CharField()


class Products(BaseModel):
    name = peewee.CharField()
    description = peewee.CharField()
    price_p_u = peewee.DecimalField()
    quantity = peewee.IntegerField()
    tags = peewee.ManyToManyField(Producttags)

class Transaction(BaseModel):
    username = peewee.ForeignKeyField(User, backref= 'user_transactions')
    purchased_product = peewee.ForeignKeyField(Products)
    quantity_total = peewee.IntegerField()


ProductTags = Products.tags.get_through_model()