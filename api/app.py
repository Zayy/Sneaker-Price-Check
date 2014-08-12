import json
from flask import Flask,request,render_template
app = Flask(__name__)





@app.route('/price_my_sneaker', methods=['POST'])
def price_my_sneaker_form():
    shoe = request.form['sneaker_model']
    year = request.form['sneaker_year']
    condition = request.form['sneaker_condition']
    og_checkbox = request.form.getlist('ogcheckbox')
    #laces = request.form['laces']
    #insole = request.form['insole']
    #box = request.form['box']
    #paper = request.form['paper']
    print og_checkbox

    og_list = []
    for entry in og_checkbox:
        og_list.append({'og_part': entry})

    print og_list
    return shoe + ' ' + year + ' ' + condition 
    # + ' ' + laces + ' ' + insole + ' ' + box + ' ' + paper



@app.route('/contact', methods=['POST'])
def handle_contact_form():
        name = request.form['name_cf']
        mail = request.form['email_cf']
        message = request.form['message_cf']

        contact_dict = {'name':name,'mail': mail, 'message':message}
        contact_json = json.dumps(contact_dict)
        return contact_json


@app.route('/support',methods =['POST'])
def handle_support_form():
        problem = request.form['problem_sf']
        change = request.form['change_sf']

        support_dict = {'problem': problem, 'change':change}
        support_json =json.dumps(support_dict )
        return support_json




@app.route('/signup', methods=['POST'])
def handle_Signup_form():
        fullname= request.form['name_sf']
        email= request.form['email_sf']
        month = request.form['month_sf']
        day = request.form['day_sf']
        year = request.form['year_sf']

        signup_dict ={'fullname':fullname,'email':email,'month':month,'day':day,'year':year}
        #signup_dict={'fullname' : fullname,'email' : email}
        signup_json=json.dumps(signup_dict)
        return signup_json





if __name__ == "__main__":
    app.debug = True
    app.run('0.0.0.0')