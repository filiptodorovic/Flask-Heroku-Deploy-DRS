from flask import Flask, render_template, request, redirect, url_for, session, Response
from flask_session import Session
from flask import Blueprint

from MongoDBDRSProjekat.DataBaseWork.CRUD.UsersCRUD import UserCRUD
from MongoDBDRSProjekat.DataBaseWork.HelperFunctions import get_hash_password
from MongoDBDRSProjekat.Model.User import User
from MongoDBDRSProjekat.Model.CreditCard import CreditCard
from MongoDBDRSProjekat.Model.Valute import Valute

user_service = Blueprint('user_service', __name__)


@user_service.route('/register', methods =['POST'])
def register():
    repository = UserCRUD()
    msg = ''
    print(request.json['name'] + " has arrived")

    #basic input check
    if 'name' in request.json and 'password' in request.json and 'email' in request.json :
        name = request.json['name']
        last_name = request.json['last_name']
        address = request.json['address']
        city = request.json['city']
        country = request.json['country']
        telephone_number = request.json['telephone_number']
        email = request.json['email']
        password = request.json['password']
        hash_password = get_hash_password(password)
        #check how you get credit card
        credit_card = CreditCard()

        #initialize balance
        balance = [Valute("dollar", 0)]

        #check if the account with the same email already exists
        user = repository.find_user_by_email(email)
        if user:
            #account already exists
            return "User mail is taken!", 409
        else:
            #execute insert to database
            print("Adding new user")
            user = User(name, last_name, address, city, country, telephone_number, email, hash_password, credit_card, balance)

            # successfully added to database
            if repository.add_user(user):
                #log in successfully registered user
                session['loggedin'] = True
                session['id'] = user.email
                session['name'] = user.name
                user_json = repository.class_to_json(user)
                print("New user successfully added")
                return "OK", 201

            # failed adding to database
            else:
                print("i have failed to add to repository")
                return "Internal server connection error", 500
    #form is not filled out completely
    else:
        #did not fill out the form
        return "Form incorrectly filled", 400

@user_service.route('/editProfile', methods =['POST'])
def edit_profile():
    repository = UserCRUD()

    if session['loggedin'] == True:
        email = session['id']
        user = repository.find_user_by_email(email)
        msg = ''
        changed_data = 0
        if user:
            #update data which is submitted
            if 'name' in request.form:
                user.name = request.form['name']
                session['name'] = request.form['name']
                changed_data += 1
            if 'last_name' in request.form:
                user.last_name = request.form['last_name']
                changed_data += 1
            if 'address' in request.form:
                user.address = request.form['address']
                changed_data += 1
            if 'city' in request.form:
                user.city = request.form['city']
                changed_data += 1
            if 'country' in request.form:
                user.country = request.form['country']
                changed_data += 1
            if 'telephone_number' in request.form:
                user.telephone_number = request.form['telephone_number']
                changed_data += 1
            if 'password' in request.form:
                user.password = get_hash_password(request.form['password'])
                changed_data += 1

            if changed_data == 0:
                #no changes submitted
                user_json = repository.class_to_json(user)
                return user_json, 200
            else:
                #update user
                if repository.update_user(user):
                    #user successfully updated
                    user_json = repository.class_to_json(user)
                    return user_json, 200
                else:
                    return None, 500
        else:
            #user does not exist
            return None, 400

    else:
        #user is not logged in
        return None, 400
@user_service.route('/login', methods =['POST'])
def login():
    msg = ''
    repository = UserCRUD();

    if 'email' in request.form and 'password' in request.form:
        email = request.form['email']
        password = request.form['password']

        #check if account exists and if password is correct
        user = repository.find_user_by_email(email)
        if user and user.password == get_hash_password(password):
            session['loggedin'] = True
            session['id'] = user.email
            session['name'] = user.name
            #logged in successfully
            user_json = repository.class_to_json(user)
            return user_json, 200
        else:
            #failed log in
            return None, 401
    #did not input password or email
    return None, 401

@user_service.route('/logout', methods = ['POST'])
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('name', None)
    return 200

@user_service.route('/validateUser', methods =['POST'])
def validate_user():
    print(request.json['name_of_user'] + " has validated")
    print(request.json)
    repository = UserCRUD()
    #input check
    if 'name_of_user' in request.json and 'card_number' in request.json and 'expiration_date' in request.json and 'security_code' in request.json:
        email = session['id']
        user = repository.find_user_by_email(email)
        if user:
            #validation of input data
            if user.name == request.json['name_of_user'] and request.json['card_number'] == 4242424242424242 and request.json['expiration_date'] == 02.23 and request.json['security code'] == 123:
                credit_card = CreditCard(request.json['card_number'], request.json['name_of_user'], request.json['expiration_date'], request.json['security_code'])
                user.credit_card = credit_card
                if repository.update_user(user):
                    #successful validation of credit card and updating user data
                    user_json = repository.class_to_json(user)
                    return user_json, 200
                else:
                    #failed database update
                    return None, 500

            else:
                #invalid input data
                return None, 400
        else:
            #user does not exist
            return None, 400
    else:
        #client did not fill out the form
        return None, 400

@user_service.route('/balance')
def get_balance():
    repository = UserCRUD()
    email = session['id']
    user = repository.find_user_by_email(email)
    if user:
        return convert_online_balance_to_json(user), 200
    else:
        #there is no user with this email address in database, internal server error
        return None, 500

@user_service.route('/deposit', methods=['POST'])
def deposit():
    repository = UserCRUD()
    email = session['id']
    user = repository.find_user_by_email(email)
    if user:
        user = add_valute_amount(user, "dollar", request.form['amount'])
        if repository.update_user(user):
            user_json = repository.class_to_json(user)
            return user_json, 200
        else:
            return None, 400
    else:
        #user does not exist
        return None, 400


def add_valute_amount(user, valute_name, amount_to_add):
    for i in range(len(user.online_balance)):
        if user.online_balance[i].name == "dollar":
            user.online_balance[i].amount = request.form['amount']
            return user
    #there is no currency with that name in user's balance
    return None

def convert_online_balance_to_json(user):
    json_online_balance = []
    for valute in user.online_balance:
        valute_json = valute.valute_to_json()
        json_online_balance.append(valute_json)

    return json_online_balance
