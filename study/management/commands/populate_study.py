from django.core.management.base import BaseCommand
from study.models import Subtopic, StudyMaterial
from icfes.models import Category, Subject

class Command(BaseCommand):
    help = "Puebla la base de datos con materias, subtemas y materiales de estudio"

    def handle(self, *args, **kwargs):
        # Limpiar datos anteriores
        StudyMaterial.objects.all().delete()
        Subtopic.objects.all().delete()
        Subject.objects.all().delete()
        Category.objects.all().delete()

        # Crear categorías
        math_category = Category.objects.create(name='Matemáticas')
        reading_category = Category.objects.create(name='Lectura Crítica')
        science_category = Category.objects.create(name='Ciencias Naturales')

        # Crear materias (Subjects) asociadas a las categorías
        mat = Subject.objects.create(name='Matemáticas', category=math_category)
        lec = Subject.objects.create(name='Lectura Crítica', category=reading_category)
        cie = Subject.objects.create(name='Ciencias Naturales', category=science_category)

        # Crear subtemas
        arit = Subtopic.objects.create(name='Aritmética', subject=mat)
        alg = Subtopic.objects.create(name='Álgebra', subject=mat)
        comp = Subtopic.objects.create(name='Comprensión textual', subject=lec)
        arg = Subtopic.objects.create(name='Análisis argumentativo', subject=lec)
        bio = Subtopic.objects.create(name='Biología', subject=cie)
        fis = Subtopic.objects.create(name='Física', subject=cie)

        # Materiales de Matemáticas
        StudyMaterial.objects.create(
            title='Sumas y restas básicas',
            description='Video sobre operaciones básicas',
            explanation='Explica con ejemplos cómo sumar y restar.',
            link='https://www.youtube.com/watch?v=video_suma',
            resource_type='video',
            subtopic=arit
        )
        StudyMaterial.objects.create(
            title='Problemas con fracciones',
            explanation='Problemas aplicados con fracciones.',
            link='https://es.khanacademy.org/math/arithmetic/fraction-arithmetic',
            resource_type='web',
            subtopic=arit
        )
        StudyMaterial.objects.create(
            title='Introducción al Álgebra',
            explanation='Curso básico de álgebra.',
            link='https://www.youtube.com/watch?v=video_algebra',
            resource_type='video',
            subtopic=alg
        )
        StudyMaterial.objects.create(
            title='Ecuaciones lineales',
            explanation='Material interactivo para resolver ecuaciones.',
            link='https://www.mundoprimaria.com/juegos-matematicas/ecuaciones',
            resource_type='web',
            subtopic=alg
        )

        # Materiales de Lectura Crítica
        StudyMaterial.objects.create(
            title='Cómo mejorar la comprensión lectora',
            explanation='Técnicas de lectura activa.',
            link='https://www.youtube.com/watch?v=comprension_video',
            resource_type='video',
            subtopic=comp
        )
        StudyMaterial.objects.create(
            title='Ejercicios de lectura crítica',
            explanation='Ejercicios prácticos tipo ICFES.',
            link='https://www.leercritico.com/ejercicios',
            resource_type='web',
            subtopic=comp
        )
        StudyMaterial.objects.create(
            title='Identificación de argumentos',
            explanation='Explicación con ejemplos de argumentos y falacias.',
            link='https://www.youtube.com/watch?v=argumentos_video',
            resource_type='video',
            subtopic=arg
        )
        StudyMaterial.objects.create(
            title='Ejercicios de lógica informal',
            explanation='Material para practicar inferencias.',
            link='https://lógica-informal.org/ejercicios',
            resource_type='web',
            subtopic=arg
        )

        # Materiales de Ciencias Naturales
        StudyMaterial.objects.create(
            title='Célula: estructura y funciones',
            explanation='Video explicativo sobre las partes de la célula.',
            link='https://www.youtube.com/watch?v=celula_bio',
            resource_type='video',
            subtopic=bio
        )
        StudyMaterial.objects.create(
            title='ADN y herencia',
            explanation='Artículo sobre genética básica.',
            link='https://geneticaescolar.com/adn',
            resource_type='web',
            subtopic=bio
        )
        StudyMaterial.objects.create(
            title='Las leyes de Newton',
            explanation='Explicación con ejemplos animados.',
            link='https://www.youtube.com/watch?v=newton_fisica',
            resource_type='video',
            subtopic=fis
        )
        StudyMaterial.objects.create(
            title='Velocidad y aceleración',
            explanation='Página con ejemplos interactivos.',
            link='https://fisicainteractiva.com/velocidad',
            resource_type='web',
            subtopic=fis
        )

        self.stdout.write(self.style.SUCCESS('✔ Base de datos de materiales poblada correctamente.'))
