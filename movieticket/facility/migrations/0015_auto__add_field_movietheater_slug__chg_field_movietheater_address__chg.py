# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'MovieTheater.slug'
        db.add_column(u'facility_movietheater', 'slug',
                      self.gf('django.db.models.fields.SlugField')(max_length=255, unique=True, null=True),
                      keep_default=False)


        # Changing field 'MovieTheater.address'
        db.alter_column(u'facility_movietheater', 'address', self.gf('django.db.models.fields.TextField')(max_length=255))

        # Changing field 'MovieTheater.google_map'
        db.alter_column(u'facility_movietheater', 'google_map', self.gf('django.db.models.fields.TextField')())
        # Adding unique constraint on 'MovieTheater', fields ['name']
        db.create_unique(u'facility_movietheater', ['name'])


    def backwards(self, orm):
        # Removing unique constraint on 'MovieTheater', fields ['name']
        db.delete_unique(u'facility_movietheater', ['name'])

        # Deleting field 'MovieTheater.slug'
        db.delete_column(u'facility_movietheater', 'slug')


        # Changing field 'MovieTheater.address'
        db.alter_column(u'facility_movietheater', 'address', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'MovieTheater.google_map'
        db.alter_column(u'facility_movietheater', 'google_map', self.gf('django.db.models.fields.CharField')(max_length=255))

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
            'address': ('django.db.models.fields.TextField', [], {'max_length': '255'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'google_map': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'default': "''", 'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255', 'unique': 'True', 'null': 'True'}),
            'tel': ('django.db.models.fields.CharField', [], {'default': "'0'", 'max_length': '11'})
        }
    }

    complete_apps = ['facility']