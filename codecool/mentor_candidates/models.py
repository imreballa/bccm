from django.db import models

class Mentor(models.Model):
    first_name = models.CharField(max_length = 128, blank = False)
    last_name = models.CharField(max_length = 128, blank = False)
    email = models.EmailField(max_length = 128, blank = False, unique = True)
    description = models.TextField(blank = True, null = True)
    def __str__(self): return '{} {}'.format(self.last_name, self.first_name)
    def full_name(self): return '{} {}'.format(self.last_name, self.first_name)
        
class Opinion(models.Model):
    mentor = models.ForeignKey(Mentor)
    name = models.CharField(max_length = 256, blank = False)
    description = models.TextField(blank = False)
    def __str__(self): return '{} about {}'.format(self.name, self.mentor)

