from flask import *
from Verification import *
from Data import *

app = Flask(__name__)
app.secret_key ='secret_123'

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


@app.route('/Homepage')
def Homepage():
    return render_template("HomePage.html")

@app.route('/Password')
def password():
    return render_template("password.html")

if __name__ == '__main__':
    app.run()
