from app.module.database.db_connection import get_db
from app.module.image import Image

class Image_Service:

    def __init__(self):
        self.db = get_db()
        self.db_cursor = self.db.cursor()

    def add_image(self,image):
        query = """INSERT INTO product_image (product_name, img_name, isMain, isBig)
                VALUES ('{}','{}','{}','{}');""".format(image.img_prduct_name,image.img_name,image.img_isMain,image.img_isBig);


                #('"""+image.img_prduct_name+"""','"""+image.img_name+"""','
                #"""+image.img_isMain+"""','"""+image.img_isBig+"""');""";
        #print (query)
        self.db_cursor.execute(query)
        self.db.commit()

    def get_main_image(self,product_name):
        query = "SELECT img_name FROM product_image WHERE product_name = '"+product_name+"' AND isMain = '1' ;"
        self.db_cursor.execute(query)
        rows = self.db_cursor.fetchall()
        return rows

    def get_image_big(self,product_name):
        query = "SELECT img_name FROM product_image WHERE product_name = '" + product_name + "' AND img_isBig = '1';"
        self.db_cursor.execute(query)
        rows = self.db_cursor.fetchall()
        return rows

    def get_image_small(self, product_name):
        query = "SELECT img_name FROM product_image WHERE product_name = '" + product_name + "' AND img_isBig = '0';"
        self.db_cursor.execute(query)
        rows = self.db_cursor.fetchall()
        return rows
