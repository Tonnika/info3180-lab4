from flash_wtf import Form 
from wtforms import FileField
from wtforms.validators import FileRequired, FileAllowed 

class UploadForm(Form):
    photo = FileField('image',validators=[FileRequired(), FileAllowed(['jpg','png'], 'Images only')])