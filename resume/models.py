from django.db import models

class Education (models.Model):
    title = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    program = models.CharField(max_length=200)
    duration = models.CharField(max_length=200)
    skills_programming_languages = models.TextField()
    skills_design_tools = models.TextField()
    
    def __unicode__(self):
        return self.title

class Job(models.Model): 
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    period = models.CharField(max_length=200)
    detail = models.TextField()
    job_type = models.CharField(max_length=200)

    def __unicode__(self):
        return self.title

class Affiliation(models.Model): 
    title = models.CharField(max_length=200)
    period = models.CharField(max_length=200)

    def __unicode__(self):
        return self.title

        
class Contact(models.Model): 
    title_contact = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    title_research = models.CharField(max_length=200)
    research_interest = models.TextField(max_length=200)

    def __unicode__(self):
        return self.title_contact

class Images(models.Model): 
    Contact = models.ForeignKey(Contact)
    title = models.CharField(max_length=200)
    image_name = models.CharField(max_length=200)
    link = models.CharField(max_length=200)
    
    def __unicode__(self):
        return self.title
