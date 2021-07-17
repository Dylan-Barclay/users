from flask import Flask, render_template, request, redirect, session
from users import User
app = Flask(__name__)
app.secret_key = 'blah'

@app.route('/')
def index():
    users = User.get_all_users()
    return render_template('index.html', users = users)

@app.route('/user/create')
def new_user():
    return render_template('add_new_user.html')

@app.route('/create', methods=['POST'])
def create_new_user():
    User.create_new_user(request.form)
    return redirect('/')

@app.route('/show/<int:user_id>')
def show_user(user_id):
    data = {
        'id': user_id
    }
    user = User.show_user(data)
    return render_template('show.html', user = user)

@app.route('/user/delete/<int:user_id>')
def delete_user(user_id):
    data = {
        'id' : user_id
    }
    User.delete_user(data)
    return redirect('/')

@app.route('/user/edit/<int:user_id>')
def edit_user(user_id):
    data = {
        'id' : user_id
    }
    user = User.show_user(data)
    return render_template ('edit.html',user = user )

@app.route('/user/update/<int:user_id>', methods = ['POST'])
def update_user(user_id):
    data = {
        'id': user_id,
        'first_name' : request.form["first_name"],
        'last_name' : request.form["last_name"],
        'email' : request.form["email"]
    }
    User.update_user(data)
    return redirect(f'/show/{user_id}')



if __name__=='__main__':
    app.run(debug=True)