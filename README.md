# CoroFlask

Visualizing Coronavirus cases and deaths using Flask and ChartJS for US counties. 
While most of the websites (like (The New York Times)[https://www.nytimes.com/interactive/2020/us/california-coronavirus-cases.html#cases] at the time of building this) focus on showing graphs for states and countries, I wanted to see graphs for each county. 

I have also changed the way graphs display data. I wanted to see total number of cases and new cases in one graph. So, each day will have sum of cases till day and at the top count of number of cases for that day in a different colour. Adding the heights of both the bars would give the total count till date.

## Source
(NYT)[https://github.com/nytimes/covid-19-data]

### Screenshots
![ScreenShot2020-04-28142438.jpg](/Screenshots/ScreenShot2020-04-28142438.jpg)
![Screen Shot 19-04-2020](/Screenshots/ScreenShot2020-04-19214043.jpg)


### TODO list:

- [x] Get both the charts displaying.
- [x] Update 'updateChart' function to toggle between daily, weekly, biweekly avergaes.
	- [x] Add 3-day period for completeness.
	- [ ] Take averages instead of showing just the dates's values.
- [x] Add a back button. 
- [x] Update to select any county from a drop down. (new branch)
	- [x] Implement drop down over a text box.
		- [x] Get county names based on state selected.
		- [x] Use this county name to display the charts.
		- [x] Include all US states. ~Currently, Arizona and California are only selectable.~
	- [ ] Extend this to include other countries, if possible!
- [x] Fix reading CountyName from a list.
- [x] Add empty validation check on entered County Name.
	- [ ] Improve validation checks. Maybe use a list of countynames and compare if the entered text is one of them?
- [x] Stacked charts to show each periods gain increase.
	- [x] Add stacked chart for deaths.
- [x] Fix width of graphs. Now they are going to the end of browser window.
- [x] UpdateChart function to update the stacked charts.
- [x] Remove old non stacked charts.
	- [ ] Maybe give user option to select if they want to see stacked or not? 
- [x] Remove second y axis on stacked graphs.
- [ ] Reorder buttons so it looks a bit compact.

### Notes:
1. Flask can pull data from Select tag only using name attribute. Does not work for id attribute.