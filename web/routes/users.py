from flask import render_template, Blueprint

from web.utils import login_required

users_bp = Blueprint("users", __name__)


@users_bp.route("/admin/users")
@login_required
def admin_users():
    return render_template("admin/users.html")
