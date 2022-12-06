__winc_id__ = "d7b474e9b3a54d23bca54879a4f1855b"
__human_name__ = "Betsy Webshop"


from models import (db, User, Billing, Tags, Products, Transaction, Products_tags, User_products) 


def search(term):
    query = Products.select().where(Products.name.contains(term)|Products.description.contains(term))
    for product in query:
        return(product.name)


def list_user_products(user_id):
    query = Products.select(Products, User_products).join(User_products).where(User_products.seller == user_id)
    return [product.name for product in query]


def list_products_per_tag(tag_id):
    query = Products_tags.select(Products_tags, Products).join(Products).where(Products_tags.tag == tag_id)
    return [product_with_tag.product.name for product_with_tag in query]


def add_product_to_catalog(user_id, product):
    id_product = Products.get(name = product)
    User_products.create(seller = user_id, product = id_product.id)

    # To check if the query worked I used this:
    # print([(product.seller, product.product) for product in User_products.select()])
    return "product added to user"


def update_stock(product_id, new_quantity):
    Products.update(quantity= new_quantity).where(Products.id == product_id).execute()
    
    # To check if the query worked I used this:    
    # print([product.quantity for product in Products.select()])
    return "stock updated"


def purchase_product(product_id, buyer_id, quantity):
    Transaction.create(buyer= buyer_id, purchased_product= product_id, quantity= quantity)
    query = Products.select().where(Products.id == product_id)
    for product in query:
        Products.update(quantity= (product.quantity - quantity)).where(Products.id == product_id).execute()

    # To check if the query worked I used this:
    # print([product.quantity for product in Products.select()])
    # for transaction in Transaction.select():
    #     print(transaction.buyer)
    return "product sold"

def remove_product(product_id):
    User_products.delete().where(User_products.product == product_id).execute()

    # To check if the query worked I used this:
    # for product in User_products.select():
    #     print(product.product)

    return "product removed"


def main():
    db.connect()
    print('connected')
    

    print(search('Rood'))
    print(list_user_products(1))
    print(list_products_per_tag(3))
    print(add_product_to_catalog(1, 'shirt met print'))
    print(update_stock(1, 6))
    print(purchase_product(1, 2, 1))
    print(remove_product(2))


    db.close()
    print('closed')

if __name__ == "__main__":
    main()