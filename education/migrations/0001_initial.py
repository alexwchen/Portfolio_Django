# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Material'
        db.create_table(u'education_material', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('date', self.gf('django.db.models.fields.DateField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('source_url', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('image_url', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'education', ['Material'])

        # Adding model 'Material_Type'
        db.create_table(u'education_material_type', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('material', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['education.Material'])),
            ('material_type', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'education', ['Material_Type'])


    def backwards(self, orm):
        # Deleting model 'Material'
        db.delete_table(u'education_material')

        # Deleting model 'Material_Type'
        db.delete_table(u'education_material_type')


    models = {
        u'education.material': {
            'Meta': {'object_name': 'Material'},
            'date': ('django.db.models.fields.DateField', [], {'max_length': '200'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_url': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'source_url': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'education.material_type': {
            'Meta': {'object_name': 'Material_Type'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'material': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['education.Material']"}),
            'material_type': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['education']