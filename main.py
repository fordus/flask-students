from flask import Flask, redirect, render_template
from flask import request
from functions import *
import os


app = Flask(__name__)

# Página principal
@app.route('/')
def principal():  
    estudiantes = open_csv()
    page = 0
    return render_template('index.html',estudiantes=estudiantes,delete_student=delete_student, page=page)

# Borrar estudiante
@app.route('/borrar/<id>')
def borrar(id):
    delete_student_recursive(id)
    return redirect('/')

# Agregar estudiante
@app.route('/agregar', methods=['GET', 'POST'])
def agregar():
    if request.method == 'GET':
        return "<h1>Agregar estudiante</h1>"
    else:
        codigo = request.form['codigo']
        nombre = request.form['nombre']
        documento = request.form['documento']
        programa = request.form['programa']
        jornada = request.form['jornada']
        semestre = request.form['semestre']
        add_student(codigo, nombre, documento, programa, jornada, semestre)
        return redirect('/')

# Ver detalles de un estudiante
@app.route('/detalles/<id>')
def detalles(id):
    program,teachers,location = add_all(id)
    estudiante = show_student_recursive(id)
    if estudiante:
        return render_template('detalles.html',estudiante=estudiante,program=program, teachers=teachers, location=location)
    else:
        return "Estudiante no encontrado"

# Buscar un estudiante por cualquier parámetro
@app.route('/buscar', methods=['GET', 'POST'])
def buscar():
    if request.method == 'GET':
        return "<h1>Buscar estudiante</h1>"
    else:
        param = request.form['param']
        estudiantes = search_student_recursive(param)
        return render_template('buscar.html',estudiantes=estudiantes,delete_student=delete_student)

# Editar un estudiante
@app.route('/editar/<id>', methods=['GET', 'POST'])
def edit(id):
    if request.method == 'GET':
        estudiante = show_student(id)
        return render_template('editar.html',estudiante=estudiante)
    else:
        codigo = request.form['codigo']
        nombre = request.form['nombre']
        documento = request.form['documento']
        programa = request.form['programa']
        jornada = request.form['jornada']
        semestre = request.form['semestre']
        edit_student(id, codigo, nombre, documento, programa, jornada, semestre)
        return redirect('/')

# Página de cursos
@app.route('/cursos')
def cursos():
    cursos = open_csv("courses")
    return render_template('cursos.html',cursos=cursos)

# Buscar un curso por cualquier parámetro
@app.route('/buscar_curso', methods=['GET', 'POST'])
def buscar_curso():
    if request.method == 'GET':
        return "<h1>Buscar curso</h1>"
    else:
        param = request.form['param']
        cursos = search(param, "courses")
        return render_template('cursos.html',cursos=cursos)

# Página de profesores
@app.route('/profesores')
def profesores():
    profesores = open_csv("teachers")
    return render_template('profesores.html',profesores=profesores)

# Buscar un profesor por cualquier parámetro
@app.route('/buscar_profesor', methods=['GET', 'POST'])
def buscar_profesor():
    if request.method == 'GET':
        return "<h1>Buscar profesor</h1>"
    else:
        param = request.form['param']
        profesores = search(param, "teachers")
        return render_template('profesores.html',profesores=profesores)

# Página de sedes
@app.route('/sedes')
def sedes():
    sedes = open_csv("locations")
    return render_template('sedes.html',sedes=sedes)

# Buscar una sede por cualquier parámetro
@app.route('/buscar_sede', methods=['GET', 'POST'])
def buscar_sede():
    if request.method == 'GET':
        return "<h1>Buscar sede</h1>"
    else:
        param = request.form['param']
        sedes = search(param, "locations")
        return render_template('sedes.html',sedes=sedes)

# Paginacion
@app.route('/pagina/<int:page>')
def pagination(page):
    estudiantes = open_csv()
    return render_template('index.html',estudiantes=estudiantes,delete_student=delete_student,page=page)

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))