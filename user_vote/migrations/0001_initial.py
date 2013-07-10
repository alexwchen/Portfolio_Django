# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'User_ID'
        db.create_table(u'user_vote_user_id', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user_ip', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'user_vote', ['User_ID'])

        # Adding model 'User_Event'
        db.create_table(u'user_vote_user_event', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['user_vote.User_ID'])),
            ('enter_time', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('page_link', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('time_on_page', self.gf('django.db.models.fields.IntegerField')(null=True)),
        ))
        db.send_create_signal(u'user_vote', ['User_Event'])

        # Adding model 'User_Project_Lock'
        db.create_table(u'user_vote_user_project_lock', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['user_vote.User_ID'])),
            ('project_lock', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('project_link', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'user_vote', ['User_Project_Lock'])


    def backwards(self, orm):
        # Deleting model 'User_ID'
        db.delete_table(u'user_vote_user_id')

        # Deleting model 'User_Event'
        db.delete_table(u'user_vote_user_event')

        # Deleting model 'User_Project_Lock'
        db.delete_table(u'user_vote_user_project_lock')


    models = {
        u'user_vote.user_event': {
            'Meta': {'object_name': 'User_Event'},
            'enter_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'page_link': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'time_on_page': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'user_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['user_vote.User_ID']"})
        },
        u'user_vote.user_id': {
            'Meta': {'object_name': 'User_ID'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user_ip': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'user_vote.user_project_lock': {
            'Meta': {'object_name': 'User_Project_Lock'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'project_link': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'project_lock': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'user_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['user_vote.User_ID']"})
        }
    }

    complete_apps = ['user_vote']