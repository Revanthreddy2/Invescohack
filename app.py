from flask import Flask, render_template, request, session

import week
import matplotlib as plt
app = Flask(__name__)


@app.route('/',methods=['GET','POST'])
def index():
    values=False
    overall=False
    is_submitted=False
    if request.method == 'POST':
        is_submitted=True
        # session['form_submitted'] = True
        values,overall=week.calculate_values(request.form['startDate'],request.form['endDate'])
        week.plot_monthly_means()
        return render_template('index.html',values=values,overall=overall,is_submitted=is_submitted)
    else:
        # session.pop('form_submitted', None)
        is_submitted=False
        return render_template('index.html',is_submitted=is_submitted)


if __name__ == '__main__':
    app.run(debug=True)
