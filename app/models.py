from app import db
from mapfunctions import datacreate
import pandas as pd
import numpy as np
import mpl_toolkits.basemap.pyproj as pyproj
#matplotlib.use('TkAgg')
import matplotlib



class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	nickname = db.Column(db.String(64), index=True, unique=True)
	email = db.Column(db.String(120), index=True, unique=True)
	posts = db.relationship('Post', backref='author', lazy='dynamic')

	def __repr__(self):
		return '<User %r>' % (self.nickname)
