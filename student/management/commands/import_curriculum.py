import csv
from django.core.management import BaseCommand
from function.models import Curriculum

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
                curriculum = Curriculum.objects.create(
                    name=row[0],
                    teacher=row[1],
                    all_time=row[2],
                    theoretical_time=row[3],
                    practice_time=row[4],
                    score=row[5],
                    category=row[6],
                    method=row[7],
                    assessment=row[8],
                    week_time=row[9],
                    time=row[10],
                    place=row[11]
                )
