import csv
from django.core.management import BaseCommand
from function.models import Teacher

# python manage.py import_students --path

class Command(BaseCommand):
    help = '从一个CSV文件的内容中读取候选人列表，导入到数据库中'

    def add_arguments(self, parser):
        parser.add_argument('--path', type=str)

    def handle(self, *args, **kwargs):
        path = kwargs['path']
        with open(path, 'rt', encoding='utf-8') as f:
            reader = csv.reader(f, dialect='excel')
            for row in reader:
                teacher = Teacher.objects.create(
                    name=row[0],
                    sex=row[1],
                    subject=row[2],
                    phone=row[3],
                )
