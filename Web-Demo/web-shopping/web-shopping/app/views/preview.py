from flask import render_template,request
from app import app
from app.module.product import Product

@app.route('/preview/<product: product_name>')
def preview():
    product = request.args.get('product_name')

    model = {'title':product.prName, 'product': product}


    return render_template('preview.html',model = model)