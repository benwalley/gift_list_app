from flask import render_template, flash, url_for, redirect, session, request
from gift_list import app
from lists.form import GiftsForm, ExtraForm
from gift_list import db
from users.models import User
from lists.models import Gifts, Extras
from users.decorators import login_required
import bcrypt

#INDEX ROUTE

@app.route('/')
@app.route('/index')
def index():
    if session.get('name'):
        return redirect(url_for('list'))
    else:
        return redirect(url_for('login'))

#ROUTE FOR ADDING A GIFT TO DATABASE
    
@app.route('/addgift', methods = ("GET", "POST"))
@login_required
def addgift():
    form=GiftsForm()
    if form.validate_on_submit():
        name = session.get('name')
        gift = Gifts(
            form.gift.data,
            form.comment.data,
            name
            )
        db.session.add(gift)
        db.session.commit()
        flash('Gift Wish added')
        return redirect(url_for('addgift'))
        
            
    return render_template('lists/addGift.html', form=form)
  
#ROUTE FOR SHOWING ALL USERS  
@app.route('/list')
def list():
    users = User.query.order_by(User.name.asc())
    return render_template('lists/list.html', users = users)

#ROUTE FOR SHOWING A SPECIFIC USERS LIST
@app.route('/list/<name>', methods = ("GET", "POST"))
def user_list(name):
    wanter = name
    gifts = Gifts.query.filter_by(wanter = name)
    extras = Extras.query.filter_by(wanter = name)
    form=ExtraForm()
    if form.validate_on_submit():
        giver = session.get('name')
        extra = Extras(
            form.comment.data,
            wanter,
            giver
            )
        db.session.add(extra)
        db.session.commit()
        return redirect(url_for('list'))
    return render_template('lists/user_list.html', gifts = gifts, form = form, name = name, extras = extras)

#ROUTE THAT IS SENT TO IN ORDER TO SAY THAT YOU ARE GIVING A GIFT    
@app.route('/give/<int:gift_id>')
@login_required
def give(gift_id):
    gift = Gifts.query.filter_by(id=gift_id).first_or_404()
    if gift.giver:
        gift.giver = gift.giver + " " + session.get('name')
    else:
        gift.giver = session.get('name')
    
    db.session.commit()
    return redirect('/list')
    
    
@app.route('/delete/<int:gift_id>')
@login_required
def delete(gift_id):
    gift = Gifts.query.filter_by(id = gift_id).first()
    db.session.delete(gift)
    db.session.commit()
    return redirect('/list')
    

@app.route('/delete_extra/<int:extra_id>')
@login_required
def delete_extra(extra_id):
    extra = Extras.query.filter_by(id = extra_id).first()
    db.session.delete(extra)
    db.session.commit()
    return redirect('/list')

@app.route('/dont_give<int:gift_id>')   
def dont_give(gift_id):
    gift = Gifts.query.filter_by(id=gift_id).first_or_404()
    gift.giver = gift.giver.replace(session.get('name'), '')
    gift.giver = gift.giver.replace(session.get('name').lower(), '')
    
    
    db.session.commit()
    return redirect('/list')
    
    
    