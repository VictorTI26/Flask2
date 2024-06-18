from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField

class CadastroForm(FlaskForm):
    usuario = StringField(label='Username:')