from verify_ip.ext.routes.main import bp

def init_app(app):
    app.register_blueprint(bp)