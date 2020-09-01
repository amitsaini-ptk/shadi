from django.db import models
from django.template.defaultfilters import slugify


GENDER_CHOICES = (('Male', 'Male'),('Female', 'Female') )

STATE_CHOICES=(('Andhra Pradesh', 'Andhra Pradesh'),('Arunachal Pradesh', 'Arunachal Pradesh'),('Assam', 'Assam'),('Bihar', 'Bihar'),('Chandigarh', 'Chandigarh'),('Chhattisgarh', 'Chhattisgarh'),('Delhi', 'Delhi'),('Goa','Goa'),('Gujarat','Gujarat'),('Haryana','Haryana'),('Himachal Pradesh', 'Himachal Pradesh'),('Jammu & Kashmir', 'Jammu & Kashmir'),('Jharkhand', 'Jharkhand'),('Karnataka', 'Karnataka'),('Kerala', 'Kerala'),('Madhya Pradesh', 'Madhya Pradesh'),('Maharashtra', 'Maharashtra'),('Manipur','Manipur'),('Meghalaya','Meghalaya'),('Mizoram','Mizoram'),('Nagaland','Nagaland'),('Orissa', 'Orissa'),('Puducherry','Puducherry'),('Punjab','Punjab'),('Rajasthan','Rajasthan'),('Sikkim','Sikkim'),('Uttar Pradesh','Uttar Pradesh'),('Tamil Naidu','Tamil Naidu'),('Uttarakhand','Uttarakhand'))

class bdata(models.Model):
	name = models.CharField(max_length=250)
	slug = models.SlugField(max_length = 250, null = True, blank = True) 
	pic= models.ImageField(upload_to ='media/pics/')
	age = models.IntegerField(default=0)
	gender = models.CharField(choices=GENDER_CHOICES,max_length=100)
	education = models.CharField(max_length=100)
	job = models.CharField(max_length=100)
	city = models.CharField(max_length=100)
	state = models.CharField(choices=STATE_CHOICES,max_length=250)
	about= models.TextField(default=0)
	mobno=models.IntegerField(default=0)

def save(self, *args, **kwargs):
	super(bdata, self).save(*args, **kwargs)
	self.slug = slugify(self.name+'-'+str(self.pk))
	super(bdata, self).save(*args, **kwargs)


def __str__(self):
		return self.name

class ProfileImage(models.Model):
	profs = models.ForeignKey(bdata, on_delete=models.SET_NULL, null=True, blank=True)
	img = models.ImageField(upload_to='Profile_image')

