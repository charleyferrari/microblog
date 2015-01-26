from app import db
from mapfunctions import datacreate
import pandas as pd
import numpy as np
import mpl_toolkits.basemap.pyproj as pyproj
#matplotlib.use('TkAgg')
import matplotlib
import sqlite3

nycrez = datacreate()

con = sqlite3.connect('app.db')
con.execute('DROP TABLE IF EXISTS nycrez')
pd.io.sql.write_frame(nycrez, 'nycrez', con)

"""DB READ TEST 

con = sqlite3.connect('app.db')
df = pd.read_sql('SELECT * FROM nycrez LIMIT 3', con)

"""
