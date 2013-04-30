import sys,os
from datetime import *
sys.path.append('/Users/alexwchen/Desktop/')
os.environ['DJANGO_SETTINGS_MODULE'] ='portfolio.settings'

from django.core.management import setup_environ
from portfolio import settings
setup_environ(settings)

sys.path.append('/Users/alexwchen/Desktop/portfolio')
from portfolio.rankProj.models import Project, Feature

allProj = Project.objects.all()
allFeature = Feature.objects.all()
f_store = open('projdb.xml', 'w')

for project in allProj:
	p_title = '\t' + '<p_title>' + str(project.title) + '</p_title>' +'\n'
	p_authors = '\t' + '<authors>' + str(project.authors) + '</authors>' + '\n'
	p_date = '\t' + '<date>' + str(project.complete_date) + '</date>' + '\n'
	p_vid = '\t' + '<vid_url>' + str(project.video_url) + '</vid_url>' + '\n'
	p_pdf = '\t' + '<pdf>' + str(project.PDF) + '</pdf>' + '\n'
	p_voteup = '\t' + '<vote_up>' + str(project.vote_up) + '</vote_up>' + '\n'
	p_votedown = '\t' + '<vote_down>' + str(project.vote_down) + '</vote_down>' + '\n'
	p_proj_type = '\t' + '<proj_type>' + str(project.proj_type) + '</proj_type>' + '\n'
	p_tags = '\t' + '<tags>' + str(project.tags) + '</tags>' + '\n'
	p_mcontent = '\t' + '<p_content>\n\t' + str(project.motivation_content) + '\n</p_content>' + '\n'
	p_mimage = '\t' + '<p_img>' + str(project.motivation_image) + '</p_img>' + '\n'
	p_id = '\t' + '<id>' + str(project.id) + '</id>' + '\n'
	p_start = '<project>' + '\n'
	p_close = '</project>' + '\n'
	f_start =  '\t' + '<feature>' + '\n'
	f_close =  '\t' + '</feature>' + '\n'

	print p_start
	print p_title
	print p_authors
	print p_date
	print p_vid
	print p_pdf
	print p_voteup
	print p_votedown
	print p_proj_type
	print p_tags
	print p_mcontent 
	print p_mimage
	print p_id

	f_store.write(p_start)
	f_store.write(p_title)
	f_store.write(p_authors)
	f_store.write(p_date)
	f_store.write(p_vid)
	f_store.write(p_pdf)
	f_store.write(p_voteup)
	f_store.write(p_votedown)
	f_store.write(p_proj_type)
	f_store.write(p_tags)
	f_store.write(p_mcontent)
	f_store.write(p_mimage)
	f_store.write(p_id)


	for features in allFeature:	
		if (str(features.project)==str(project.title)):
			f_title = '\t\t' + '<title>' + str(features.feature_title) + '</title>' + '\n'
			f_content = '\t\t' + '<f_content>\n' + str(features.feature_content) + '\n\t\t</f_content>' + '\n'
			f_image = '\t\t' + '<f_img>' + str(features.feature_image) + '</f_img>' + '\n'
			f_display_choice = '\t\t' + '<f_display_choice>' + str(features.display_choice) + '</f_display_choice>' + '\n'
			print f_start
			print f_title
			print f_content
			print f_image
			print f_display_choice
			print f_close   
			f_store.write(f_start)
			f_store.write(f_title)
			f_store.write(f_content)
			f_store.write(f_image)
			f_store.write(f_display_choice)
			f_store.write(f_close)

	
print p_close
f_store.write(p_close)
