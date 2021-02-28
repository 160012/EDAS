import csv
from django.core.management import BaseCommand
from student.models import Student

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
                student = Student.objects.create(
                    is_active=1,
                    is_staff=1,
                    is_superuser=0,
                    username=row[0],
                    name=row[1],
                    sex=row[2],
                    phone=row[3],
                    qq=row[4],
                    dor=row[5]
                )
