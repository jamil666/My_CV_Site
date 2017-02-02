from django.contrib import admin
from .models import *
# Register your models here.

class AdminUserInfo(admin.ModelAdmin):

    search_fields = ('Name', 'Position', 'Address', 'Email', 'Tel', 'Photo', 'LinkedIn')

    list_display = ('Name', 'Position', 'Address', 'Email', 'Tel', 'Photo', 'LinkedIn')

admin.site.register(UserInfo, AdminUserInfo)


class AdminEducation(admin.ModelAdmin):
    fieldsets = (

        ('Education1', {'fields':
                       ('Date1',
                        'Academy1',
                        'Degree1')}),
        ('Education2', {'fields':
                       ('Date2',
                        'Academy2',
                        'Degree2')}),

    )


    search_fields = ('Date1', 'Academy1', 'Degree1', 'Date2', 'Academy2', 'Degree2')

    list_display = ('Date1', 'Academy1', 'Degree1', 'Date2', 'Academy2', 'Degree2')


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

        ('Work5', {'fields':
                       ('Date5',
                        'Work5',
                        'Position5')}),

        ('Work6', {'fields':
                       ('Date6',
                        'Work6',
                        'Position6')}),
    )

    search_fields = ('Date1', 'Work1', 'Position1',
                     'Date2', 'Work2', 'Position2',
                     'Date3', 'Work3', 'Position3',
                     'Date4', 'Work4', 'Position4',
                     'Date5', 'Work5', 'Position5',
                     'Date6', 'Work6', 'Position6'
                     )

    list_display = ('Date1', 'Work1', 'Position1',
                     'Date2', 'Work2', 'Position2',
                     'Date3', 'Work3', 'Position3',
                     'Date4', 'Work4', 'Position4',
                     'Date5', 'Work5', 'Position5',
                     'Date6', 'Work6', 'Position6'
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
                     'Skill24',
                     'Skill25',
                     'Skill26',
                     'Skill27',
                     'Skill28',
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
                     'Skill24',
                     'Skill25',
                     'Skill26',
                     'Skill27',
                     'Skill28',
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
                     'Cert9',
                     'Cert10',
                     )

    list_display = ('Cert1',
                     'Cert2',
                     'Cert3',
                     'Cert4',
                     'Cert5',
                     'Cert6',
                     'Cert7',
                     'Cert8',
                     'Cert9',
                     'Cert10',
                     )

admin.site.register(Certificates, AdminCertificates)
