from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.contacto import Contacto
from utils.db import db

contactos = Blueprint('contactos', __name__)

@contactos.route('/')
def index():
    contactos_query = Contacto.query.all()
    return render_template('index.html', contactos=contactos_query)

@contactos.route('/new', methods=['POST'])
def add_contact():

    nombre=request.form['nombre']
    email=request.form['email']
    tel=request.form['tel']
    foto= request.form['foto']

    nuevo_contacto = Contacto(nombre, email, tel, foto)

    db.session.add(nuevo_contacto)
    db.session.commit()

    flash("Contacto creado satisfactoriamente!")

    return redirect('/')

@contactos.route('/about')
def about():
    return render_template('about.html')

@contactos.route('/update/<id>', methods = ['POST', 'GET'])
def update(id):
    contacto = Contacto.query.get(id)

    if request.method == "POST":
        
        contacto.nombre=request.form['nombre']
        contacto.email=request.form['email']
        contacto.tel=request.form['tel']
        contacto.foto= request.form['foto']

        db.session.commit()

        flash("Contacto actualizado!")

        return redirect(url_for('contactos.index'))

    return render_template('update.html', contacto=contacto)

@contactos.route('/delete/<id>')
def delete(id):
    contacto = Contacto.query.get(id)
    db.session.delete(contacto)
    db.session.commit()
    
    flash('Contacto eliminado')

    return redirect(url_for('contactos.index'))

