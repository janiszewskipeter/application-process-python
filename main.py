from flask import Flask, render_template, request, url_for, redirect

import data_manager

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/mentors')
def mentors_list():
    mentor_name = request.args.get('mentor-last-name')
    mentor_city = request.args.get('city-name')
    if mentor_city:
        mentor_details = data_manager.get_mentors_by_city(mentor_city)
    else:
        mentor_details = data_manager.get_mentors()
    if mentor_name:
        mentor_details = data_manager.get_mentors_by_last_name(mentor_name)
    else:
        mentor_details = data_manager.get_mentors()

    # We get back a list of dictionaries from the data_manager (for details check 'data_manager.py')
    return render_template('mentors.html', mentors=mentor_details)

@app.route('/mentors_city')
def mentors_by_city():
    mentor_city = request.args.get('city-name')
    if mentor_city:
        mentor_details = data_manager.get_mentors_by_city(mentor_city)
    else:
        mentor_details = data_manager.get_mentors()
    return render_template('mentors.html', mentors=mentor_details)
if __name__ == '__main__':
    app.run(debug=True)
