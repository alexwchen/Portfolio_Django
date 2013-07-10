# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Education'
        db.create_table(u'resume_education', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('degree', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('program', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('duration', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('skills_programming_languages', self.gf('django.db.models.fields.TextField')()),
            ('skills_design_tools', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'resume', ['Education'])

        # Adding model 'Job'
        db.create_table(u'resume_job', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('company', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('period', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('start_date', self.gf('django.db.models.fields.DateField')()),
            ('end_date', self.gf('django.db.models.fields.DateField')()),
            ('detail', self.gf('django.db.models.fields.TextField')()),
            ('job_type', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'resume', ['Job'])

        # Adding model 'Affiliation'
        db.create_table(u'resume_affiliation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('period', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'resume', ['Affiliation'])

        # Adding model 'Contact'
        db.create_table(u'resume_contact', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title_contact', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('title_research', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('research_interest', self.gf('django.db.models.fields.TextField')(max_length=200)),
        ))
        db.send_create_signal(u'resume', ['Contact'])

        # Adding model 'Images'
        db.create_table(u'resume_images', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Contact', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['resume.Contact'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('image_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('link', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'resume', ['Images'])

        # Adding model 'Supervisor'
        db.create_table(u'resume_supervisor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('contact', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['resume.Contact'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('start_date', self.gf('django.db.models.fields.DateField')()),
            ('end_date', self.gf('django.db.models.fields.DateField')()),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('field', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('position', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('university', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('famous_paper', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('link', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('research_interest', self.gf('django.db.models.fields.TextField')(max_length=200)),
        ))
        db.send_create_signal(u'resume', ['Supervisor'])


    def backwards(self, orm):
        # Deleting model 'Education'
        db.delete_table(u'resume_education')

        # Deleting model 'Job'
        db.delete_table(u'resume_job')

        # Deleting model 'Affiliation'
        db.delete_table(u'resume_affiliation')

        # Deleting model 'Contact'
        db.delete_table(u'resume_contact')

        # Deleting model 'Images'
        db.delete_table(u'resume_images')

        # Deleting model 'Supervisor'
        db.delete_table(u'resume_supervisor')


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
            'link': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'position': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'research_interest': ('django.db.models.fields.TextField', [], {'max_length': '200'}),
            'start_date': ('django.db.models.fields.DateField', [], {}),
            'university': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['resume']