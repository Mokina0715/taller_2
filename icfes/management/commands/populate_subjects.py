from django.core.management.base import BaseCommand
from icfes.models import Subject, Category

class Command(BaseCommand):
    def handle(self, *args, **options):
        print('Hola mundo')

        subjects = {
            "Matematicas": ["Geometria", "Estadistica", "Aritmetica", "Algebra"],
            "Ingles": ["Comprension Lectora", "Gramática", "Vocabulario"],
            "Literatura": ["Análisis Literario", "Historia de la Literatura"],
            "Sociales": ["Historia", "Geografía", "Cívica"],
            "Biologia": ["Botánica", "Zoología", "Genética"]
        }

        for category_name, subjects in subjects.items():
            category = Category.objects.filter(name=category_name).first()
            if not category:
                print(f'Categoria {category_name} no encontrada, creando una nueva.')
                category = Category(name=category_name)
                category.save()

            for subjec in subjects:
                print(f'Creando la materia {subjec}')
                if not Subject.objects.filter(name=subjec, category=category).exists():
                    print(f'Creando la materia {subjec} bajo la categoria {category_name}')
                    sub = Subject(
                        name=subjec,
                        category=category
                    )
                    sub.save()
        print('Se han creado las materias exitosamente')