from django.core.management import BaseCommand

from main.models import Student


class Command(BaseCommand):

    def handle(self, *args, **options):
        student_list = [
            {'first_name': 'Oleg', 'last_name': 'Maslov'},
            {'first_name': 'Alexey', 'last_name': 'Markov'},
            {'first_name': 'Anna', 'last_name': 'Udina'},
        ]

        student_obj = []
        for i in student_list:
            student_obj.append(Student(**i))

        Student.objects.bulk_create(student_obj)