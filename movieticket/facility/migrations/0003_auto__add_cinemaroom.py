# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'CinemaRoom'
        db.create_table(u'facility_cinemaroom', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('total_row', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('total_column', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('theater', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['facility.MovieTheater'])),
        ))
        db.send_create_signal(u'facility', ['CinemaRoom'])


    def backwards(self, orm):
        # Deleting model 'CinemaRoom'
        db.delete_table(u'facility_cinemaroom')


    models = {
        u'facility.cinemaroom': {
            'Meta': {'object_name': 'CinemaRoom'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'theater': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['facility.MovieTheater']"}),
            'total_column': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'total_row': ('django.db.models.fields.IntegerField', [], {'default': '1'})
        },
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