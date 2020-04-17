import csv
import urllib2
rawURL = 'https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv'
#url = 'https://github.com/nytimes/covid-19-data/blob/master/us-counties.csv'
response = urllib2.urlopen(rawURL)
cr = csv.reader(response)
print('URLTest')
i=0
countyData=[]
for row in cr:
    #row date,county,state,fips,cases,deaths
	if row[1]=='Los Angeles':
		countyData.append(row)
print(len(countyData))

dates=[row[0] for row in countyData]
cases=[row[4] for row in countyData]
deaths=[row[5] for row in countyData]
i=0
while i<3:
	print(dates[i],cases[i],deaths[i])
	i+=1
