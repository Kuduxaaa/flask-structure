# -*- coding: utf-8 -*-
# Coded By Kuduxaaa

from app import db


"""
Example users model
"""
class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    username = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(32), nullable=False)

    def __init__(self, username, email, password, balance):
        self.username = username
        self.password = password
        self.email = email
        

    def save(self):
        """
        save in the database
        """

        db.session.add(self)
        db.session.commit()
        return True


    def delete(self):
        """
        delete from database
        """

        db.session.delete(self)
        db.session.commit()
        return True

    def __repr__(self):
        return '<User %r>' % self.username
