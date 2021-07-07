from django.shortcuts import render
from .models import skills,overview,Education,Acheivements,projects,FilesAdmin
from .models import certifications
from django.core.mail import send_mail
from django.http import HttpResponse


# Create your views here.
def home(request):
    
    data=skills.objects.all()
    overviews=overview.objects.all()
    education=Education.objects.all()
    Achievements=Acheivements.objects.all()
    Certifications=certifications.objects.all()
    Projects=projects.objects.all()
    f=FilesAdmin.objects.all()
   
    dir={'overviews':overviews,'data':data,'education':education,'achievements': Achievements,'Certifications':Certifications,'projects':Projects,'File':f}
   
    return render(request,'index.html',dir)

def contact(request):
    if request.method=='POST':
        contactName=request.POST['contactName']
        contactEmail=request.POST['contactEmail']
        contactSubject=request.POST['contactSubject']
        contactMessage=request.POST['contactMessage']
        
        send_mail(
             contactEmail, #subject of mail
            contactMessage, #message
            contactEmail,  #mail
            ['sreehariputhiyedath@gmail.com'], #to mail

            )
        return render(request,'index.html',{'c':contactName})
    else:
        return render(request,'index.html')

def download(request,path):
    file_path=os.path.join(settings.MEDIA_ROOT,path)
    if os.path.exists(file_path):
        with open(file_path,'rb')as fh:
            response=HttpResponse(fh.read(),content_type="application/adminupload")
            response['content-disdposition']='inline;filename='+os.path.basename(file_path)
            return response
    raise Http404