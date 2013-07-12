# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Supervisor_Famous_paper.conference'
        db.delete_column(u'resume_supervisor_famous_paper', 'conference')

        # Deleting field 'Supervisor_Famous_paper.author'
        db.delete_column(u'resume_supervisor_famous_paper', 'author')


    def backwards(self, orm):
        # Adding field 'Supervisor_Famous_paper.conference'
        db.add_column(u'resume_supervisor_famous_paper', 'conference',
                      self.gf('django.db.models.fields.CharField')(default='none', max_length=200),
                      keep_default=False)

        # Adding field 'Supervisor_Famous_paper.author'
        db.add_column(u'resume_supervisor_famous_paper', 'author',
                      self.gf('django.db.models.fields.CharField')(default='none', max_length=200),
                      keep_default=False)


    models = {
        u'resume.affiliation': {
            'Meta': {'object_name': 'Affiliation'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'period': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'resume.contact': {
            'Meta': {'object_name': 'Contact'},
            'email': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'research_interest': ('django.db.models.fields.TextField', [], {'max_length': '200'}),
            'title_contact': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'title_research': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'resume.education': {
            'Meta': {'object_name': 'Education'},
            'degree': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'duration': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'program': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'skills_design_tools': ('django.db.models.fields.TextField', [], {}),
            'skills_programming_languages': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'resume.images': {
            'Contact': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['resume.Contact']"}),
            'Meta': {'object_name': 'Images'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'link': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'resume.job': {
            'Meta': {'object_name': 'Job'},
            'company': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'detail': ('django.db.models.fields.TextField', [], {}),
            'end_date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'job_type': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'period': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'start_date': ('django.db.models.fields.DateField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'resume.supervisor': {
            'Meta': {'object_name': 'Supervisor'},
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['resume.Contact']"}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'end_date': ('django.db.models.fields.DateField', [], {}),
            'famous_paper': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'field': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_path': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'link': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'position': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'research_interest': ('django.db.models.fields.TextField', [], {'max_length': '200'}),
            'start_date': ('django.db.models.fields.DateField', [], {}),
            'university': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'resume.supervisor_affiliation': {
            'Meta': {'object_name': 'Supervisor_Affiliation'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'supervisor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['resume.Supervisor']"}),
            'title': ('django.db.models.fields.CharField', [], {'default': "'none'", 'max_length': '200'})
        },
        u'resume.supervisor_department': {
            'Meta': {'object_name': 'Supervisor_Department'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'supervisor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['resume.Supervisor']"}),
            'title': ('django.db.models.fields.CharField', [], {'default': "'none'", 'max_length': '200'})
        },
        u'resume.supervisor_famous_paper': {
            'Meta': {'object_name': 'Supervisor_Famous_paper'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'supervisor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['resume.Supervisor']"}),
            'title': ('django.db.models.fields.CharField', [], {'default': "'none'", 'max_length': '200'})
        }
    }

    complete_apps = ['resume']