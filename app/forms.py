from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import ValidationError, DataRequired, Regexp, Email, EqualTo, Length
from app.models import User


class LoginForm(FlaskForm):
    username = StringField('نوم', validators=[
        DataRequired(message="دغه ځای خالی مه پریږدی!"),
        Regexp('^[A-Za-z0-9]*$', message="یوازې انګلیسی حروف او عددونه")
    ])
    password = PasswordField('پاسورډ', validators=[
        DataRequired(message="دغه ځای خالی مه پریږدی!")
    ])
    remember_me = BooleanField('ما په یاد ولرئ')
    submit = SubmitField('ننوځئ')

class RegistrationForm(FlaskForm):
    username = StringField('نوم', validators=[
        DataRequired(message="دغه ځای خالی مه پریږدی!"),
        Regexp('^[A-Za-z0-9]*$', message="یوازې انګلیسی حروف او عددونه")
    ])
    email = StringField('ایمیل', validators=[DataRequired(), Email()])
    password = PasswordField('پاسورډ', validators=[DataRequired()])
    password2 = PasswordField('پاسورډ بیاوارې', validators=[
        DataRequired(), EqualTo('password')
    ])
    submit = SubmitField('توکل')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a differetn email address')


class EditProfileForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    about_me = TextAreaField('About me', validators=[Length(min=0, max=140)])
    password = PasswordField('نوی پاسورډ', validators=[DataRequired()])
    password2 = PasswordField('پاسورډ بیاوارې', validators=[
        DataRequired(), EqualTo('password')
    ])

    submit = SubmitField('Submit')

class CreatePostForm(FlaskForm):
    title = TextAreaField('عنوان', validators=[
        DataRequired(), 
        Length(min = 10, max = 132)
    ])
    post = TextAreaField('مقاله دلته ولیکه . .‌ .', validators=[
        DataRequired(),
        Length(min=20, max=3000)
    ])
    submit = SubmitField('Submit')
