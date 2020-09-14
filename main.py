from flask import Flask, render_template, request, url_for, redirect
import random
import data_manager

app = Flask(__name__)


@app.route('/')
def index():

    return render_template('index.html')


@app.route('/mentors')
def mentors_list():
    mentor_name = request.args.get('mentor-last-name')
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

@app.route('/applicants')
def applicants():
    applicant_name = request.args.get('applicant_name')

    if applicant_name:
        details = data_manager.get_applicant_data_by_name(applicant_name)
    else:
        details = data_manager.get_all_applicans()
    return render_template('applicants.html', applicans=details)

@app.route('/applicants-phone')
def applicants_phone():
    applicant_email = request.args.get('applicant_email')
    if applicant_email:
        details = data_manager.get_applicants_data_by_email(applicant_email)
    else:
        details = data_manager.get_all_applicans()
    return render_template('applicants-phone.html', applicans=details)

@app.route('/applicant-info/<application_code>')
def applicant_info(application_code):
    applicant_info = data_manager.get_applicant_info(application_code)
    return render_template('applicants-info.html', applicant_info=applicant_info)


@app.route('/update_nr/<application_code>', methods=['POST'])
def update_number_in_db(application_code):
    if request.method == "POST":

        new_nr = request.form['new_nr']
        # new_nr = request.args.get('new_nr')
        # print(text)
        # print(new_nr)
        data_manager.update_nr(new_nr, application_code)
        applicant_info = data_manager.get_applicant_info(application_code)
        return render_template('applicants-info.html', applicant_info=applicant_info)
    else:
        applicant_info = data_manager.get_applicant_info(application_code)
        return render_template('applicants-info.html', applicant_info=applicant_info)


@app.route('/delete/<application_code>', methods=['POST'])
def delete_user(application_code):
    if request.method == "POST":
        data_manager.delete(application_code)
        details = data_manager.get_all_applicans()
        return render_template('applicants.html', applicans=details)
    else:
        applicant_info = data_manager.get_applicant_info(application_code)
        return render_template('applicants-info.html', applicant_info=applicant_info)

@app.route('/delete_by_email_ending', methods=['POST'])
def delete_by_email_ending() :
    if request.method == "POST":
        email_end = request.form['email-ending']
        data_manager.delete_by_email_ending(email_end)
        details = data_manager.get_all_applicans()
        return render_template('applicants.html', applicans=details)
    return None

@app.route('/new')
def new():
    return render_template('add_applicant.html')

@app.route('/add_applicant', methods=['POST'])
def add_applicant():
    if request.method == 'POST':
        name = request.form['name']
        last_name = request.form['last_name']
        phone = request.form['phone_nr']
        email= request.form['email']
        code = random.randint(100, 1000)
        print(code)
        data_manager.append_applicant(name, last_name, phone, email,code)
        applicant_info = data_manager.get_applicant_info(code)
        return render_template('applicants-info.html', applicant_info=applicant_info)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
