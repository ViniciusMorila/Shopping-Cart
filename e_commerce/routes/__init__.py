from flask import Blueprint

from .products import products
from .auth import auth
from .cart import cart
from .checkout import checkout

routes = Blueprint("routes", __name__)

routes.register_blueprint(products)
routes.register_blueprint(auth)
routes.register_blueprint(cart)
routes.register_blueprint(checkout)
