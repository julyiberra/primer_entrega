import random

# Preguntas para el juego
questions = [
    "¿Qué función se usa para obtener la longitud de una cadena en Python?",
    "¿Cuál de las siguientes opciones es un número entero en Python?",
    "¿Cómo se solicita entrada del usuario en Python?",
    "¿Cuál de las siguientes expresiones es un comentario válido en Python?",
    "¿Cuál es el operador de comparación para verificar si dos valores son iguales?",
]
# Respuestas posibles para cada pregunta, en el mismo orden que las preguntas
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
# Índice de la respuesta correcta para cada pregunta, en el mismo orden que las preguntas
correct_answers_index = [1, 2, 0, 3, 1]

# Se inicia el puntaje del juego
score=0
# El usuario deberá contestar 3 preguntas aleatorias diferentes
questions_to_ask = random.sample(list(zip(questions, answers, correct_answers_index)), k=3)

for k,elem in enumerate(questions_to_ask):
    # Se muestra la pregunta y las respuestas posibles
    print(questions[k])
    for i, answer in enumerate(answers[k]):
        print(f"{i + 1}. {answer}")

    # El usuario tiene 2 intentos para responder correctamente
    for intento in range(2):
        user_answer = input("Respuesta: ")
        # Se verifica si la respuesta es válida
        if user_answer.isdigit() and int(user_answer)-1 in range(4):
            user_answer=int(user_answer)-1
            # Se verifica si la respuesta es correcta
            if user_answer == correct_answers_index[k]:
                print("¡Correcto!")
                score+=1
                break
            else:
                score-=0.5
        else:
            print("Respuesta no válida")
            exit(1)
    else:
        # Si el usuario no responde correctamente después de 2 intentos,
        # se muestra la respuesta correcta
        print("Incorrecto. La respuesta correcta es:")
        print(answers[k][correct_answers_index[k]])

    # Se imprime un blanco al final de la pregunta
    print()
print(f'Puntaje: {score} puntos')