from  flask import Flask
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Nombre Usuario', validators= [DataRequired()])
    password = PasswordField('password', validators= [DataRequired()])
    submit = SubmitField('Enviar')

class TodoForm(FlaskForm):
    description = StringField('Description', validators= [DataRequired()])
    submit = SubmitField('Crear')

class DeleteTodoForm(FlaskForm):
    submit = SubmitField('Eliminar')

class UpdateTodoForm(FlaskForm):
    submit = SubmitField('Actualizar')