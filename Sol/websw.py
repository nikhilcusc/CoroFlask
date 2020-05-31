from __future__ import print_function
from flask import Flask, render_template, Markup, request, flash, jsonify

from flask_inputs import Inputs
from wtforms import Form, BooleanField, StringField, PasswordField, validators
from wtforms.validators import DataRequired

import pandas as pd
import csv
import urllib2
import sys

rawURL = 'https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv'

app = Flask(__name__)
app.secret_key = 'EcCbAbg7nZ' #haha not so secret!

# validation
class Validation(Form):
    county = StringField('county', [validators.DataRequired()])

@app.route('/_getCounties')
def getCounties():
	stateSelected = request.args.get('state')
	
	#get the rawdata from website
	response = urllib2.urlopen(rawURL)
	cr = csv.reader(response)
	
	countyList= []
	for row in cr:
		#print(row)
		try:
			if row[2]==stateSelected and not (row[1] in countyList):
				countyList.append(row[1])
		except IndexError:
			continue
	
	#result = countyList;
	return jsonify({"countyListNames":countyList})
	

@app.route('/')
def home():
    return render_template('home.html')

'''	
@app.route('/Corochart', methods=['GET'])
def Corochart():
	#CountyNameDD = 'Maricopa'
	#CountyNameDD = request.form.get('county')
	CountyNameDD = request.args.get("counties")
	CountyName = CountyNameDD 
	CountyName.replace(",", "")
	
	return render_template('testDropDown.html',title='testDropDown', countyData=CountyNameDD)
'''

@app.route('/Corochart', methods=['GET'])
def Corochart():
	
	#get county name
	CountyName = request.args.get("counties")
	'''
	Because we are getting names from the list, we don't need validation
	#validate the CountyName here
	validation = Validation(request.form) 
	
	if not validation.validate(): # empty county Name 
		flash('Empty text box')
		return render_template('home.html')
	'''
	#get the rawdata from website
	response = urllib2.urlopen(rawURL)
	cr = csv.reader(response)
	countyData=[]
	for row in cr:
		#row date,county,state,fips,cases,deaths
		if row[1]==CountyName:
			countyData.append(row)
	
	dates=[row[0] for row in countyData]
	cases=[row[4] for row in countyData]
	deaths=[row[5] for row in countyData]
	row = countyData[0]
	
	#Cases daily change
	stackedCases=[0]
	trailingSumStackedCases=[0]
	for ind in range(1,len(countyData)):
		#print(countyData[ind][4], countyData[ind-1][4])
		stackedCases.append( int(countyData[ind][4]) - int(countyData[ind-1][4]))
		trailingSumStackedCases.append(int(countyData[ind-1][4]))

	#Deaths daily change
	stackedDeaths=[0]
	trailingSumStackedDeaths=[0]
	for ind in range(1,len(countyData)):
		#print(countyData[ind][4], countyData[ind-1][4])
		stackedDeaths.append( int(countyData[ind][5]) - int(countyData[ind-1][5]))
		trailingSumStackedDeaths.append(int(countyData[ind-1][5]))


	county = [row[1],row[2]]
	return render_template('Corochart.html',title='Corochart', countyData=county, dates=dates, cases=cases, stackedCases=stackedCases,  trailingSumStackedCases=trailingSumStackedCases, deaths=deaths, stackedDeaths=stackedDeaths, trailingSumStackedDeaths=trailingSumStackedDeaths)
