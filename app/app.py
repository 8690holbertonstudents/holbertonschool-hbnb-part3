import os
from flask import Flask
from flask_migrate import Migrate
from config import db, Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate = Migrate(app, db)

    from api.user_api import user_api
    app.register_blueprint(user_api)

    return app

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app = create_app()
    app.run(debug=True, host="0.0.0.0", port=port)
