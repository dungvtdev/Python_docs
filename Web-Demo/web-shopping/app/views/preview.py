from flask import render_template,request
from app import app
from app.module.product import Product
from app.module.database.db_connection import get_db

@app.route('/preview/')
def preview():
    product = request.args.get('product_name')
    db_connect = get_db()

    model = {'title':product.prName, 'product': product}


    return render_template('preview.html',model = model)