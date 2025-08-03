from django.core.management.base import BaseCommand
from icfes.models import  Category

class Command(BaseCommand):
    def handle(self, *args, **options):
        categorias = [ "Matematicas", "Ingles", "Literatura", "Sociales", "Biologia"]

        for categoria in categorias:
            print(f'Creando la categoria {categoria}')
            sub = Category(
                name = categoria
            )
            sub.save()
        print('Se han creado las categoria exitosamente')