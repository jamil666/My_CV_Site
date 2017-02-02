from django.contrib import admin
from .models import *
# Register your models here.

class AdminUserInfo(admin.ModelAdmin):

    search_fields = ('Name', 'Position', 'Address', 'Email', 'Tel', 'Photo', 'LinkedIn')

    list_display = ('Name', 'Position', 'Address', 'Email', 'Tel', 'Photo', 'LinkedIn')

admin.site.register(UserInfo, AdminUserInfo)


class AdminEducation(admin.ModelAdmin):
    search_fields = ('Dates', 'Academy', 'Degree')

    list_display = ('Dates', 'Academy', 'Degree')


admin.site.register(Education, AdminEducation)


class AdminWorkExperience(admin.ModelAdmin):

    fieldsets = (

        ('Work1', {'fields':
                        ('Date1',
                        'Work1',
                        'Position1')}),
        ('Work2', {'fields':
                       ('Date2',
                        'Work2',
                        'Position2')}),
        ('Work3', {'fields':
                       ('Date3',
                        'Work3',
                        'Position3')}),

        ('Work4', {'fields':
                       ('Date4',
                        'Work4',
                        'Position4')}),
    )

    search_fields = ('Date1',
                     'Work1',
                     'Position1',
                     'Date2',
                     'Work2',
                     'Position2',
                     'Date3',
                     'Work3',
                     'Position3',
                     'Date4',
                     'Work4',
                     'Position4'
                     )

    list_display = ('Date1',
                     'Work1',
                     'Position1',
                     'Date2',
                     'Work2',
                     'Position2',
                     'Date3',
                     'Work3',
                     'Position3',
                     'Date4',
                     'Work4',
                     'Position4'
                     )

admin.site.register(WorkExperience, AdminWorkExperience)


class AdminSkills(admin.ModelAdmin):

    search_fields = ('Skill1',
                     'Skill2',
                     'Skill3',
                     'Skill4',
                     'Skill5',
                     'Skill6',
                     'Skill7',
                     'Skill8',
                     'Skill9',
                     'Skill10',
                     'Skill11',
                     'Skill12',
                     'Skill13',
                     'Skill14',
                     'Skill15',
                     'Skill16',
                     'Skill17',
                     'Skill18',
                     'Skill19',
                     'Skill20',
                     'Skill21',
                     'Skill22',
                     'Skill23',
                     )

    list_display = ('Skill1',
                     'Skill2',
                     'Skill3',
                     'Skill4',
                     'Skill5',
                     'Skill6',
                     'Skill7',
                     'Skill8',
                     'Skill9',
                     'Skill10',
                     'Skill11',
                     'Skill12',
                     'Skill13',
                     'Skill14',
                     'Skill15',
                     'Skill16',
                     'Skill17',
                     'Skill18',
                     'Skill19',
                     'Skill20',
                     'Skill21',
                     'Skill22',
                     'Skill23',
                     )

admin.site.register(Skills, AdminSkills)


class AdminLanguages(admin.ModelAdmin):

    search_fields = ('Lang1', 'Lang2', 'Lang3')

    list_display = ('Lang1', 'Lang2', 'Lang3')

admin.site.register(Languages, AdminLanguages)


class AdminCertificates(admin.ModelAdmin):

    search_fields = ('Cert1',
                     'Cert2',
                     'Cert3',
                     'Cert4',
                     'Cert5',
                     'Cert6',
                     'Cert7',
                     'Cert8',
                     )

    list_display = ('Cert1',
                     'Cert2',
                     'Cert3',
                     'Cert4',
                     'Cert5',
                     'Cert6',
                     'Cert7',
                     'Cert8',
                     )

admin.site.register(Certificates, AdminCertificates)
