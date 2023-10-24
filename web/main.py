from datetime import timedelta
from flask import Flask, redirect, flash, request
from flask import session
from web.routes.main import main_bp
from web.routes.shop import shop_bp
from web.routes.users import users_bp
from web.routes.orders import orders_bp
from web.routes.events import events_bp
from web.routes.quizes import quizes_bp
from utils import dotenv_values

app = Flask(__name__)
app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(minutes=60)
app.secret_key = dotenv_values["FLASK_SECRET_KEY"]
app.register_blueprint(main_bp, url_prefix="/")
app.register_blueprint(shop_bp, url_prefix="/")
app.register_blueprint(orders_bp, url_prefix="/")
app.register_blueprint(users_bp, url_prefix="/")
app.register_blueprint(events_bp, url_prefix="/")
app.register_blueprint(quizes_bp, url_prefix="/")


@app.errorhandler(404)
def page_not_found(e):
    flash('Страницы не существует! Перенаправил вас в админ панель.', 'warning')
    return redirect('/admin/dashboard')


@app.route('/admin/changetheme')
def change_theme():
    theme = session.get('current_theme', 'white')
    session['current_theme'] = 'black' if theme == 'white' else 'white'

    # Store the referring URL in the session
    session['referring_url'] = request.referrer

    # Redirect to the referring URL
    return redirect(session.get('referring_url', '/admin/dashboard'))


@app.context_processor
def inject_theme():
    current_theme = session.get('current_theme', 'white')
    cur_ses = {'current_theme': current_theme}
    return cur_ses


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8081, debug=True)
