from django.db import models

##################################
# Resume Content Models
##################################

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
    start_date = models.DateField()
    end_date = models.DateField()
    detail = models.TextField()
    job_type = models.CharField(max_length=200)

    def __unicode__(self):
        return self.title

class Affiliation(models.Model): 
    title = models.CharField(max_length=200)
    period = models.CharField(max_length=200)

    def __unicode__(self):
        return self.title

##################################
# Contact & Supervisor Content Model
##################################
        
class Contact(models.Model): 
    title_contact = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    title_research = models.CharField(max_length=200)
    research_interest = models.TextField(max_length=200)

    def __unicode__(self):
        return self.title_contact

# supervisor related model starts here
class Supervisor(models.Model): 
    contact = models.ForeignKey(Contact)
    name = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    email = models.CharField(max_length=200)
    field = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    university = models.CharField(max_length=200)
    image_path = models.CharField(max_length=200)
    link = models.CharField(max_length=200)
    research_interest = models.TextField(max_length=200)

    def __unicode__(self):
        return self.name

class Supervisor_Affiliation(models.Model):
    supervisor = models.ForeignKey(Supervisor)
    title = models.CharField(max_length=200, default="none")
    def __unicode__(self):
        return self.title

class Supervisor_Department(models.Model):
    supervisor = models.ForeignKey(Supervisor)
    title = models.CharField(max_length=200, default="none")
    def __unicode__(self):
        return self.title

class Supervisor_Famous_paper(models.Model):
    supervisor = models.ForeignKey(Supervisor)
    title = models.CharField(max_length=200, default="none")
    author = models.CharField(max_length=200, default="none")
    conference = models.CharField(max_length=200, default="none")
    def __unicode__(self):
        return self.title
