from base import app
from flask import render_template, redirect, url_for
from base.models import Message
from base.forms import MessageForm, OwnerForm
from base import db
import datetime

x = datetime.datetime.now()

def delete_outdated():
    new = Message.query.filter(Message.date.startswith((int(x.strftime("%d%m%Y"))))).all()
    for item in Message.query.filter().all():
        if item in new:
            continue
        db.session.delete(item)
    db.session.commit()

@app.route('/')
def main_page():
    return render_template('index.html')

@app.route('/owner_check', methods=['GET', 'POST', 'DELETE'])
def verification_page():
    form = OwnerForm()
    if form.validate_on_submit():
        if form.code.data == "0000":
            return redirect(url_for('owner_page')), delete_outdated()
    return render_template('check.html', form=form)

@app.route('/owner')
def owner_page():
    msg = Message.query.all()
    return render_template("owner.html", msg=msg)


@app.route('/request', methods=['GET', 'POST'])
def request_page():
    form = MessageForm()
    if form.validate_on_submit():
        request_to_create = Message(name=form.name.data,
                                    date=datetime.datetime.now().strftime('%d%m%Y'),
                                    description=form.description.data)
        
        db.session.add(request_to_create)
        db.session.commit()
        return redirect(url_for('main_page'))
    return render_template('request.html', form=form, time=datetime.datetime.now())