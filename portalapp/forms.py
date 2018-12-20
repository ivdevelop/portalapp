from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import SelectField, SubmitField, StringField, IntegerField, SelectMultipleField
from wtforms import validators, ValidationError
from wtforms.validators import InputRequired


class UploadForm(FlaskForm):
	agreementUp = SelectField('Choose SLA')
	ciReposUp = SelectField('Choose Repository')
	inputFileUp = FileField('Choose CSV file', validators=[FileRequired(),
		FileAllowed(['csv'], 'Only CSV format allowed')
		])
	submit_button = SubmitField('Upload')

class CreateForm(FlaskForm):
	companyNameCr = StringField('Company Name')
	officeCr = SelectField('Choose country') ##Need to provide choices from DB 
	agTypeCr = SelectField('Choose service type') ##Need to provide choices from DB 
	slaNameCr = StringField('Name of Agreement')
	slaNumberCr = StringField('Set the number of contract')
	#slaStartDateCr = DateField('Set Start Date of Contract') # Set Datetime format
	#slaEndDateCr = DateField('Set End Date of Contract') # Set Datetime format
	#slaSignDate = DateField ('Date of contract sign') # Set Datetime format
	slaServiceAvalCr = SelectField('Service Avalibility Schedule') ##Need provide choice from DB
	slaServiceProvCr = SelectField('Service Providing Schedule') ##Need provide choice from DB
	teamCr = SelectField('Choose team') ##Set default team, First line is default line
	slmServiceCr = SelectMultipleField('Choose provided services (Hold CTRL to choose)') ## Need provide from DB
	inputFielCr = FileField('Choose CSV file', validators=[FileRequired(),
		FileAllowed(['csv'], 'Only CSV format allowed')
		])
	submit_button = SubmitField('Upload')

	