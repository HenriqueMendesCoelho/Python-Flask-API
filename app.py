import os

from flask import Flask
from flask_restful import Api

from adapters.handlers.error_handling import handler
from controllers.user_controller import user_bp

app = Flask(__name__)
app.register_blueprint(user_bp)
app.register_blueprint(handler)
app.config['SQLALCHEMY_DATABASE_URI'] = '{db}://{u}:{p}@{ur}:{pr}/{n}'.format(
    db='postgresql',
    u='postgres',
    p=os.environ.get('DB_PASS'),
    ur='localhost',
    pr='5432',
    n='python_test'
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config["JSON_SORT_KEYS"] = False

# flask_restful
api = Api(app)


@app.before_first_request
def initiate_database():
    # db.drop_all()
    db.create_all()


@app.route('/health-check', methods=['GET'])
def teste():
    return {'app': 'running'}


if __name__ == '__main__':
    from adapters.sql_alchemy import db
    db.init_app(app)
    app.run(debug=False)
