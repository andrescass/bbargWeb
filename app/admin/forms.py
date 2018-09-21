# app/admin/forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, IntegerField, SelectField
from wtforms.validators import DataRequired
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from ..models import Department, Employee, Role

class DepartmentForm(FlaskForm):
    """
    Form for admin to add or edit a department
    """
    name = StringField('Name', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    imageUrl = StringField('Image url', validators=[DataRequired()])
    submit = SubmitField('Submit')

class RoleForm(FlaskForm):
    """
    Form for admin to add or edit a role
    """
    name = StringField('Name', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    submit = SubmitField('Submit')

class EmployeeAssignForm(FlaskForm):
    """
    Form for admin to assign departments and roles to employees
    """
    is_admin = BooleanField('isAdmin')
    is_lore = BooleanField('isLore')
    is_chart = BooleanField('isChart')
    submit = SubmitField('Submit')

class LoreForm(FlaskForm):
    """
    Form for admin to add or edit a department
    """
    title = StringField('Title', validators=[DataRequired()])
    loreBody = StringField('Body', validators=[DataRequired()])
    imageUrl = StringField('Image url', validators=[DataRequired()])
    submit = SubmitField('Submit')

class HunterForm(FlaskForm):
	"""
	Form for hunters in charts
	"""
	name = StringField('Name', validators=[DataRequired()])
	position = IntegerField('Position', validators=[DataRequired()])
	lastPosition = IntegerField('Last Position', validators=[DataRequired()])
	submit = SubmitField('Submit')

class NiusForm(FlaskForm):
    """
    Form for admin to add or edit a news
    """
    title = StringField('Title', validators=[DataRequired()])
    newsBody = StringField('Body', validators=[DataRequired()])
    imageUrl = StringField('Image url', validators=[DataRequired()])
    submit = SubmitField('Submit')

class VideoForm(FlaskForm):
    """
    Form for admin to add or edit a video entry
    """
    title = StringField('Title', validators=[DataRequired()])
    videoBody = StringField('Description', validators=[DataRequired()])
    videoUrl = StringField('Url', validators=[DataRequired()])
    submit = SubmitField('Submit')

class EventsForm(FlaskForm): ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'),
    """
    Form for admin to add or edit a event entry
    """
    dayChoices = [('1', 'Monday'), ('2', 'Tuesday'), ('3', 'Wednesday'), ('4', 'Thursday'), ('5', 'Friday'), ('6', 'Saturday'), ('7', 'Sunday')] 
    hourChoices = [('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'), ('17', '17'), ('18', '18'), ('19', '19'), ('20', '20'), ('21', '21'), ('22', '22'), ('23', '23'), ('24', '24')] 
    title = StringField('Title', validators=[DataRequired()])
    eventBody = StringField('Description', validators=[DataRequired()])
    eventDay = SelectField('Day', choices=dayChoices, validators=[DataRequired()])
    eventHour = SelectField('Hour', choices=hourChoices, validators=[DataRequired()])
    submit = SubmitField('Submit')