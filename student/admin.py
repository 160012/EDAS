from django.contrib import admin
from .models import Student
from django.contrib.auth.admin import UserAdmin


@admin.register(Student)
class StudentAdmin(UserAdmin):

    def save_model(self, request, obj, form, change):
        if change:
            user = request.user.username
            name = self.model.objects.get(pk=obj.pk).name
            # person = form.cleaned_data['person'].name
            f = open('/data/wwwroot/jiaowuxitong.txt', 'a')
            # f.write(person+'职位:'+job+',被'+user+'修改'+'\r\n')
            f.write('学生信息,学生:'+name+'被'+user+'修改'+'\r\n')
            f.close()
        else:
            pass
        super().save_model(request, obj, form, change)

    # 列表页展示字段
    list_display = ['id', 'username', 'colored_name', 'sex',
                    'phone', 'qq', 'dor', ]
    # # 将源码的UserAdmin转换成列表格式
    # fieldsets = list(UserAdmin.fieldsets)
    fieldsets = [('学生信息',
                  {'fields': ('username', 'password', 'name', 'sex', 'phone',
                              'qq', 'dor',)}),
                 ('学生权限',
                  {'classes': ('collapse',),
                   'fields': ('is_superuser', 'is_staff',
                              'is_active', 'groups', 'user_permissions')}),
                 ]
    # 设置排序方式
    ordering = ['id']
    # 为字段设置路由地址
    list_display_links = ['id', 'username', 'colored_name']
    # 设置过滤器
    list_filter = ['sex', 'dor']
    # 设置每页展示数据量
    list_per_page = 10
    # 设置可搜索字段
    search_fields = ['username', 'colored_name', 'qq', 'phone']

    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            self.readonly_fields = []

        else:
            self.readonly_fields = ['username', 'password', 'is_staff', 'is_active', 'is_superuser',
                                    'groups', 'user_permissions']
        return self.readonly_fields
