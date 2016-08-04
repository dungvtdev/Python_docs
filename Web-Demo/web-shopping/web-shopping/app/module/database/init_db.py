from app.module.database.db_connection import get_db
from app import app
from app.module.database.list_product_demo import product,image
from app.module.database import db_image_product,db_product
from app.module.image import Image
from app.module.product import Product

# function create tables for app
def init_db():
    db = get_db()
    with app.open_resource('module/database/schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()

def create_db():
 #   with app.test_request_context():
    with app.app_context():
        init_db()
        print("database created")

        # add list image of product into table product_image
        img_service = db_image_product.Image_Service()
        for img in image:
            print(img['product_name'],' ', img['img_name'],'   ', img['isMain'],'  ', img['isBig'])
            imgObj = Image(img['product_name'],img['img_name'],img['isMain'],img['isBig'])
            #print(img['product_name'],' ',img['img_name'],'   ',img['isMain'],'  ',img['isBig'])
            img_service.add_image(imgObj)

        #add list product into table prodcut
        product_service = db_product.Product_Service()
        for pro in product:
            productObj = Product(pro['name'],pro['type'],pro['description'],pro['color']
                                 ,pro['price'],pro['sale'],pro['bought'],pro['timeup'])
            product_service.add_product(productObj)