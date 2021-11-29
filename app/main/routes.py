from flask import session, redirect, url_for, render_template, request
from . import main
from .forms import LoginForm


@main.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        session['name'] = request.get_json()["name"]
        session['room'] = "Messenger"
        return {"ok": True}
    elif request.method == 'GET':
        session['name'] = session.get('name', '')
        session['room'] = "Messenger"
    return {"name" : session['name']}


@main.route('/chat')
def chat():
    """Chat room. The user's name and room must be stored in
    the session."""
    name = session.get('name', '')
    room = session.get('room', '')
    if name == '' or room == '':
        return redirect(url_for('.index'))
    return render_template('chat.html', name=name, room=room)
