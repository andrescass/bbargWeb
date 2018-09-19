# app/admin/forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, IntegerField
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