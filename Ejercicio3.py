# Lista de estudiantes
estudiantes = [
    {"id": 1, "Nombre": "Paula Casas"},
    {"id": 2, "Nombre": "Maria Perez"},
    {"id": 3, "Nombre": "Pedro Daza"},
    {"id": 4, "Nombre": "Luis Lopez"}
]

# Lista de cursos
cursos = [
    {"id": 22, "Nombre": "Des. Aplicaciones con acceso a datos", "Horario": "Jueves 8-11am, Viernes 8-10 am",
        "Profesor": "Arturo Gomez", "Lista estudiantes": ["Estudiante 1", "Estudiante 2"]},
    {"id": 23, "Nombre": "Estructura de datos I", "Horario": "Lunes 8-11am, Jueves 8-10 am",
        "Profesor": "Julian Triana", "Lista estudiantes": ["Estudiante 1", "Estudiante 3"]},
    {"id": 24, "Nombre": "Des. Aplicaciones Web I", "Horario": "Martes 10-1",
        "Profesor": "Margarita Gonzalez", "Lista estudiantes": ["Estudiante 3", "Estudiante 4"]},
    {"id": 25, "Nombre": "Ingles IV", "Horario": "Lunes Miercoles 6-8 am\nViernes 7-8 am",
        "Profesor": "Claudia Torres", "Lista estudiantes": ["Estudiante 1", "Estudiante 2"]},
    {"id": 26, "Nombre": "Electiva", "Horario": "Jueves 7-10pm",
        "Profesor": "Alex Arevalo", "Lista estudiantes": ["Estudiante 1", "Estudiante 2"]},
    {"id": 27, "Nombre": "Practica Empresarial", "Horario": "Miercoles 2-4",
        "Profesor": "Daniel Avila", "Lista estudiantes": ["Estudiante 3", "Estudiante 4"]}
]

# Notas de los estudiantes por curso
notas = [
    {"estudiante_id": 1, "curso_id": 22, "notas": [4.0, 3.8]},
    {"estudiante_id": 1, "curso_id": 23, "notas": [3.7, 4.2]},
    {"estudiante_id": 1, "curso_id": 25, "notas": [4.1, 3.9]},
    {"estudiante_id": 1, "curso_id": 26, "notas": [4.3, 3.6]},
    {"estudiante_id": 2, "curso_id": 22, "notas": [3.9, 4.1]},
    {"estudiante_id": 2, "curso_id": 25, "notas": [4.2, 3.8]},
    {"estudiante_id": 2, "curso_id": 26, "notas": [4.0, 3.7]},
    {"estudiante_id": 3, "curso_id": 24, "notas": [3.8, 4.0]},
    {"estudiante_id": 3, "curso_id": 23, "notas": [3.9, 4.1]},
    {"estudiante_id": 3, "curso_id": 27, "notas": [4.0, 3.9]},
    {"estudiante_id": 4, "curso_id": 24, "notas": [4.1, 3.8]},
    {"estudiante_id": 4, "curso_id": 27, "notas": [3.7, 4.2]}
]

# Agregar un estudiante
estudiantes.append({"id": 5, "Nombre": "Jorge Trejo"})

# Matricular el nuevo estudiante en un curso
# Matricular a Jorge en el curso de Des. Aplicaciones con acceso a datos
cursos[0]["Lista estudiantes"].append("Jorge Trejo")

# Promedio de un estudiante
promedio_nota = (notas[0]["notas"][0] + notas[0]["notas"][1]) / 2


# Entrada del usuario
nombre_curso = input("Ingrese el nombre del curso: ")

# Buscar el curso en la lista
estudiantes_curso = []
for curso in cursos:
    if curso["Nombre"] == nombre_curso:
        estudiantes_curso = curso["Lista estudiantes"]
        break

# Mostrar los estudiantes
if estudiantes_curso:
    print(f"Estudiantes matriculados en {nombre_curso}:")
    for estudiante in estudiantes_curso:
        print(f"{estudiante}")
else:
    print(f"No se encontraron estudiantes para el curso: {nombre_curso}")

# Crear lista que combina estudiantes con sus cursos y notas
estudiantesConCursos = []

print("\nEstudiantes con sus cursos y notas:")

for estudiante in estudiantes:
    estudianteConCursos = {
        "id": estudiante["id"],
        "Nombre": estudiante["Nombre"],
        "cursos": []
    }
    for curso in cursos:
        if estudiante["Nombre"] in curso["Lista estudiantes"]:
            cursoConNotas = {
                "id": curso["id"],
                "Nombre": curso["Nombre"],
                "horario": curso["Horario"],
                "Profesor": curso.get("Profesor", "N/A"),
                "notas": []
            }
            for nota in notas:
                if nota["estudiante_id"] == estudiante["id"] and nota["curso_id"] == curso["id"]:
                    cursoConNotas["notas"] = nota["notas"]
            estudianteConCursos["cursos"].append(cursoConNotas)
    estudiantesConCursos.append(estudianteConCursos)

# Mostrar la lista final
for estudiante in estudiantesConCursos:
    print(f"Estudiante: {estudiante['Nombre']}")
    for curso in estudiante["cursos"]:
        print(f"  Curso: {curso['Nombre']}")
        print(f"  Horario: {curso['horario']}")
        print(f"  Profesor: {curso['Profesor']}")
        print(f"  Notas: {curso['notas']}")
    print()
