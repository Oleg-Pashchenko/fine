from flask import render_template, Blueprint

from web.utils import login_required

events_bp = Blueprint("events", __name__)


@events_bp.route("/admin/events")
@login_required
def admin_events():
    return render_template("admin/events.html")
