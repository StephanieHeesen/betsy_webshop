from models import (db, User, Billing, Products_tags, Products, Transaction, Tags, User_products)
import os

def delete_database():
    cwd = os.getcwd()
    database_path = os.path.join(cwd, 'databasebetsy.db')
    if os.path.exists(database_path):
        os.remove(database_path)

def populate_test_data():
    db.connect()

    db.create_tables([
        User, Billing, Products_tags,
        Products, Transaction, Tags, User_products
    ])

    # Table User
    users = [
        ['Piet','Hoogte', 'Elsenlaan', 34, '3011ZB', 'Utrecht'], 
        ['Mike', 'Draven', 'van Grootstraat', 198, '1088HH', 'Amsterdam'],
        ]

    for user in users:
        User.create(first_name = user[0], last_name = user[1], street = user[2], house_number = user[3],
        zip = user[4], city = user[5])


    # Table Products    
    products = [
        ['gebreide trui', 'gebreide trui van fijn wol rood van kleur', 129.99, 8 ],
        ['shirt met print', 'wit shirt met korte mouwen met een leuke disney print', 24.99, 20 ]
    ]

    for product in products:
        Products.create(name = product[0], description = product[1], price_p_u = product[2], quantity = product[3])
    

    # Table Tags
    producttags = [
        'trui', 'rood', 'winter', 'shirt', 'wit', 'zomer'
    ]

    for producttag in producttags:
        Tags.create(tagname = producttag)


    # Table Products_tags
    tagsproducts = [
        [ 1, 1], [1, 2], [1, 3], [2, 4],[2, 5], [2, 6]
    ]

    for producttag in tagsproducts:
        Products_tags.create(product = producttag[0], tag = producttag[1])

    
    # Table Billing
    billing = [
        [1, False, 'Kastanjelaan', 55, '3088HG', 'Utrecht']
    ]

    for bill in billing:
        Billing.create(user = bill[0], equal_billing_address = bill[1], street = bill[2], 
        house_number= bill[3], zip= bill[4], city= bill[5] )

    
print(delete_database())
print(populate_test_data())