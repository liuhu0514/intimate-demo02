from django.contrib import admin
from .models import Problem, Option

# Register your models here.


class OptionInline(admin.StackedInline):
    model = Option
    extra = 2


class OptionAdmin(admin.ModelAdmin):
    list_display = ['name', 'frequency', 'pro']
    list_filter = ['oname']
    search_fields = ['oname']
    list_per_page = 5


class ProblemAdmin(admin.ModelAdmin):
    # 显示字段
    list_display = ['name', 'frequency']
    # 过滤字段
    list_filter = ['pname', 'pfrequency']
    # 搜索字段
    search_fields = ['pname']
    # 分页
    list_per_page = 5
    # 级联创建
    inlines = [OptionInline]


# 注册模型到管理界面
admin.site.register(Problem, ProblemAdmin)
admin.site.register(Option, OptionAdmin)
