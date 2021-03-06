# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'MovieTheater.longtitude'
        db.alter_column(u'facility_movietheater', 'longtitude', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=20, decimal_places=10))

        # Changing field 'MovieTheater.latitude'
        db.alter_column(u'facility_movietheater', 'latitude', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=20, decimal_places=10))

    def backwards(self, orm):

        # Changing field 'MovieTheater.longtitude'
        db.alter_column(u'facility_movietheater', 'longtitude', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'MovieTheater.latitude'
        db.alter_column(u'facility_movietheater', 'latitude', self.gf('django.db.models.fields.FloatField')(null=True))

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
            'latitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '10', 'blank': 'True'}),
            'longtitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '10', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'open_time': ('django.db.models.fields.TimeField', [], {})
        }
    }

    complete_apps = ['facility']