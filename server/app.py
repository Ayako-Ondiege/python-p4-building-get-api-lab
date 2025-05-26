#!/usr/bin/env python3

from flask import Flask, jsonify
from flask_migrate import Migrate
from models import db, Bakery, BakedGood

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
def index():
    return jsonify({"message": "Welcome to the Bakery API!"}), 200

@app.route('/bakeries')
def get_bakeries():
    bakeries = Bakery.query.all()
    return jsonify([
        {"id": b.id, "name": b.name}
        for b in bakeries
    ]), 200

@app.route('/bakeries/<int:id>')
def get_bakery_by_id(id):
    bakery = Bakery.query.get(id)
    if bakery:
        return jsonify({
            "id": bakery.id,
            "name": bakery.name,
        }), 200
    return jsonify({"error": "Bakery not found"}), 404

@app.route('/baked_goods/by_price')
def baked_goods_by_price():
    goods = BakedGood.query.order_by(BakedGood.price.desc()).all()
    return jsonify([
        {"id": g.id, "name": g.name, "price": g.price}
        for g in goods
    ]), 200

@app.route('/baked_goods/most_expensive')
def most_expensive_baked_good():
    good = BakedGood.query.order_by(BakedGood.price.desc()).first()
    if good:
        return jsonify({
            "id": good.id,
            "name": good.name,
            "price": good.price
        }), 200
    return jsonify({"error": "No baked goods found"}), 404

if __name__ == '_main_':
    app.run(port=5555, debug=True)
