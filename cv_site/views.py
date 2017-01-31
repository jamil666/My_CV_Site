from django.shortcuts import render

# Create your views here.
from gmail import GMail, Message
from .models import *


def home(request):

    UserInfoTable = UserInfo.objects.get(id=1)
    EducationTable = Education.objects.get(id=1)
    WorkExperienceTable = WorkExperience.objects.get(id=1)
    SkillsTable = Skills.objects.get(id=1)
    LanguagesTable = Languages.objects.get(id=1)
    CertificatesTable = Certificates.objects.get(id=1)

    context = {'UserInfoTable': UserInfoTable,
               'EducationTable': EducationTable,
               'WorkExperienceTable': WorkExperienceTable,
               'SkillsTable': SkillsTable,
               'LanguagesTable': LanguagesTable,
               'CertificatesTable': CertificatesTable,
               }

    return render(request, 'index.html', context)


def contact(request):

    return render(request, 'contact.html')

def send_mail(request):
    if request.method == "POST":

        Name = request.POST.get("Name")
        From = request.POST.get("Email")
        message = request.POST.get("Message")

        if '@' in From:

            gmail = GMail('<PythonCVSite@gmail.com>', '123456789F!')
            msg = Message('Test Message', to='<jkarimov@azerfon.az>',
                          text='You received mail from %s \n\n Email: %s \n\n' % (Name, From) + message)
            gmail.send(msg)
            return render(request, 'contactthanks.html')
        else:
            return render(request, 'error.html')



    return render(request, 'contactthanks.html')

def error(request):
    return render(request, 'error.html')