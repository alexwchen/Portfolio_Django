# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Project'
        db.create_table(u'rankProj_project', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('authors', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('complete_date', self.gf('django.db.models.fields.DateField')()),
            ('short_description', self.gf('django.db.models.fields.TextField')()),
            ('tags', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('link', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('rank_img', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('vote_up', self.gf('django.db.models.fields.IntegerField')()),
            ('base_vote', self.gf('django.db.models.fields.IntegerField')()),
            ('PDF', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('video_url', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('motivation_content', self.gf('django.db.models.fields.TextField')()),
            ('motivation_image', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'rankProj', ['Project'])

        # Adding model 'Feature'
        db.create_table(u'rankProj_feature', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['rankProj.Project'])),
            ('feature_title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('feature_content', self.gf('django.db.models.fields.TextField')()),
            ('feature_image', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('display_choice', self.gf('django.db.models.fields.IntegerField')()),
            ('feature_order', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'rankProj', ['Feature'])

        # Adding model 'Project_Type'
        db.create_table(u'rankProj_project_type', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['rankProj.Project'])),
            ('project_type', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'rankProj', ['Project_Type'])


    def backwards(self, orm):
        # Deleting model 'Project'
        db.delete_table(u'rankProj_project')

        # Deleting model 'Feature'
        db.delete_table(u'rankProj_feature')

        # Deleting model 'Project_Type'
        db.delete_table(u'rankProj_project_type')


    models = {
        u'rankProj.feature': {
            'Meta': {'object_name': 'Feature'},
            'display_choice': ('django.db.models.fields.IntegerField', [], {}),
            'feature_content': ('django.db.models.fields.TextField', [], {}),
            'feature_image': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'feature_order': ('django.db.models.fields.IntegerField', [], {}),
            'feature_title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['rankProj.Project']"})
        },
        u'rankProj.project': {
            'Meta': {'object_name': 'Project'},
            'PDF': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'authors': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'base_vote': ('django.db.models.fields.IntegerField', [], {}),
            'complete_date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'motivation_content': ('django.db.models.fields.TextField', [], {}),
            'motivation_image': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'rank_img': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'short_description': ('django.db.models.fields.TextField', [], {}),
            'tags': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'video_url': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'vote_up': ('django.db.models.fields.IntegerField', [], {})
        },
        u'rankProj.project_type': {
            'Meta': {'object_name': 'Project_Type'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['rankProj.Project']"}),
            'project_type': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['rankProj']