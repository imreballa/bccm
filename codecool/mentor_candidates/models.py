from django.db import models

class Mentor(models.Model):
    first_name = models.CharField(max_length = 128, blank = False)
    last_name = models.CharField(max_length = 128, blank = False)
    email = models.EmailField(max_length = 128, blank = False, unique = True)
    description = models.TextField(blank = True, null = True)
    
class Opinion(models.Model):
    mentor = models.ForeignKey(Mentor)
    name = models.CharField(max_length = 256, blank = False)
    description = models.TextField(blank = False)

