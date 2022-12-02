# Models go here
import peewee
from peewee import Model

db = peewee.SqliteDatabase("databasebetsy.db")

def main():
    pass

class BaseModel(Model):

    class Meta:
        database = db

class Tags(BaseModel):
    tagname = peewee.CharField()


class User(BaseModel):
    first_name = peewee.CharField()
    last_name = peewee.CharField()
    street = peewee.CharField()
    house_number = peewee.IntegerField()
    zip = peewee.CharField()
    city = peewee.CharField()

class Products(BaseModel):
    name = peewee.CharField()
    description = peewee.CharField()
    price_p_u = peewee.DecimalField()
    quantity = peewee.IntegerField()
    seller = peewee.ForeignKeyField(User, backref= 'products_seller')
    
class Products_tags(BaseModel):
    product =  peewee.ForeignKeyField(Products, backref= 'products_per_tag')
    tag = peewee.ForeignKeyField(Tags, backref= 'tags_per_product')

class Billing(BaseModel):
    user = peewee.ForeignKeyField(User)
    equal_billing_address = peewee.BooleanField()
    street = peewee.CharField()
    house_number = peewee.IntegerField()
    zip = peewee.CharField()
    city = peewee.CharField()



class Transaction(BaseModel):
    buyer = peewee.ForeignKeyField(User, backref= 'buyer_transactions')
    purchased_product = peewee.ForeignKeyField(Products, backref= 'buyers_product')
    quantity = peewee.IntegerField()


# ProductTags = Products.tags.get_through_model()