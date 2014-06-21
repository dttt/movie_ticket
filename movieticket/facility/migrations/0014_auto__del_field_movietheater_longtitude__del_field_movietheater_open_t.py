# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'MovieTheater.longtitude'
        db.delete_column(u'facility_movietheater', 'longtitude')

        # Deleting field 'MovieTheater.open_time'
        db.delete_column(u'facility_movietheater', 'open_time')

        # Deleting field 'MovieTheater.close_time'
        db.delete_column(u'facility_movietheater', 'close_time')

        # Deleting field 'MovieTheater.latitude'
        db.delete_column(u'facility_movietheater', 'latitude')

        # Adding field 'MovieTheater.google_map'
        db.add_column(u'facility_movietheater', 'google_map',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'MovieTheater.longtitude'
        db.add_column(u'facility_movietheater', 'longtitude',
                      self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=11, decimal_places=6, blank=True),
                      keep_default=False)

        # Adding field 'MovieTheater.open_time'
        db.add_column(u'facility_movietheater', 'open_time',
                      self.gf('django.db.models.fields.TimeField')(default=datetime.datetime(2014, 6, 20, 0, 0)),
                      keep_default=False)

        # Adding field 'MovieTheater.close_time'
        db.add_column(u'facility_movietheater', 'close_time',
                      self.gf('django.db.models.fields.TimeField')(default=datetime.datetime(2014, 6, 20, 0, 0)),
                      keep_default=False)

        # Adding field 'MovieTheater.latitude'
        db.add_column(u'facility_movietheater', 'latitude',
                      self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=11, decimal_places=6, blank=True),
                      keep_default=False)

        # Deleting field 'MovieTheater.google_map'
        db.delete_column(u'facility_movietheater', 'google_map')


    models = {
        u'facility.cinemaroom': {
            'Meta': {'object_name': 'CinemaRoom'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'theater': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['facility.MovieTheater']"}),
            'total_column': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'total_row': ('django.db.models.fields.CharField', [], {'default': "'a'", 'max_length': '2'})
        },
        u'facility.movietheater': {
            'Meta': {'object_name': 'MovieTheater'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'google_map': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'default': "''", 'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'tel': ('django.db.models.fields.CharField', [], {'default': "'0'", 'max_length': '11'})
        }
    }

    complete_apps = ['facility']