# Do not modify these lines
__winc_id__ = "d7b474e9b3a54d23bca54879a4f1855b"
__human_name__ = "Betsy Webshop"

# Add your code after this line

from models import User, Product, Tag, Transaction, db
from peewee import fn

# Querying Utilities

def search(term):
    term = term.lower()
    return Product.select().where(
        (fn.Lower(Product.name).contains(term)) | (fn.Lower(Product.description).contains(term))
    )


def list_user_products(user_id):
    return Product.select().where(Product.user == user_id)


def list_products_per_tag(tag_id):
    return Product.select().join(Tag).where(Tag.id == tag_id)


def add_product_to_catalog(user_id, product_data):
    product = Product.create(user=user_id, **product_data)
    return product


def remove_product(product_id):
    Product.delete().where(Product.id == product_id).execute()


def update_stock(product_id, new_quantity):
    Product.update(quantity=new_quantity).where(Product.id == product_id).execute()


def purchase_product(product_id, buyer_id, quantity):
    # Assuming the existence of the necessary records in the database
    Transaction.create(buyer=buyer_id, product=product_id, quantity=quantity)
    update_stock(product_id, Product.get(Product.id == product_id).quantity - quantity)


# Test data utility

def populate_test_database():
    # Create test users
    user1 = User.create(name='Alice', address='123 Main St', billing_info='Credit Card')
    user2 = User.create(name='Bob', address='456 Oak St', billing_info='PayPal')

    # Create test tags
    tag1 = Tag.create(name='Clothing')
    tag2 = Tag.create(name='Electronics')

    # Create test products
    product1 = Product.create(name='Sweater', description='Warm sweater', price=25.99, quantity=10, user=user1)
    product1.tags.add(tag1)

    product2 = Product.create(name='Smartphone', description='High-end smartphone', price=499.99, quantity=5, user=user2)
    product2.tags.add(tag2)

    # Create a test transaction
    Transaction.create(buyer=user2, product=product1, quantity=2)


if __name__ == "__main__":
    # Uncomment the line below to populate the test database
    # populate_test_database()

    # Your testing or querying code can go here
    pass

