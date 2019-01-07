from wtforms import FileField,StringField, IntegerField, TextAreaField, SubmitField, RadioField, SelectField, Form, PasswordField
from wtforms import validators, ValidationError



class Dataform(Form):
    image = FileField('Image', [validators.DataRequired('Please upload the image')])
    time = StringField('Time', [validators.DataRequired('Please type in the time')])
    date = StringField('Date', [validators.DataRequired('Please type in the date')])
    location = StringField('Location', [validators.DataRequired('Please type in the location')])
    reason = StringField('Reason', [validators.data_required('Please tell us what happen')])
    submit = SubmitField('Submit')


