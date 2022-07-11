import csv

# Esta función abre el archivo csv y lo devuelve como una lista de listas


def open_csv(param="students"):
    dir = f"./database/{param}.csv"
    with open(dir, newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
    return data


# Esta función guarda los datos de una lista de listas en un archivo csv
def write_csv(data):
    with open("./database/students.csv", 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(data)

# Esta función elimina un estudiante de la lista de estudiantes
def delete_student(id):
    data = open_csv()
    for i in range(len(data)):
        if data[i][0] == id:
            data.pop(i)
            break
    write_csv(data)

# Esta función elimina un estudiante utilizando una función recursiva
def delete_student_recursive(id):
    data = open_csv()
    i = 0

    def delete(id, data, i):
        if i < len(data):
            if data[i][0] == id:
                data.pop(i)
                return data
            else:
                return delete(id, data, i+1)

    data = delete(id, data, i)
    write_csv(data)

# Esta función agrega un estudiante a la lista de estudiantes
def add_student(codigo, nombre, documento, programa, jornada, semestre):
    check = check_student(codigo, nombre, documento,
                          programa, jornada, semestre)
    if check:
        data = open_csv()
        data = [[codigo, nombre, documento, programa, jornada, semestre], *data]
        write_csv(data)
    else:
        print("Error: faltan datos")

# Esta función comprueba los datos de un estudiante
def check_student(codigo, nombre, documento, programa, jornada, semestre):
    if codigo == "" or nombre == "" or documento == "" or programa == "" or jornada == "" or semestre == "":
        return False
    return True

# Esta función muestra los detalle de un estudiante
def show_student(id):
    data = open_csv()
    for i in range(len(data)):
        if data[i][0] == id:
            return data[i]
    return False

# Esta función muestra los datos de un estudiante utilizando una función recursiva
def show_student_recursive(id):
    data = open_csv()
    i = 0

    def show(id, data, i):
        if i < len(data):
            if data[i][0] == id:
                return data[i]
            else:
                return show(id, data, i+1)

    data = show(id, data, i)
    return data

# Esta función busca un estudiante por cualquier parámetro
def search_student(param):

    print(param)
    if param == "":
        print("Error: faltan datos")
        return open_csv()
    else:
        data = open_csv()
        result = []
        for i in range(len(data)):
            if param in data[i]:
                result += [data[i]]
        print(result)
        return result

# Esta función busca un estudiante por cualuqer parámetro utilizando una función recursiva
def search_student_recursive(param):

    if param == "":
        print("Error: faltan datos")
        return open_csv()

    data = open_csv()
    i = 0
    result = []

    def search(param, data, i, result):
        if i < len(data):
            if param in data[i]:
                print("aqui", data[i])
                result += [data[i]]

            return search(param, data, i+1, result)
        
        return result

    data = search(param, data, i, result)
    return data
    


# Esta función retorna los 6 primeros estudiantes
def top_students():
    data = open_csv()
    result = []
    for i in range(len(data)):
        result += [data[i]]
    return result[:6]

# Esta función modifica los datos de un estudiante
def edit_student(id, codigo, nombre, documento, programa, jornada, semestre):
    check = check_student(codigo, nombre, documento,
                          programa, jornada, semestre)
    if check:
        data = open_csv()
        for i in range(len(data)):
            if data[i][0] == id:
                data[i] = [codigo, nombre, documento,
                           programa, jornada, semestre]
                break
        write_csv(data)
    else:
        print("Error: faltan datos")

# Esta función busca por cualquier parámetro
def search(param, file):
    if param == "":
        print("Error: faltan datos")
        return open_csv(file)
    else:
        data = open_csv(file)
        result = []
        for i in range(len(data)):
            if param in data[i]:
                result += [data[i]]

        return result

# Añadir cursos, profesores, sede a un estudiante
def add_all(id):

    data = open_csv()
    program = []

    courses = [[1, 2, 3], [4, 5, 6], [3, 2, 1]]

    for i in range(len(data)):
        if data[i][0] == id:

            if data[i][5] == "1":
                location = "SEDE 1 MEDELLIN"
            elif data[i][5] == "2" or data[i][5] == "3":
                location = "SEDE 2 CALI"
            elif data[i][5] == "4" or data[i][5] == "5" or data[i][5] == "6":
                location = "SEDE 3 BOGOTA"
            else:
                print("Error: semestre no encontrado")

            if data[i][3] == "QUIMICA":
                program = courses[0]
            elif data[i][3] == "SOFTWARE":
                program = courses[1]
            elif data[i][3] == "DERECHO":
                program = courses[2]
            else:
                print("Error: programa no encontrado")
            break

    courses_names = open_csv("courses")

    list_names_teachers = []
    list_names_courses = []

    for i in range(len(program)):
        index = program[i]
        list_names_courses.append(courses_names[index][1])
        list_names_teachers.append(courses_names[index][2])

    list_names_teachers = list(set(list_names_teachers))

    return list_names_courses, list_names_teachers, location
