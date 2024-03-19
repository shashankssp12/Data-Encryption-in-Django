from django.db import models
from encrypted_model_fields.fields import EncryptedCharField

# Create your models here.
class PII(models.Model):
    first_name = EncryptedCharField(max_length= 50, null= False)
    last_name = EncryptedCharField(max_length=50, null=False)
    # for showing up with name in console
    def __str__(self)->str:
         return self.first_name
     
    #Use this command :pip install django-encrypted-model-fields
