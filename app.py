"""Blogly application."""

from flask import Flask, redirect, render_template, request, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:2118@localhost/blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'asdfghjkl'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all()

@app.route('/')
def homepage():

    return redirect('users')

@app.route('/users')
def show_users():
  
    users = User.query.order_by(User.last_name, User.first_name).all()
    return render_template('users/index.html', users=users)

@app.route('/users/new', methods=['GET'])
def new_user_form():
    
    return render_template('users/create_user.html')

@app.route('/users/new', methods=['POST'])
def add_new_user():

    new_user = User(
        first_name = request.form['first_name'],
        last_name = request.form['last_name'],
        image_url = request.form['image_url'] or None)

    db.session.add(new_user)
    db.session.commit()

    return redirect('/users')

@app.route(f"/users/<int:id>")
def show_user_info(id):

    user = User.query.get_or_404(id)
    return render_template('users/user_details.html', user=user)

@app.route(f"/users/<int:id>/edit")
def show_edit_user_page(id):
    
    user = User.query.get_or_404(id)
    return render_template('users/edit_user.html', user=user)

@app.route(f"/users/<int:id>/edit", methods=['POST'])
def edit_user(id):

    user = User.query.get_or_404(id)
    user.first_name = request.form['first_name'],
    user.last_name = request.form['last_name'],
    user.image_url = request.form['image_url'] or None

    db.session.add(user)
    db.session.commit()

    return redirect('/users')    

@app.route(f"/users/<int:id>/delete", methods=['POST'])
def delete_user(id):

    user = User.query.get_or_404(id)
    
    db.session.delete(user)
    db.session.commit()

    return redirect('/users')
