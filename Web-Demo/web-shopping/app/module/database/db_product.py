from app.module.database.db_connection import get_db
from app.module.product import Product

class Product_Service:

    def __init__(self):
        self.db = get_db()
        self.db_cursor = self.db.cursor()

    def get_hot_product(self):
        "hot product selected by the number of products sold"
        query = "SELECT * FROM product ORDER BY product.product_bought LIMIT 3 ; "
        self.db_cursor.execute(query)
        rows = self.db_cursor.fetchall()
        for row in rows:
            print(row['product_name'])
        return rows

    def get_new_product(self):
        query = "SELECT * FROM product WHERE (julianday('now')-julianday(product_time_up)) >= 2 LIMIT 4;"
        self.db_cursor.execute(query)
        rows = self.db_cursor.fetchall()
        return rows

    def get_product_detail(self,name_product):
        query = "SELECT * FROM product WHERE "+name_product+"= product.product_name;"
        self.db_cursor.execute(query)
        rows = self.db_cursor.fetchall()
        return rows

    def get_feature_product(self):
        query = "SELECT * FROM product WHERE julianday('now') > julianday(product_time_up) LIMIT 4;"
        self.db_cursor.execute(query)
        rows = self.db_cursor.fetchall()
        return rows

    def get_image_of_product(self,product_name):
        query = """ SELECT product_image.location, product_image.isLarger, product_image.main
                    FROM product_image, product
                    WHERE product.product_id = product_image.product_id AND product.product_name = '"""+product_name+"""';"""
        self.db_cursor.execute(query)
        rows = self.db_cursor.fetchall()
        return rows
    def add_product(self,product):
        query = """ INSERT INTO product (product_name,product_description,product_type,product_color,
                    product_price,product_sale,product_bought,product_time_up)
                    VALUES ('{}','{}','{}','{}','{}','{}','{}','{}');""".format(product.prName,product.prDescription,
                                                            product.prType,product.prColor,product.prPrice,
                                                            product.prSale,product.prBought,product.prTimeUp)
        print(query)
        self.db_cursor.execute(query)
        self.db.commit()
