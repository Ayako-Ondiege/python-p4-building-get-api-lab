#!/usr/bin/env python3

from random import choice as rc
from app import app
from models import db, Bakery, BakedGood

with app.app_context():
    # Clear existing data
    BakedGood.query.delete()
    Bakery.query.delete()
    
    # Create bakery records
    bakeries = [
        Bakery(name='Delightful donuts'),
        Bakery(name='Incredible crullers')
    ]
    db.session.add_all(bakeries)

    # Create baked good records
    baked_goods = [
        BakedGood(name='Chocolate dipped donut', price=2.75, bakery=bakeries[0]),
        BakedGood(name='Apple-spice filled donut', price=3.50, bakery=bakeries[0]),
        BakedGood(name='Glazed honey cruller', price=3.25, bakery=bakeries[1]),
        BakedGood(name='Chocolate cruller', price=3.40, bakery=bakeries[1])
    ]
    db.session.add_all(baked_goods)

    # Commit to DB
    db.session.commit()
