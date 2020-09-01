from django.shortcuts import render



from profiles.models import bdata
# ,ProfileImage


def matrimony_home(request):
	obj = bdata.objects.all()
	
	return render(request,'matrimony_home.html', {'prof':obj})
	## this will list all the profiles

def matrimony_detail(request,slug):
	objs = bdata.objects.filter(slug=slug).first()
	images = ProfileImage.objects.filter(profs=objs)

	return render(request,'matrimony_detail.html', {'profs':objs, 'images':images})

# Create your views here.
