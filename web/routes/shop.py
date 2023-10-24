from flask import Blueprint, render_template, request, redirect, send_from_directory

from web.models import ShopItems, session
from web.utils import login_required, dotenv_values

shop_bp = Blueprint("shop", __name__)


@shop_bp.route("/uploads/<path:filename>")
def uploaded_file(filename):
    return send_from_directory("uploads", filename)


@shop_bp.route("/admin/shop")
@login_required
def admin_shop():
    all_shop_items = session.query(ShopItems).all()
    return render_template("admin/shop.html", items=all_shop_items)


@shop_bp.route("/admin/shop/create-item", methods=["GET"])
@login_required
def admin_shop_create():
    return render_template("admin/create-item.html")


@shop_bp.route("/admin/shop/create-item", methods=["POST"])
@login_required
def admin_shop_create_post():
    name = request.form.get("name", None)
    price = request.form.get("price", None)
    quantity = request.form.get("quantity", None)
    photo = request.files.get("photo", None)
    if name is None or price is None or quantity is None or photo is None:
        return redirect("/admin/shop/create-item")
    image = request.files["photo"]
    image.save("uploads/" + image.filename)
    try:
        price, quantity = int(price), int(quantity)
    except:
        return redirect("/admin/shop/create-item")

    if price < 0 or quantity < 0:
        return redirect("/admin/shop/create-item")

    item = ShopItems(
        name=name, price=int(price), quantity=int(quantity), image_url=image.filename
    )
    session.add(item)
    session.commit()

    return redirect("/admin/shop")


@shop_bp.route("/admin/shop/edit-item", methods=["GET"])
@login_required
def admin_shop_edit():
    item_id = request.args.get("item_id", None)
    if item_id is None or not item_id.isdigit():
        return redirect("/admin/shop")
    item = session.get(ShopItems, item_id)
    if item is None:
        return redirect("/admin/shop")
    return render_template("admin/edit-item.html", item=item)


@shop_bp.route("/admin/shop/delete-item")
@login_required
def admin_shop_delete_post():
    item_id = request.args.get("item_id", None)
    item = session.get(ShopItems, item_id)
    session.delete(item)
    session.commit()
    return redirect("/admin/shop")


@shop_bp.route("/admin/shop/edit-item", methods=["POST"])
@login_required
def admin_shop_edit_post():
    item_id = request.args.get("item_id", None)
    name = request.form.get("name", None)
    price = request.form.get("price", None)
    quantity = request.form.get("quantity", None)
    photo = request.files.get("photo", None)
    if name is None or price is None or quantity is None:
        return redirect(f"/admin/shop/edit-item?item_id={item_id}")
    if photo:
        image = request.files["photo"]
        image.save("uploads/" + image.filename)
    try:
        price, quantity = int(price), int(quantity)
    except:
        return redirect(f"/admin/shop/edit-item?item_id={item_id}")

    if price < 0 or quantity < 0:
        return redirect(f"/admin/shop/edit-item?item_id={item_id}")

    item = session.get(ShopItems, item_id)
    item.price = price
    item.quantity = quantity
    item.name = name
    if photo:
        item.image_url = image.filename
    session.add(item)
    session.commit()

    return redirect("/admin/shop")
