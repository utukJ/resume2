from django.db import models
from django import forms


# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=100, blank=True)
    email = models.EmailField()
    mobile_num = models.CharField(max_length=11, blank=True)
    message = models.TextField()

    def __str__(self):
        return self.message[:50] + " by " + self.email

class ContactForm(forms.ModelForm):
    class Meta: 
        model = Contact
        fields = ["name", "email", "mobile_num", "message"]



    