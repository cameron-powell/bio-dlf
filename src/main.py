from flask import flash
from flask import Flask
from flask import redirect
from flask import render_template
from flask import url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import SelectField
from wtforms import SubmitField
from wtforms import TextAreaField
from wtforms.validators import DataRequired


app = Flask(__name__)
app.config['SECRET_KEY'] = 'temp key' #TODO: This is only for debugging.  Change to environment variable for production use.
bootstrap = Bootstrap(app)


class FeedbackForm(FlaskForm):
    section = SelectField('Lab Section',
                          choices=[('P01', 'P01 Monday 1:05pm-3:55pm'), ('Q05', 'Q05 Wednesday 1:05pm-3:55pm')])
    feedback = TextAreaField('Feedback', validators=[DataRequired()])
    submit = SubmitField('Submit')


@app.route('/')
def index():
    return render_template('base.html')


@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    form = FeedbackForm()
    if form.validate_on_submit():
        flash('Thank you for your feedback!')
        return redirect(url_for('index'))
    return render_template('feedback.html', form=form)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return '<h1>500</h1>', 500


if __name__ == '__main__':
    app.run(debug=True)
