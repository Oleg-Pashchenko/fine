from flask import render_template, Blueprint

from web.utils import login_required

quizes_bp = Blueprint("quizes", __name__)


@quizes_bp.route("/admin/quizes")
@login_required
def admin_quizes():
    return render_template("admin/quizes.html")
