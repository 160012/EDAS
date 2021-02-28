from django.db import models

sex_field = [
    ('男', '男'),
    ('女', '女'),
]


class Cadres(models.Model):
    c_id = models.AutoField(primary_key=True, verbose_name='ID')
    sex = models.CharField(max_length=10, choices=sex_field, verbose_name='性别')
    name = models.CharField(max_length=20, verbose_name='姓名')
    position = models.CharField(max_length=20, verbose_name='职务')
    phone = models.CharField(max_length=20, verbose_name='联系方式')
    QQ = models.CharField(max_length=20, verbose_name='QQ')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '班级干部'
        verbose_name_plural = '班级干部'


class Teacher(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=10, verbose_name='姓名')
    sex = models.CharField(max_length=20, choices=sex_field, default='男', verbose_name='性别')
    phone = models.CharField(max_length=20, verbose_name='联系方式')
    subject = models.CharField(max_length=20, verbose_name='科目')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '教师信息'
        verbose_name_plural = '教师信息'


category_fields = [
    ('专业课、任选课', '专业课、任选课'),
    ('专业课、必修课', '专业课、必修课'),
    ('专业课、限选课', '专业课、限选课'),
    ('公共课、必修课', '公共课、必修课'),
    ('公共课、任选课', '公共课、任选课'),
]

assessment = [
    ('过程考核', '过程考核'),
    ('闭卷', '闭卷'),
]

method_fields = [
    ('理论', '理论'),
    ('上机', '上机'),
]

class Curriculum(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, unique=None, verbose_name='课程名')
    score = models.CharField(max_length=10, verbose_name='学分')
    all_time = models.IntegerField(verbose_name='总学时')
    theoretical_time = models.IntegerField(verbose_name='理论学时')
    practice_time = models.IntegerField(verbose_name='实践学时')
    category = models.CharField(max_length=20, choices=category_fields, verbose_name='类别')
    method = models.CharField(max_length=20, choices=method_fields, default='理论', verbose_name='授课方式')
    assessment = models.CharField(max_length=20, choices=assessment, verbose_name='考核方式')
    teacher = models.CharField(max_length=20, default=None, verbose_name='任课教师')
    week_time = models.CharField(max_length=20, verbose_name='周次')
    time = models.CharField(max_length=20, verbose_name='上课时间')
    place = models.CharField(max_length=20, verbose_name='上课地点')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '课程信息'
        verbose_name_plural = '课程信息'







