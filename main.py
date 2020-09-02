import unittest
from  flask import  request, make_response, redirect , render_template, session, url_for, flash
from flask_login import login_required, current_user

from app import create_app
from app.firestore_service import get_users, get_todos ,put_todo, delete_todo,update_todo
app= create_app()

from app.form import LoginForm, TodoForm , DeleteTodoForm ,UpdateTodoForm

# todos = ['Comprar Cafe','Enviar Solicitud de Compra','Entrega del Producto']


   
@app.cli.command()
def test():
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner().run(tests)

@app.errorhandler(404)
def no_found(error):
    return render_template('404.html', error=error)

@app.errorhandler(500)
def no_found_services(error):
    return render_template('500.html', error=error)


@app.route('/')
def index():
    #    raise(Exception('500 error'))
    user_ip = request.remote_addr

    response = make_response(redirect('/hello'))
    # response.set_cookie('user_ip',user_ip)
    session['user_ip'] = user_ip
    return response


@app.route('/hello', methods=['POST', 'GET'])
@login_required
def hello():
    user_id = session.get('user_id')
    username = current_user.id
    todo_form = TodoForm()
    delete_form = DeleteTodoForm()
    update_form = UpdateTodoForm()
    context = {
        'user_ip':user_id,
        'todos': get_todos(user_id=username),
        'username': username,
        'todo_form': todo_form,
        'delete_form': delete_form,
        'update_form': update_form
    }

    if todo_form.validate_on_submit():
        put_todo(username, todo_form.description.data)

        flash('Tu tarea se creo con éxito!')

        return redirect(url_for('hello'))
  
    return render_template('hello.html', **context )


@app.route('/todos/delete/<todo_id>', methods=['POST'])
def delete(todo_id):
    user_id = current_user.id
    delete_todo(user_id=user_id, todo_id=todo_id)

    return redirect(url_for('hello'))

@app.route('/todos/update/<todo_id>/<int:done>', methods=['POST'])
def update(todo_id, done):
    user_id = current_user.id
    update_todo(user_id=user_id, todo_id=todo_id, done=done)
    return redirect(url_for('hello'))

if __name__ == '__main__':
    app.run(port = 5000, debug = True)