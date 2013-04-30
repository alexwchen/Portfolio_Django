from django.db import models

class Project(models.Model):
    
    title = models.CharField(max_length=200)
    authors = models.CharField(max_length=200)
    complete_date = models.DateField()

    short_description = models.TextField()
    tags = models.CharField(max_length=200)
    link= models.CharField(max_length=200)
    rank_img = models.CharField(max_length=200)
    vote_up = models.IntegerField()
    base_vote = models.IntegerField()
        
    PDF = models.CharField(max_length=200)
    video_url = models.CharField(max_length=200)
    motivation_content = models.TextField() 
    motivation_image = models.CharField(max_length=200)
    def __unicode__(self):
        return self.title

class Feature(models.Model):
    
    project = models.ForeignKey(Project)
    feature_title = models.CharField(max_length=200)
    feature_content = models.TextField()
    feature_image = models.CharField(max_length=200)
    display_choice = models.IntegerField()
    feature_order = models.IntegerField()
    def __unicode__(self):
        return self.feature_title

class Project_Type(models.Model):
    
    project = models.ForeignKey(Project)
    project_type = models.CharField(max_length=200)

    def __unicode__(self):
        return self.project_type


