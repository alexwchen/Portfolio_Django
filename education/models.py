from django.db import models

class Material(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField(max_length=200)
    description = models.TextField()
    source_url = models.CharField(max_length=200)  
    image_url = models.CharField(max_length=200)
    def __unicode__(self):
        return self.title

class Material_Type(models.Model):
    material = models.ForeignKey(Material)
    material_type = models.CharField(max_length=200)
    def __unicode__(self):
        return self.material_type
