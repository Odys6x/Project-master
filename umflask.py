from flask import *
from user import *
from forms import *
from Data import *
from Verification import *
import functools

app = Flask(__name__)
app.secret_key = 'secret_123'

@app.route('/login',  methods=('GET', 'POST'))
def login():
    login_form = LoginForm(request.form)
    error = None
    if request.method == 'POST':
        user = get_user(login_form.id.data, login_form.password.data)
        if user is False:
            error = 'You are banned'
        if user is None:
            error = 'Wrong username and password'
        else:
            return redirect(url_for('homepage'))
        flash(error)
    return render_template('login.html', form=login_form)

@app.route('/register', methods=('GET', 'POST'))
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST':
        username = form.id.data
        password = form.password.data
        answer = form.answer.data
        error = None
        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        elif not answer:
            error = 'Answer is required'
        else:
            create_user(username, password, answer)
            return redirect(url_for('login'))
        flash(error)
    return render_template('register.html', form=form)

@app.route('/changepassword', methods=('GET', 'POST'))
def password():
    pform = PasswordForm(request.form)
    if request.method == 'POST':
        username = pform.id.data
        password = pform.password.data
        answer = pform.answer.data
        error = None
        user = cpassword(username, answer)
        if user is None:
            error = 'Wrong Details'
        else:
            npassword(username, password)
            return redirect(url_for('login'))
        flash(error)
    return render_template('password.html', form=pform)

@app.route('/blacklist', methods=('GET', 'POST'))
def blacklist():
    bform = BlacklistForm(request.form)
    if request.method == 'POST':
        username = bform.id.data
        reason = bform.reason.data
        error = None
        if not username:
            error = 'Username is required'
        if not reason:
            error = 'Reason is required'
        else:
            blacklistuser(username, reason)
            return redirect(url_for('blacklist', form=bform))
        flash(error)
    return render_template('blacklist.html', form=bform)

@app.route('/homepage')
def homepage():
    return render_template('Home Page.html')

@app.route('/ExcuseForm', methods=('GET', "POST"))
def submit_Data():
    form = Dataform(request.form)
    if request.method == "POST":
        image = form.image.date
        time = form.time.data
        date = form.date.data
        location = form.location.data
        reason=form.reason.data
        error = None
        if not image:
            error = "Image is required"

        elif not time:
            error = "Time is required"

        elif not date:
            error = "Date is required"

        elif not location:
            error = "Location is required"

        elif not reason:
            error = "Reason is required"

        else:
            set_data(image, time, date, location, reason)
            flash("Submitted Sucessfully")
        flash(error)

    return render_template("Excuse Form.html",form=form)


if __name__ == '__main__':
    app.run()
