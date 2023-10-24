import os
from functools import wraps

import dotenv
from flask import session, redirect


def login_required(view_func):
    @wraps(view_func)
    def decorated_view(*args, **kwargs):
        if session.get("authenticated", False):
            return view_func(*args, **kwargs)
        else:
            return redirect("/admin")

    return decorated_view


current_dir = os.getcwd()
parent_dir = os.path.dirname(current_dir)
dotenv.load_dotenv(dotenv_path=parent_dir)
dotenv_values = dotenv.dotenv_values()
