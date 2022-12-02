__winc_id__ = "d7b474e9b3a54d23bca54879a4f1855b"
__human_name__ = "Betsy Webshop"

import models
from models import (db, User, Billing, Tags, Products, Transaction, Products_tags) 
    


def search(term):
    query = Products.select().where(Products.name.contains(term)|Products.description.contains(term))
    for product in query:
        return(product.name)


def list_user_products(user_id):
    query = Products.select(Products, User).join(User).where(User.id == user_id)
    return [product.name for product in query]


def list_products_per_tag(tag_id):
    query = Products_tags.select(Products_tags, Products).join(Products).where(Products_tags.tag == tag_id)
    return [product_with_tag.product.name for product_with_tag in query]


def add_product_to_catalog(user_id, product):
    Products.create(seller= user_id, name= product)
    #????


def update_stock(product_id, new_quantity):
    Products.update(quantity= new_quantity).where(Products.id == product_id).execute()
    
    print([product.quantity for product in Products.select()])


def purchase_product(product_id, buyer_id, quantity):
    Transaction.create(buyer= buyer_id, purchased_product= product_id, quantity= quantity)
    # Products.update(quantity= )


def remove_product(product_id):
    ...


def main():
    db.connect()
    print('connected')

    print(search('Rood'))
    print(list_user_products(1))
    print(list_products_per_tag(3))

    print(update_stock(1, 6))
    


    db.close()
    print('closed')

if __name__ == "__main__":
    main()