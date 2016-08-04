from app import app
from flask import render_template
from app.module.database.db_product import Product_Service
from app.module.database.db_image_product import Image_Service
from app.module.product import Product

@app.route('/')
@app.route('/index')
def index():
    product_service = Product_Service()
    img_service = Image_Service()

    list_hot_product_receiver = product_service.get_hot_product()
    list_hot_product = []
    for hot_product in list_hot_product_receiver:
        rows_img = img_service.get_main_image(hot_product['product_name'])
        img_main = ''
        for row_img in rows_img:
            img_main = row_img['img_name']
        product = Product(hot_product['product_name'],hot_product['product_type'],hot_product['product_description'],
                          hot_product['product_color'],hot_product['product_price'],hot_product['product_sale'],
                          hot_product['product_bought'],hot_product['product_time_up'])
        model_hot_product = {}
        model_hot_product['product'] = product
        model_hot_product['img_main'] = img_main
        list_hot_product.append(model_hot_product)
        print(model_hot_product['product'].prName)


    list_new_product_receiver = product_service.get_new_product()
    list_new_product = []
    for new_product in list_new_product_receiver:
        rows_img = img_service.get_main_image(new_product['product_name'])
        img_main = ''
        for row_img in rows_img:
            img_main = row_img['img_name']
        model_new_product = {}
        model_new_product['product'] = new_product
        model_new_product['img_main'] = img_main
        list_new_product.append(model_new_product)

    list_fea_product_receiver = product_service.get_feature_product()
    list_fea_product = []
    for fea_product in list_fea_product_receiver:
        rows_img = img_service.get_main_image(fea_product['product_name'])
        img_main = ''
        for row_img in rows_img:
            img_main = row_img['img_name']
        model_fea_product = {}
        model_fea_product['product'] = fea_product
        model_fea_product['img_main'] = img_main
        list_fea_product.append(model_fea_product)

    return render_template('index.html',new_product = list_new_product, h_products = list_hot_product,fea_product = fea_product)