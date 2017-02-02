from django.db import models

# Create your models here.

class UserInfo(models.Model):

    Name = models.CharField(max_length=100, blank=True)
    Position = models.CharField(max_length=100, blank=True)
    Address = models.CharField(max_length=255, blank=True)
    Email = models.CharField(max_length=100, blank=True)
    Tel = models.CharField(max_length=100, blank=True)
    Photo = models.ImageField(blank=True, upload_to="cv_site/static/images")
    LinkedIn = models.CharField(max_length=255, blank=True)


class Education(models.Model):

    Dates = models.CharField(max_length=100, blank=True)
    Academy = models.CharField(max_length=200, blank=True)
    Degree = models.CharField(max_length=200, blank=True)


class WorkExperience(models.Model):

    Date1 = models.CharField(max_length=100, blank=True)
    Work1 = models.CharField(max_length=100, blank=True)
    Position1 = models.CharField(max_length=200, blank=True)

    Date2 = models.CharField(max_length=100, blank=True)
    Work2 = models.CharField(max_length=100, blank=True)
    Position2 = models.CharField(max_length=200, blank=True)

    Date3 = models.CharField(max_length=100, blank=True)
    Work3 = models.CharField(max_length=100, blank=True)
    Position3 = models.CharField(max_length=200, blank=True)

    Date4 = models.CharField(max_length=100, blank=True)
    Work4 = models.CharField(max_length=100, blank=True)
    Position4 = models.CharField(max_length=200, blank=True)

    Date5 = models.CharField(max_length=100, blank=True)
    Work5 = models.CharField(max_length=100, blank=True)
    Position5 = models.CharField(max_length=200, blank=True)

    Date6 = models.CharField(max_length=100, blank=True)
    Work6 = models.CharField(max_length=100, blank=True)
    Position6 = models.CharField(max_length=200, blank=True)



class Skills(models.Model):

    Skill1 = models.CharField(max_length=255, blank=True)
    Skill2 = models.CharField(max_length=255, blank=True)
    Skill3 = models.CharField(max_length=255, blank=True)
    Skill4 = models.CharField(max_length=255, blank=True)
    Skill5 = models.CharField(max_length=255, blank=True)
    Skill6 = models.CharField(max_length=255, blank=True)
    Skill7 = models.CharField(max_length=255, blank=True)
    Skill8 = models.CharField(max_length=255, blank=True)
    Skill9 = models.CharField(max_length=255, blank=True)
    Skill10 = models.CharField(max_length=255, blank=True)
    Skill11 = models.CharField(max_length=255, blank=True)
    Skill12 = models.CharField(max_length=255, blank=True)
    Skill13 = models.CharField(max_length=255, blank=True)
    Skill14 = models.CharField(max_length=255, blank=True)
    Skill15 = models.CharField(max_length=255, blank=True)
    Skill16 = models.CharField(max_length=255, blank=True)
    Skill17 = models.CharField(max_length=255, blank=True)
    Skill18 = models.CharField(max_length=255, blank=True)
    Skill19 = models.CharField(max_length=255, blank=True)
    Skill20 = models.CharField(max_length=255, blank=True)
    Skill21 = models.CharField(max_length=255, blank=True)
    Skill22 = models.CharField(max_length=255, blank=True)
    Skill23 = models.CharField(max_length=255, blank=True)
    Skill24 = models.CharField(max_length=255, blank=True)
    Skill25 = models.CharField(max_length=255, blank=True)
    Skill26 = models.CharField(max_length=255, blank=True)
    Skill27 = models.CharField(max_length=255, blank=True)
    Skill28 = models.CharField(max_length=255, blank=True)



class Languages(models.Model):

    Lang1 = models.CharField(max_length=100, blank=True)
    Lang2 = models.CharField(max_length=100, blank=True)
    Lang3 = models.CharField(max_length=100, blank=True)


class Certificates(models.Model):

    Cert1 = models.CharField(max_length=200, blank=True)
    Cert2 = models.CharField(max_length=200, blank=True)
    Cert3 = models.CharField(max_length=200, blank=True)
    Cert4 = models.CharField(max_length=200, blank=True)
    Cert5 = models.CharField(max_length=200, blank=True)
    Cert6 = models.CharField(max_length=200, blank=True)
    Cert7 = models.CharField(max_length=200, blank=True)
    Cert8 = models.CharField(max_length=200, blank=True)
    Cert9 = models.CharField(max_length=200, blank=True)
    Cert10 = models.CharField(max_length=200, blank=True)
