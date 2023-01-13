from flask import Flask
from flask_restful import Api

from resources.user import user_bp

app = Flask(__name__)
app.register_blueprint(user_bp)
app.config['SQLALCHEMY_DATABASE_URI'] = '{db}://{u}:{p}@{ur}:{pr}/{n}'.format(
    db='postgresql',
    u='postgres',
    p='8u3T7&HQ$5o^x##',
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
    db.drop_all()
    db.create_all()


@app.route('/health-check', methods=['GET'])
def teste():
    return {'app': 'running'}


if __name__ == '__main__':
    from sql_alchemy import db
    db.init_app(app)
    app.run(debug=True)
