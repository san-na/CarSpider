#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

from car import db
from datetime import datetime
from flask.ext.sqlalchemy import SQLAlchemy


class Car(db.Model):
    '''汽车表
    '''
    __tablename__ = 'car'

    __now = datetime.now()
    id = db.Column(db.Integer, primary_key=True)
    logo = db.Column(db.String(200),index=True)
    model = db.Column(db.String(200),index=True)
    befor_price = db.Column(db.String(200))
    after_price = db.Column(db.String(200))
    plan = db.Column(db.String(200))
    purchased = db.Column(db.Integer)
    link = db.Column(db.String(100))
    status = db.Column(db.Boolean, default=True)
    created = db.Column(db.DateTime, default=__now)
    updated = db.Column(db.DateTime, default=__now)

    def __init__(self, logo, model, befor_price, after_price,
                    plan, purchased, link):
        self.logo = logo
        self.model = model
        self.befor_price = befor_price
        self.after_price = after_price
        self.plan = plan
        self.purchased = purchased
        self.link = link

    def __repr__(self):
        return '<User %r>' % self.name

    def update(self):
        db.session.commit()

    def save(self):
        db.session.add(self)
        db.session.commit()
