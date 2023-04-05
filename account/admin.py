from django.contrib import admin
from .models import *
from django.contrib.auth.models import Group

admin.site.unregister(Group)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ["user", "ism", "familya", 'phone', "school", "clas" ]
    list_filter = ['clas']
    search_fields = ['', 'phone']
    list_editable = ['clas']
    actions = ['export_to_json']

    def ism(self, obj):
        if obj.user and obj.user.first_name:
            return obj.user.first_name
        return '-'

    def familya(self, obj):
        if obj.user and obj.user.last_name:
            return obj.user.last_name
        return '-'

    def export_to_json(self, request, queryset):
        import json
        from django.http import HttpResponse

        response = HttpResponse(content_type='application/json')
        response['Content-Disposition'] = 'attachment; filename="students.json"'

        data = []

        for obj in queryset:
            data.append({
                "id" : obj.id,
                "username" : obj.user.username,
                "first_name" : obj.user.first_name,
                "last_name" : obj.user.last_name,
                "phone" : obj.phone,
            })

        json.dump(data, response, ensure_ascii=True, indent=4)
        return response

admin.site.register(School)

@admin.register(Administrator)
class StudentAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", 'phone']
    search_fields = ['phone']

    def first_name(self, obj):
        if obj.user and obj.user.first_name:
            return obj.user.first_name

    def last_name(self, obj):
        if obj.user and obj.user.last_name:
            return obj.user.last_name


