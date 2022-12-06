# Models go here
import peewee
from peewee import Model, Check

db = peewee.SqliteDatabase("databasebetsy.db")


class BaseModel(Model):

    class Meta:
        database = db

class Tags(BaseModel):
    tagname = peewee.CharField(unique=True)


class User(BaseModel):
    first_name = peewee.CharField()
    last_name = peewee.CharField()
    street = peewee.CharField()
    house_number = peewee.IntegerField(constraints= [Check('house_number< 100000')])
    zip = peewee.CharField()
    city = peewee.CharField()


class Products(BaseModel):
    name = peewee.CharField(index=True)
    description = peewee.CharField()
    price_p_u = peewee.DecimalField()
    quantity = peewee.IntegerField()


class User_products(BaseModel):
    seller = peewee.ForeignKeyField(User, backref= 'products_seller')
    product = peewee.ForeignKeyField(Products, backref= "sellers_for_product")

    
class Products_tags(BaseModel):
    product =  peewee.ForeignKeyField(Products, backref= 'products_per_tag')
    tag = peewee.ForeignKeyField(Tags, backref= 'tags_per_product')

class Billing(BaseModel):
    user = peewee.ForeignKeyField(User)
    equal_billing_address = peewee.BooleanField()
    street = peewee.CharField(default= User.select(User.street))
    house_number = peewee.IntegerField(default= User.select(User.house_number))
    zip = peewee.CharField(default= User.select(User.zip))
    city = peewee.CharField(default= User.select(User.city))



class Transaction(BaseModel):
    buyer = peewee.ForeignKeyField(User, backref= 'buyer_transactions')
    purchased_product = peewee.ForeignKeyField(Products, backref= 'buyers_product')
    quantity = peewee.IntegerField()


