# Models go here

from peewee import Model, SqliteDatabase, ForeignKeyField, CharField, DecimalField, IntegerField

db = SqliteDatabase('betsy-webshop/betsy.db')


class BaseModel(Model):
    class Meta:
        database = db


class User(BaseModel):
    name = CharField(max_length=255)
    address = CharField(max_length=255)
    billing_info = CharField(max_length=255)

class Tag(BaseModel):
    name = CharField(unique=True)


class Product(BaseModel):
    name = CharField(max_length=255)
    description = CharField(max_length=1000)
    price = DecimalField(max_digits=10, decimal_places=2)
    quantity = IntegerField()
    user = ForeignKeyField(User, backref='products')
    tag1 = ForeignKeyField(Tag, backref='product1', null=True)
    tag2 = ForeignKeyField(Tag, backref='product2', null=True)


class Transaction(BaseModel):
    buyer = ForeignKeyField(User, backref='transactions')
    product = ForeignKeyField(Product, backref='transactions')
    quantity = IntegerField()


def initialize_db():
    db.connect()
    db.create_tables([User, Product, Tag, Transaction])


# Initialize the database
initialize_db()
