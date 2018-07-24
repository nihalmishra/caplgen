from django.db import models
from django.forms import ModelForm
from django.utils import timezone

CHOICES = (
    ('capl','CAPL'),
    ('capl-xml', 'CAPL-XML'),
)

class Upload(models.Model):
	xlfile = models.FileField(upload_to="files/")    
	upload_date = models.DateTimeField(auto_now_add=True)
	sheet_name = models.CharField(max_length=40, default='')
	option = models.CharField(max_length=8, choices=CHOICES, default='capl-xml')

	def __str__(self):
		return (str(self.xlfile) + " " + str(timezone.now()))

# FileUpload form class.
class UploadForm(ModelForm):
	class Meta:
		model = Upload
		fields = ('xlfile', 'sheet_name', 'option')