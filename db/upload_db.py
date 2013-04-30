import sys,os
from datetime import *
sys.path.append('/Users/alexwchen/Desktop/')
os.environ['DJANGO_SETTINGS_MODULE'] ='portfolio.settings'

from django.core.management import setup_environ
from portfolio import settings

setup_environ(settings)

sys.path.append('/Users/alexwchen/Desktop/portfolio')
from portfolio.rankProj.models import Project, Feature
from portfolio.polls.models import Poll


import re
from urllib2 import *
from BeautifulSoup import BeautifulSoup

allProj = Project.objects.all()
allFeature = Feature.objects.all()

f_store = open('projdb.xml').read()
soup = BeautifulSoup(f_store)
projects = soup('project')

for proj in projects:
	eachproj = BeautifulSoup(str(proj))
	pattern = re.compile('>.*<')
	p_title = str(eachproj('p_title'))[1:-1] +'\n'
	search = re.search(pattern,p_title)
	p_title = str(search.group()[1:-1])

	p_authors = str(eachproj('authors'))[1:-1] +'\n'
	search = re.search(pattern,p_authors)
	p_authors = str(search.group()[1:-1])

	p_date = str(eachproj('date'))[1:-1] +'\n'
	search = re.search(pattern,p_date)
	p_date = str(search.group()[1:-1])
	
	p_vid = str(eachproj('vid_url'))[1:-1] +'\n'
	search = re.search(pattern,p_vid)
	p_vid = str(search.group()[1:-1])
	
	p_mcontent = str(eachproj('p_content'))[1:-1] +'\n'	
	p_mcontent = p_mcontent.replace("\r","@")
	p_mcontent = p_mcontent.replace("\t","@")
	p_mcontent = p_mcontent.split("\n")
	p_content_list = []
	for i in p_mcontent:
		if i!="@":
			p_content_list.append(i.replace("@", ""))
	p_content_list = p_content_list[1:-2]

	p_mimage = str(eachproj('p_img'))[1:-1]	+'\n'
	p_mimage = re.search(pattern,p_mimage)
	p_mimage = str(p_mimage.group()[1:-1])
	
	p_id = str(eachproj('id'))[1:-1] +'\n'	
	p_id = re.search(pattern,p_id)
	p_id = str(p_id.group()[1:-1])

	p_pdf = str(eachproj('pdf'))[1:-1] +'\n'	
	p_pdf = re.search(pattern,p_pdf)
	p_pdf = str(p_pdf.group()[1:-1])

	p_voteup = str(eachproj('vote_up'))[1:-1] +'\n'	
	p_voteup = re.search(pattern,p_voteup)
	p_voteup = str(p_voteup.group()[1:-1])

	p_votedown = str(eachproj('vote_down'))[1:-1] +'\n'	
	p_votedown = re.search(pattern,p_votedown)
	p_votedown = str(p_votedown.group()[1:-1])

	p_proj_type = str(eachproj('proj_type'))[1:-1] +'\n'	
	p_proj_type = re.search(pattern,p_proj_type)
	p_proj_type = str(p_proj_type.group()[1:-1])
	
	p_tags = str(eachproj('tags'))[1:-1] +'\n'	
	p_tags = re.search(pattern,p_tags)
	p_tags = str(p_tags.group()[1:-1])
	
	"""
	print p_title
	print p_authors
	print p_date
	print p_vid
	for i in p_content_list:
		print i
	print p_mimage
	print p_id
	"""
	newProj = Project(title=p_title)
	newProj.authors = p_authors
	newProj.complete_date = p_date
	newProj.video_url = p_vid
	newProj.motivation_image = p_mimage
	newProj.id = p_id
	tmpMotivationStr = ''
	for i in p_content_list:
		tmpMotivationStr = tmpMotivationStr + i + '\n\n'
	newProj.motivation_content = tmpMotivationStr
	
	newProj.vote_up = p_voteup
	newProj.vote_down = p_votedown
	newProj.PDF = p_pdf
	newProj.proj_type = p_proj_type
	newProj.tags = p_tags
	
	newProj.save()
	
	features = eachproj('feature')
	for fea in features:	
		eachfea = BeautifulSoup(str(fea))
		f_title = str(eachfea('title'))[1:-1] +'\n'
		f_title = re.search(pattern,f_title)
		f_title = str(f_title.group()[1:-1])
		
		f_content = str(eachfea('f_content'))[1:-1] +'\n'	
		f_content = f_content.replace("\r","@")
		f_content = f_content.replace("\t","@")
		f_content = f_content.split("\n")
		f_content_list = []
		for i in f_content:
			if i!="@":
				f_content_list.append(i.replace("@", ""))
		f_content_list = f_content_list[1:-2]
		print f_content_list
		

		f_img = str(eachfea('f_img'))[1:-1] +'\n'
		f_img = re.search(pattern,f_img)
		f_img = str(f_img.group()[1:-1])

		f_display_choice = str(eachfea('f_display_choice'))[1:-1] +'\n'
		f_display_choice = re.search(pattern,f_display_choice)
		f_display_choice = str(f_display_choice.group()[1:-1])
		
		print f_title
		print f_content_list
		print f_img
		print f_display_choice
		
		newFea = Feature(feature_title=f_title)
		newFea.feature_image = f_img
		newFea.project = newProj	
		tmpFeaStr = ''
		for i in f_content_list:
			tmpFeaStr = tmpFeaStr + i + '\n\n'
		newFea.feature_content = tmpFeaStr
		newFea.display_choice=0
		newFea.save()
		