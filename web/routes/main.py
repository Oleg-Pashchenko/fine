from flask import Blueprint, render_template, request, redirect, session

from web.utils import login_required, dotenv_values

main_bp = Blueprint("main", __name__)


@main_bp.route("/admin", methods=["GET"])
def admin_login():
    print('yes')
    return render_template("admin/auth.html")


@main_bp.route("/admin", methods=["POST"])
def admin_login_post():
    passphrase = request.form.get("passphrase", None)
    if passphrase is None:
        return redirect("/admin")
    if passphrase != dotenv_values["ADMIN_SITE_PASSWORD"]:
        return redirect("/admin")
    session["authenticated"] = True
    return redirect("/admin/dashboard")


@main_bp.route("/admin/dashboard")
@login_required
def admin_dashboard():
    return render_template("admin/dashboard.html")

