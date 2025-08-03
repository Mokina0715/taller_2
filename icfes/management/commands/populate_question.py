from django.core.management.base import BaseCommand
from icfes.models import Subject, Question


class Command(BaseCommand):
    help = "Popula la base de datos con preguntas de ejemplo para cada materia"

    def handle(self, *args, **options):
        questions_data = {
            "Geometria": [
                {
                    "text": "¿Cuántos lados tiene un hexágono?",
                    "option_a": "Cuatro",
                    "option_b": "Cinco",
                    "option_c": "Seis",
                    "option_d": "Siete",
                    "correct_answer": "C",
                },
                {
                    "text": "¿Cuál es la suma de los ángulos internos de un triángulo?",
                    "option_a": "180 grados",
                    "option_b": "360 grados",
                    "option_c": "90 grados",
                    "option_d": "270 grados",
                    "correct_answer": "A",
                },
                {
                    "text": "¿Cuántos vértices tiene un cubo?",
                    "option_a": "6",
                    "option_b": "8",
                    "option_c": "12",
                    "option_d": "4",
                    "correct_answer": "B",
                },
                {
                    "text": "¿Qué figura tiene todos sus lados iguales y cuatro ángulos rectos?",
                    "option_a": "Rectángulo",
                    "option_b": "Rombo",
                    "option_c": "Cuadrado",
                    "option_d": "Trapecio",
                    "correct_answer": "C",
                },
                {
                    "text": "¿Cómo se llama el segmento que une dos puntos no consecutivos de un polígono?",
                    "option_a": "Lado",
                    "option_b": "Diagonal",
                    "option_c": "Radio",
                    "option_d": "Altura",
                    "correct_answer": "B",
                },
                {
                    "text": "¿Cuál es el área de un triángulo de base 10 y altura 5?",
                    "option_a": "25",
                    "option_b": "50",
                    "option_c": "15",
                    "option_d": "30",
                    "correct_answer": "A",
                },
                {
                    "text": "¿Qué nombre recibe un polígono de ocho lados?",
                    "option_a": "Hexágono",
                    "option_b": "Octágono",
                    "option_c": "Pentágono",
                    "option_d": "Heptágono",
                    "correct_answer": "B",
                },
                {
                    "text": "¿Cuál es el perímetro de un cuadrado de lado 4?",
                    "option_a": "8",
                    "option_b": "12",
                    "option_c": "16",
                    "option_d": "20",
                    "correct_answer": "C",
                },
                {
                    "text": "¿Cómo se llama el punto donde se cortan las alturas de un triángulo?",
                    "option_a": "Baricentro",
                    "option_b": "Circuncentro",
                    "option_c": "Ortocentro",
                    "option_d": "Incentro",
                    "correct_answer": "C",
                },
                {
                    "text": "¿Qué es un radio en una circunferencia?",
                    "option_a": "La distancia entre dos puntos de la circunferencia",
                    "option_b": "La distancia del centro a un punto de la circunferencia",
                    "option_c": "La línea que une dos radios",
                    "option_d": "La mitad del diámetro",
                    "correct_answer": "B",
                },
                {
                    "text": "¿Cuántos lados tiene un dodecágono?",
                    "option_a": "10",
                    "option_b": "12",
                    "option_c": "14",
                    "option_d": "16",
                    "correct_answer": "B",
                },
            ],
            "Estadistica": [
                {
                    "text": "¿Cuál es la media de los números 2, 4 y 6?",
                    "option_a": "4",
                    "option_b": "5",
                    "option_c": "6",
                    "option_d": "3",
                    "correct_answer": "A",
                },
                {
                    "text": "¿Qué es la moda en estadística?",
                    "option_a": "El número más grande",
                    "option_b": "El número más pequeño",
                    "option_c": "El número que más se repite",
                    "option_d": "La suma de todos los números",
                    "correct_answer": "C",
                },
                {
                    "text": "¿Qué representa la mediana?",
                    "option_a": "El promedio",
                    "option_b": "El valor central",
                    "option_c": "El valor más alto",
                    "option_d": "El valor más bajo",
                    "correct_answer": "B",
                },
                {
                    "text": "¿Cómo se calcula la media aritmética?",
                    "option_a": "Multiplicando todos los valores",
                    "option_b": "Sumando y dividiendo entre la cantidad de valores",
                    "option_c": "Restando el menor al mayor",
                    "option_d": "Sumando solo los valores pares",
                    "correct_answer": "B",
                },
                {
                    "text": "¿Qué es un gráfico de barras?",
                    "option_a": "Un gráfico circular",
                    "option_b": "Un gráfico que usa líneas",
                    "option_c": "Un gráfico que usa rectángulos para comparar datos",
                    "option_d": "Un gráfico de dispersión",
                    "correct_answer": "C",
                },
                {
                    "text": "¿Qué es un dato atípico?",
                    "option_a": "Un dato que se repite mucho",
                    "option_b": "Un dato muy diferente a los demás",
                    "option_c": "El dato central",
                    "option_d": "El dato más bajo",
                    "correct_answer": "B",
                },
                {
                    "text": "¿Qué es una muestra en estadística?",
                    "option_a": "El total de la población",
                    "option_b": "Un subconjunto de la población",
                    "option_c": "El valor más alto",
                    "option_d": "El valor más bajo",
                    "correct_answer": "B",
                },
                {
                    "text": "¿Qué es la probabilidad?",
                    "option_a": "La posibilidad de que ocurra un evento",
                    "option_b": "La suma de todos los eventos",
                    "option_c": "El número de eventos posibles",
                    "option_d": "El promedio de los eventos",
                    "correct_answer": "A",
                },
                {
                    "text": "¿Qué es un gráfico circular?",
                    "option_a": "Un gráfico de barras",
                    "option_b": "Un gráfico que representa datos en sectores de un círculo",
                    "option_c": "Un gráfico de líneas",
                    "option_d": "Un gráfico de puntos",
                    "correct_answer": "B",
                },
                {
                    "text": "¿Qué es la desviación estándar?",
                    "option_a": "La diferencia entre el mayor y el menor",
                    "option_b": "Una medida de dispersión de los datos",
                    "option_c": "El valor central",
                    "option_d": "La suma de los datos",
                    "correct_answer": "B",
                },
                {
                    "text": "¿Qué es un rango en estadística?",
                    "option_a": "La diferencia entre el valor mayor y el menor",
                    "option_b": "El valor más frecuente",
                    "option_c": "El valor central",
                    "option_d": "La suma de los valores",
                    "correct_answer": "A",
                },
            ],
            "Aritmetica": [
                {
                    "text": "¿Cuánto es 7 + 5?",
                    "option_a": "10",
                    "option_b": "12",
                    "option_c": "13",
                    "option_d": "11",
                    "correct_answer": "B",
                },
                {
                    "text": "¿Cuánto es 9 - 4?",
                    "option_a": "5",
                    "option_b": "6",
                    "option_c": "4",
                    "option_d": "3",
                    "correct_answer": "A",
                },
                {
                    "text": "¿Cuánto es 6 x 3?",
                    "option_a": "18",
                    "option_b": "9",
                    "option_c": "12",
                    "option_d": "21",
                    "correct_answer": "A",
                },
                {
                    "text": "¿Cuánto es 20 ÷ 4?",
                    "option_a": "6",
                    "option_b": "5",
                    "option_c": "4",
                    "option_d": "8",
                    "correct_answer": "B",
                },
                {
                    "text": "¿Cuál es el resultado de 15 + 8?",
                    "option_a": "22",
                    "option_b": "23",
                    "option_c": "24",
                    "option_d": "25",
                    "correct_answer": "B",
                },
                {
                    "text": "¿Cuánto es 14 - 7?",
                    "option_a": "6",
                    "option_b": "7",
                    "option_c": "8",
                    "option_d": "9",
                    "correct_answer": "B",
                },
                {
                    "text": "¿Cuánto es 5 x 5?",
                    "option_a": "10",
                    "option_b": "15",
                    "option_c": "25",
                    "option_d": "20",
                    "correct_answer": "C",
                },
                {
                    "text": "¿Cuánto es 36 ÷ 6?",
                    "option_a": "5",
                    "option_b": "6",
                    "option_c": "7",
                    "option_d": "8",
                    "correct_answer": "B",
                },
                {
                    "text": "¿Cuál es el doble de 9?",
                    "option_a": "18",
                    "option_b": "16",
                    "option_c": "12",
                    "option_d": "20",
                    "correct_answer": "A",
                },
                {
                    "text": "¿Cuál es la mitad de 24?",
                    "option_a": "10",
                    "option_b": "12",
                    "option_c": "14",
                    "option_d": "16",
                    "correct_answer": "B",
                },
                {
                    "text": "¿Cuánto es 8 + 7?",
                    "option_a": "14",
                    "option_b": "15",
                    "option_c": "16",
                    "option_d": "17",
                    "correct_answer": "B",
                },
            ],
            "Algebra": [
                {
                    "text": "¿Cuál es el valor de x en la ecuación 2x = 10?",
                    "option_a": "2",
                    "option_b": "5",
                    "option_c": "10",
                    "option_d": "20",
                    "correct_answer": "B",
                }
            ],
            "Comprension Lectora": [
                {
                    "text": "¿Qué significa inferir en un texto?",
                    "option_a": "Copiar el texto",
                    "option_b": "Leer en voz alta",
                    "option_c": "Sacar conclusiones",
                    "option_d": "Buscar palabras difíciles",
                    "correct_answer": "C",
                }
            ],
            "Gramática": [
                {
                    "text": "¿Cuál es el verbo en la oración: 'El perro corre rápido'?",
                    "option_a": "perro",
                    "option_b": "corre",
                    "option_c": "rápido",
                    "option_d": "El",
                    "correct_answer": "B",
                }
            ],
            "Vocabulario": [
                {
                    "text": "¿Cuál es el sinónimo de 'feliz'?",
                    "option_a": "Triste",
                    "option_b": "Contento",
                    "option_c": "Enojado",
                    "option_d": "Cansado",
                    "correct_answer": "B",
                }
            ],
            "Análisis Literario": [
                {
                    "text": "¿Qué es una metáfora?",
                    "option_a": "Una comparación directa",
                    "option_b": "Una exageración",
                    "option_c": "Una pregunta retórica",
                    "option_d": "Una repetición",
                    "correct_answer": "A",
                }
            ],
            "Historia de la Literatura": [
                {
                    "text": "¿Quién escribió 'Cien años de soledad'?",
                    "option_a": "Pablo Neruda",
                    "option_b": "Gabriel García Márquez",
                    "option_c": "Mario Vargas Llosa",
                    "option_d": "Jorge Luis Borges",
                    "correct_answer": "B",
                }
            ],
            "Historia": [
                {
                    "text": "¿En qué año llegó Colón a América?",
                    "option_a": "1492",
                    "option_b": "1500",
                    "option_c": "1453",
                    "option_d": "1519",
                    "correct_answer": "A",
                }
            ],
            "Geografía": [
                {
                    "text": "¿Cuál es el río más largo del mundo?",
                    "option_a": "Nilo",
                    "option_b": "Amazonas",
                    "option_c": "Yangtsé",
                    "option_d": "Misisipi",
                    "correct_answer": "B",
                }
            ],
            "Cívica": [
                {
                    "text": "¿Qué es la democracia?",
                    "option_a": "Un sistema económico",
                    "option_b": "Un sistema político donde el pueblo elige",
                    "option_c": "Una religión",
                    "option_d": "Una ley",
                    "correct_answer": "B",
                }
            ],
            "Botánica": [
                {
                    "text": "¿Qué estudia la botánica?",
                    "option_a": "Los animales",
                    "option_b": "Las plantas",
                    "option_c": "Los minerales",
                    "option_d": "Los planetas",
                    "correct_answer": "B",
                }
            ],
            "Zoología": [
                {
                    "text": "¿Qué animal es un mamífero?",
                    "option_a": "Tiburón",
                    "option_b": "Gallina",
                    "option_c": "Ballena",
                    "option_d": "Cocodrilo",
                    "correct_answer": "C",
                }
            ],
            "Genética": [
                {
                    "text": "¿Qué molécula contiene la información genética?",
                    "option_a": "ADN",
                    "option_b": "ARN",
                    "option_c": "Proteína",
                    "option_d": "Lípido",
                    "correct_answer": "A",
                }
            ],
        }

        created = 0
        for subject_name, questions in questions_data.items():
            subject = Subject.objects.filter(name=subject_name).first()
            if not subject:
                self.stdout.write(
                    self.style.WARNING(f"Materia '{subject_name}' no encontrada.")
                )
                continue

            for q in questions:
                if not Question.objects.filter(
                    text=q["text"], subject=subject
                ).exists():
                    Question.objects.create(
                        text=q["text"],
                        subject=subject,
                        option_a=q["option_a"],
                        option_b=q["option_b"],
                        option_c=q["option_c"],
                        option_d=q["option_d"],
                        correct_answer=q["correct_answer"],
                    )
                    created += 1
                    self.stdout.write(
                        self.style.SUCCESS(
                            f"Pregunta creada para {subject_name}: {q['text'][:40]}..."
                        )
                    )

        self.stdout.write(self.style.SUCCESS(f"Total de preguntas creadas: {created}"))
