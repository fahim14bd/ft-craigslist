from django.db import models

# Create your models here.
class Search(models.Model):
  search  = models.CharField(max_length=500)
  created = models.DateTimeField(auto_now=True)

  class Meta:
    ordering = ['-created',]

  def __str__(self):
    return self.search

  def __unicode__(self):
    return self.search