from datetime import timedelta
from flask import Flask, render_template
from web.routes.main import main_bp
from web.routes.shop import shop_bp
from web.routes.users import users_bp
from web.routes.orders import orders_bp
from web.routes.events import events_bp
from web.routes.quizes import quizes_bp
from web.utils import login_required
from models import *

app = Flask(__name__)
app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(minutes=60)
app.secret_key = dotenv_values["FLASK_SECRET_KEY"]

app.register_blueprint(main_bp, url_prefix="/")
app.register_blueprint(shop_bp, url_prefix="/")
app.register_blueprint(orders_bp, url_prefix="/")
app.register_blueprint(users_bp, url_prefix="/")
app.register_blueprint(events_bp, url_prefix="/")
app.register_blueprint(quizes_bp, url_prefix="/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8081, debug=True)
