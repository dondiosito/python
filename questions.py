import random
import sys

# Preguntas para el juego
questions = [
    "¿Qué función se usa para obtener la longitud de una cadena en Python?",
    "¿Cuál de las siguientes opciones es un número entero en Python?",
    "¿Cómo se solicita entrada del usuario en Python?",
    "¿Cuál de las siguientes expresiones es un comentario válido en Python?",
    "¿Cuál es el operador de comparación para verificar si dos valores son iguales?",
]

# Respuestas posibles para cada pregunta
answers = [
    ("size()", "len()", "length()", "count()"),
    ("3.14", "'42'", "10", "True"),
    ("input()", "scan()", "read()", "ask()"),
    (
        "// Esto es un comentario",
        "/* Esto es un comentario */",
        "-- Esto es un comentario",
        "# Esto es un comentario",
    ),
    ("=", "==", "!=", "==="),
]

correct_answers_index = [1, 2, 0, 3, 1]

quiz_data = list(zip(questions, answers, correct_answers_index))

questions_to_ask = random.sample(quiz_data, k=3)

score = 0  

for question, options, correct_index in questions_to_ask:
    print(question) 
    for i, option in enumerate(options):
        print(f"{i + 1}. {option}")  

    for intento in range(2):
        user_input = input("Respuesta: ")

        if not user_input.isdigit():  
            print("Respuesta no válida")
            score -= 1  
            sys.exit(1)  

        user_answer = int(user_input) - 1  

        if user_answer < 0 or user_answer >= len(options):  
            print("Respuesta no válida")
            score -= 1
            sys.exit(1)

        if user_answer == correct_index: 
            print("¡Correcto!")
            score += 1
            break  
        else:
            print("Incorrecto, intenta de nuevo.")

    else:  
        print("Incorrecto. La respuesta correcta es:")
        print(options[correct_index])  

    print() 

print(f"Puntaje final: {score}")
