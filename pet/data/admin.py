from django.contrib import admin
from .models import City, Sight, Author, AuthorSightRelation, Review

# Register your models here.


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'name', 'gender')


class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class SightAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'city')


admin.site.register(AuthorSightRelation)
admin.site.register(Author, AuthorAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Sight, SightAdmin)
admin.site.register(Review)


