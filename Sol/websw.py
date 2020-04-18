from flask import Flask, render_template, Markup, request
import pandas as pd
import csv
import urllib2

rawURL = 'https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv'
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/Corochart', methods=['POST'])
def Corochart():
	#get county name
	CountyName = request.form['county']
	#validate the CountyName here
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
	county = [row[1],row[2]]
	return render_template('Corochart.html',title='Corochart', countyData=county, dates=dates, cases=cases, deaths=deaths)
