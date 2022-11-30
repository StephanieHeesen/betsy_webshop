from models import (db, User, Billing, Producttags, Products, Transaction, ProductTags)
import os

def delete_database():
    cwd = os.getcwd()
    database_path = os.path.join(cwd, 'databasebetsy.db')
    if os.path.exists(database_path):
        os.remove(database_path)

def populate_test_data():
    db.connect()

    db.create_tables([
        User, Billing, Producttags,
        Products, Transaction, ProductTags
    ])
    users = [
        ['Piet','Hoogte', 'Elsenlaan', 34, 'Utrecht'], 
        ['Mike', 'Draven', 'van Grootstraat', 198, 'Amsterdam'],
        ]
    
    products = [
        ['gebreide trui', 'gebreide trui van fijn wol rood van kleur', 129.99, 8 ],
        ['shirt met print', 'wit shirt met korte mouwen met een leuke disney print', 24.99, 20 ]
    ]
    gebreide_trui = ['trui','rood','winter']
    shirt_met_print = ['shirt', 'wit', 'zomer']
    
    
    producttags = [
        'trui', 'rood', 'winter', 'shirt', 'wit', 'zomer'
    ]


    for user in users:
        User.create(first_name = user[0], last_name = user[1], street = user[2], house_number = user[3], city = user[4])

    for producttag in producttags:
        Producttags.create(tagname = producttag)

    for product in products:
        Products.create(name = product[0], description = product[1], price_p_u = product[2], quantity = product[3])
    
print(delete_database())
print(populate_test_data())