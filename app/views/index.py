# coding=utf-8

import flask_admin as admin
from flask import url_for
from flask.ext.security import current_user, url_for_security
from flask_admin import expose
from werkzeug.utils import redirect


class AdminIndexView(admin.AdminIndexView):
    @expose('/')
    def index(self):
        if not current_user.is_authenticated:
            return redirect(url_for_security('login'))
        return self.render('dashboard.html')