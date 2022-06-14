from flask_migrate import Migrate

from verify_ip.ext.db import db
from verify_ip.ext.models.ips import Ips #noqa

migrate = Migrate()

def init_app(app):
    migrate.init_app(app, db)
