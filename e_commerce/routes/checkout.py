from flask import Blueprint, jsonify
from flask_login import login_required, current_user
from e_commerce.models import db, User

checkout = Blueprint("checkout", __name__)

@checkout.route("/v1/cart/checkout", methods=["POST"])
@login_required
def process_checkout():
    user = User.query.get(int(current_user.id))
    cart_items = user.cart
    if not cart_items:
        return jsonify({"message": "The cart is already empty"}), 400

    try:
        for cart_item in cart_items:
            db.session.delete(cart_item)
        db.session.commit()
        return jsonify({"message": "Checkout completed successfully"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Error processing checkout", "details": str(e)}), 500
