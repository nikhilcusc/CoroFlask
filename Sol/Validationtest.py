from flask_inputs import Inputs
from wtforms.validators import DataRequired 
from wtforms import StringField as StringField

class Validation(Inputs):
	county = StringField('county', validators=[InputRequired()])
CountyName = 'Maricopa'
def case(countyName):
	pass
CountyName = ''
#validate the CountyName here
validate = Validation()
print(validate)
if not validate: #empty 
	print('Empty')
else:
	print('Not Empty')
