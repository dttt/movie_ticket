# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'MovieTheater'
        db.create_table(u'facility_movietheater', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('open_time', self.gf('django.db.models.fields.TimeField')()),
            ('close_time', self.gf('django.db.models.fields.TimeField')()),
        ))
        db.send_create_signal(u'facility', ['MovieTheater'])


    def backwards(self, orm):
        # Deleting model 'MovieTheater'
        db.delete_table(u'facility_movietheater')


    models = {
        u'facility.movietheater': {
            'Meta': {'object_name': 'MovieTheater'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'close_time': ('django.db.models.fields.TimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'open_time': ('django.db.models.fields.TimeField', [], {})
        }
    }

    complete_apps = ['facility']