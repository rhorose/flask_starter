from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileRequired




class PropertyForm(FlaskForm):
    prop_title=StringField('Property Title', validators=[DataRequired()])
    description=TextAreaField('Description',validators=[DataRequired()])
    no_rooms=StringField('No. of Rooms', validators=[DataRequired()])
    no_bathrooms=StringField('No. of Bathrooms', validators=[DataRequired()])
    price=StringField('Price', validators=[DataRequired()])
    prop_type= SelectField('House/ Apartment', choices=[('House', 'House'), ('Apartment', 'Apartment'),('Townhomes','Townhomes'),('Duplexes','Duplexes')])
    location=StringField('Location', validators=[DataRequired()])     
    photo= FileField('Photo',validators=[FileRequired()])

    