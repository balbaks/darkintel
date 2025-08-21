from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail

db = SQLAlchemy()
migrate = Migrate()
mail = Mail()

def create_app():
    # 🔧 Initialize Flask with branded template/static folders
    app = Flask(
        __name__,
        template_folder='../templates',
        static_folder='../static'
    )

    # 🧬 Load configuration (can be extended to config.py or env vars)
    app.config.from_pyfile('../config.py', silent=True)

    # 🧱 Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    mail.init_app(app)

    # 🚀 Register branded routes
    from .routes import register_routes
    register_routes(app)

    # 🧬 Serve branded index.html directly
    @app.route('/')
    def home():
        return render_template('index.html')

    # 🧪 Optional: Health check route
    @app.route('/ping')
    def ping():
        return 'pong', 200

    return app
