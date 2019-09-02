from wtforms import Form, StringField
from wtforms.validators import Length, Email, DataRequired


class FeedbackForm(Form):
    username = StringField("Username", validators=[DataRequired(), Length(max=64)])
    email = StringField("Email", validators=[DataRequired(), Email(message="邮箱格式不正确")])
    subject = StringField("Username", validators=[DataRequired(), Length(max=64)])
    message = StringField("Message", validators=[DataRequired()])
