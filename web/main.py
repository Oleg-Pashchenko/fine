import random
from datetime import timedelta

from flask import Flask, render_template, redirect, url_for, flash, session, request, send_from_directory

import os
import dotenv

current_dir = os.getcwd()
parent_dir = os.path.dirname(current_dir)
dotenv.load_dotenv(dotenv_path=parent_dir)
dotenv_values = dotenv.dotenv_values()
dotenv.load_dotenv()

app = Flask(__name__)
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=60)
app.secret_key = dotenv_values['FLASK_SECRET_KEY']

from functools import wraps
from flask import session as s, redirect, url_for
from models import *


def login_required(view_func):
    @wraps(view_func)
    def decorated_view(*args, **kwargs):
        if s.get('authenticated', False):
            return view_func(*args, **kwargs)
        else:
            return redirect('/admin')

    return decorated_view


@app.route('/uploads/<path:filename>')
def uploaded_file(filename):
    return send_from_directory('uploads', filename)


@app.route('/admin', methods=['GET'])
def admin_login():
    return render_template('admin/auth.html')


@app.route('/admin', methods=["POST"])
def admin_login_post():
    passphrase = request.form.get('passphrase', None)
    if passphrase is None:
        return redirect('/admin')
    if passphrase != dotenv_values['ADMIN_SITE_PASSWORD']:
        return redirect('/admin')
    s['authenticated'] = True
    return redirect('/admin/dashboard')


@app.route('/admin/dashboard')
@login_required
def admin_dashboard():
    return render_template('admin/dashboard.html')


@app.route('/admin/shop')
@login_required
def admin_shop():
    all_shop_items = session.query(ShopItems).all()
    return render_template('admin/shop.html', items=all_shop_items)


@app.route('/admin/shop/create-item', methods=['GET'])
@login_required
def admin_shop_create():
    return render_template('admin/create-item.html')


@app.route('/admin/shop/create-item', methods=['POST'])
@login_required
def admin_shop_create_post():
    name = request.form.get('name', None)
    price = request.form.get('price', None)
    quantity = request.form.get('quantity', None)
    photo = request.files.get('photo', None)
    if name is None or price is None or quantity is None or photo is None:
        return redirect('/admin/shop/create-item')
    image = request.files['photo']
    image.save('uploads/' + image.filename)
    try:
        item = ShopItems(name=name, price=int(price), quantity=int(quantity), image_url=image.filename)
        session.add(item)
        session.commit()
    except:
        return redirect('/admin/shop/create-item')

    return redirect('/admin/shop')


@app.route('/admin/shop/edit-item')
@login_required
def admin_shop_edit():
    item_id = request.args.get('item_id', None)
    if item_id is None:
        return redirect('/admin/shop')

    return render_template('admin/shop.html')


@app.route('/admin/orders')
@login_required
def admin_orders():
    return render_template('admin/orders.html')


@app.route('/admin/users')
@login_required
def admin_users():
    return render_template('admin/users.html')


@app.route('/admin/events')
@login_required
def admin_events():
    return render_template('admin/events.html')


@app.route('/admin/quizes')
@login_required
def admin_quizes():
    return render_template('admin/quizes.html')


if __name__ == '__main__':
    app.run(port=8000, debug=True)
