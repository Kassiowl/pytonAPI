from core.domain.entity.product import Product
from core.domain.repositories.save_product import SaveProductDefinition
import sqlite3

class SaveProductImpl(SaveProductDefinition):
    def __init__(self):
        self.con = sqlite3.connect("product.db")
        self.cur = self.con.cursor()
    def create_table(self):
        try:
            self.cur.execute(f"CREATE TABLE products(id PRIMARY KEY, title, price, category)")
        except Exception as e:
            return e
    def save_product(self,product:Product):
        try:
            self.cur.execute(f"""
                INSERT INTO products VALUES('{product.id}', '{product.title}', '{product.price}', '{product.category}')
            """)
            return True
        except Exception as e:
            print(e)
            return False