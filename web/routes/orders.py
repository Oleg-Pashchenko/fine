from flask import render_template, Blueprint

from web.utils import login_required

orders_bp = Blueprint("orders", __name__)


@orders_bp.route("/admin/orders")
@login_required
def admin_orders():
    return render_template("admin/orders.html")
