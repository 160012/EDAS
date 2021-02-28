from .models import Cadres, Teacher, Curriculum
from django.contrib import admin


@admin.register(Cadres)
class CadresAdmin(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):
        if change:
            user = request.user.username
            name = self.model.objects.get(pk=obj.pk).name
            # person = form.cleaned_data['person'].name
            f = open('e://jiaowuxitong.txt', 'a')
            # f.write(person+'职位:'+job+',被'+user+'修改'+'\r\n')
            f.write('学生干部,干部:'+name+'被'+user+'修改'+'\r\n')
            f.close()
        else:
            pass
        super().save_model(request, obj, form, change)

    fieldsets = (
        ('个人信息', {
            'fields': ('c_id', 'name', 'sex', 'position', 'phone', 'QQ')
        }),)

    # 只读字段
    readonly_fields = ['c_id', ]

    # 默认排序字段
    ordering = ['c_id']

    # 可选排序字段
    sortable_by = ['c_id', 'sex']

    # 列表页展示字段
    list_display = ['c_id', 'name', 'sex', 'position', 'phone', 'QQ']

    # 设置路由地址
    list_display_links = ['c_id', 'name']

    # 设置过滤器
    list_filter = ['sex']

    # 设置每页展示数据量
    list_per_page = 10

    # 设置可搜索字段
    search_fields = ['name', 'position']


admin.site.site_title = '教务系统（极简）'
admin.site.site_header = '18级网络工程2班'


@admin.register(Curriculum)
class CurriculumAdmin(admin.ModelAdmin):

    # 修改页展示字段
    fieldsets = (
        ('课程信息', {
            'fields': ("name", "teacher", "all_time", "theoretical_time",
                       "practice_time", "score", "category", "method",
                       "assessment", "week_time", "time", "place"),
        }),
    )

    # 列表页可排序字段
    # sortable_by = ['score', 'category', 'assessment', 'all_time', 'score', 'category', 'name']

    # 列表页展示字段
    list_display = ['name', 'teacher', 'all_time', 'theoretical_time', 'practice_time',
                    'score', 'category', 'method', 'assessment', 'week_time', 'time', 'place']

    # 设置过滤字段
    list_filter = ['category', 'assessment', 'method']

    # 设置每页显示数据量
    list_per_page = 10

    # 设置搜索字段
    search_fields = ['name', 'teacher', 'place']



@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    fieldsets = (
        ('个人信息', {
            'fields': ('id', 'name', 'sex', 'phone', 'subject')
        })
        ,
    )
    # 只读字段
    readonly_fields = ['id',]
    # 默认排序字段
    ordering = ['id']
    # 列表页展示字段
    list_display = ['id', 'name', 'subject', 'phone']
    # 设置路由地址
    list_display_links = ['id', 'name']
    # 设置每页展示数据量
    list_per_page = 10
    # 设置可搜索字段
    search_fields = ['name', 'subject', 'phone']

