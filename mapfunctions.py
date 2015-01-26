import os
import csv
import Tkinter as Tk
import tkFileDialog
import copy
import re
import pandas as pd
import math
import numpy as np
import re
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import mpl_toolkits.basemap.pyproj as pyproj
#matplotlib.use('TkAgg')
import matplotlib

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
# implement the default mpl key bindings
from matplotlib.backend_bases import key_press_handler
"""

def mapdraw(floorFilter,nycrez):
	f = self.mapcode(floorFilter,nycrez)

	canvas = FigureCanvasTkAgg(f, master=self)
	canvas.show()
	canvas.get_tk_widget().grid(column=0,row=1,columnspan=2,sticky='EW')
"""
def datacreate():

	dtypedict = {13: str, 14: str, 15: str, 16: str, 17: str, 18: str, 19: str, 20: str, 61: str, 62: str, 74: str, 77: str}

	bx = pd.read_csv('bx.csv', dtype=dtypedict)
	bk = pd.read_csv('bk.csv', dtype=dtypedict)
	mn = pd.read_csv('mn.csv', dtype=dtypedict)
	qn = pd.read_csv('qn.csv', dtype=dtypedict)
	si = pd.read_csv('si.csv', dtype=dtypedict)
	nyc = pd.concat([bx,bk,mn,qn,si], ignore_index=True)

	"""
	for i in np.arange(0, len(nyc)):
	    nyc['ZoneDist1'][i] = str(nyc['ZoneDist1'][i])
	    nyc['ZoneDist2'][i] = str(nyc['ZoneDist2'][i])
	    nyc['ZoneDist3'][i] = str(nyc['ZoneDist3'][i])
	    nyc['ZoneDist4'][i] = str(nyc['ZoneDist4'][i])
	"""

	nycrez = nyc[((nyc['ZoneDist1'].str[:1] == 'R') | (nyc['ZoneDist2'].str[:1] == 'R') | 
	             (nyc['ZoneDist2'].str[:1] == 'R') |  (nyc['ZoneDist2'].str[:1] == 'R') | 
	             (nyc['ZoneDist1'].str.contains('/R')) | (nyc['ZoneDist2'].str.contains('/R')) |
	             (nyc['ZoneDist3'].str.contains('/R')) | (nyc['ZoneDist4'].str.contains('/R'))) &
	             (nyc['XCoord'].notnull())]

	nycrez = nycrez[['Borough', 'Block', 'Lot', 'CD', 'CT2010', 'CB2010',
	                 'Council', 'BldgArea', 'ResArea', 'ResidFAR', 'CommFAR', 
	                 'FacilFAR', 'BuiltFAR', 'LotArea', 'XCoord', 'YCoord', 'LandUse',
	                 'OwnerName', 'OwnerType', 'Address']]

	nycrez['LeftoverResidFAR'] = nycrez['ResidFAR'] - nycrez['BuiltFAR']
	nycrez['XCoordMeters'] = nycrez['XCoord'] * 0.3048
	nycrez['YCoordMeters'] = nycrez['YCoord'] * 0.3048         

	nycrez = nycrez[(nycrez['LeftoverResidFAR'] > 0)]

	nyli = pyproj.Proj("+proj=lcc +lat_1=40.66666666666666 +lat_2=41.03333333333333 +lat_0=40.16666666666666 +lon_0=-74 +x_0=300000 +y_0=0 +ellps=GRS80 +datum=NAD83 +to_meter=0.3048006096012192 +no_defs")
	wgs84 = pyproj.Proj("+proj=longlat +ellps=GRS80 +datum=NAD83 +no_defs")

	nycrez['Lon'], nycrez['Lat'] = pyproj.transform(nyli, wgs84, nycrez['XCoordMeters'].values, nycrez['YCoordMeters'].values)

	nycrez = nycrez.reset_index(drop=True)	

	return nycrez

"""

def mapcode(FARfilter,nycrez):

	

	fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(12, 10))
	fig.subplots_adjust(hspace=0.05, wspace=0.05)

	ax= axes

	lllat=40.481
	urlat=40.899
	lllon=-74.323
	urlon=-73.716

	m = Basemap(projection='stere',
	                lon_0=(urlon + lllon) / 2,
	                lat_0=(urlat + lllat) / 2,
	                llcrnrlat=lllat, urcrnrlat=urlat,
	                llcrnrlon=lllon, urcrnrlon=urlon,
	                resolution='f')
	m.drawcoastlines()
	m.drawstates()
	m.drawcountries()

	x, y = m(nycrez['Lon'][nycrez['LeftoverResidFAR'] > FARfilter].values, nycrez['Lat'][nycrez['LeftoverResidFAR'] > FARfilter].values)
    
	m.plot(x, y, 'k.', alpha=0.5)
	ax.set_title('Title')

	return fig

	"""