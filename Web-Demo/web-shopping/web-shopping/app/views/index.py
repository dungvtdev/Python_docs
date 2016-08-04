from app import app
from flask import render_template
from app.module.database.db_product import Product_Service

@app.route('/')
@app.route('/index')
def index():
    product_service = Product_Service()
    hot_product = product_service.get_hot_product()
    new_product = product_service.get_new_product()
    return render_template('index.html',fea_product = new_product, h_product = hot_product)