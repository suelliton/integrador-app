#!/usr/bin/env python
# -*- coding: utf-8 -*-

from my_app import db
 
class Url(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    urltarget = db.Column(db.String(50)) 
 
    def __init__(self, urltarget):
        self.urltarget = urltarget
 
    def __repr__(self):
        return '<Url %d>' % self.id