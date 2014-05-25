# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding M2M table for field available_theaters on 'Version'
        m2m_table_name = db.shorten_name(u'movie_version_available_theaters')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('version', models.ForeignKey(orm[u'movie.version'], null=False)),
            ('movietheater', models.ForeignKey(orm[u'facility.movietheater'], null=False))
        ))
        db.create_unique(m2m_table_name, ['version_id', 'movietheater_id'])

        # Adding unique constraint on 'Version', fields ['movie', 'presentation']
        db.create_unique(u'movie_version', ['movie_id', 'presentation_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'Version', fields ['movie', 'presentation']
        db.delete_unique(u'movie_version', ['movie_id', 'presentation_id'])

        # Removing M2M table for field available_theaters on 'Version'
        db.delete_table(db.shorten_name(u'movie_version_available_theaters'))


    models = {
        u'facility.movietheater': {
            'Meta': {'object_name': 'MovieTheater'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'close_time': ('django.db.models.fields.TimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '11', 'decimal_places': '6', 'blank': 'True'}),
            'longtitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '11', 'decimal_places': '6', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'open_time': ('django.db.models.fields.TimeField', [], {})
        },
        u'movie.actor': {
            'Meta': {'object_name': 'Actor'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'movie.company': {
            'Meta': {'object_name': 'Company'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'movie.director': {
            'Meta': {'object_name': 'Director'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'movie.genre': {
            'Meta': {'object_name': 'Genre'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'movie.movie': {
            'MPAA': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['movie.MPAA']"}),
            'Meta': {'object_name': 'Movie'},
            'actors': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['movie.Actor']", 'symmetrical': 'False'}),
            'company': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['movie.Company']"}),
            'director': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['movie.Director']"}),
            'genre': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['movie.Genre']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'length': ('django.db.models.fields.IntegerField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'poster': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'default': "'null'", 'max_length': '100'}),
            'summary': ('django.db.models.fields.TextField', [], {}),
            'trailer': ('django.db.models.fields.TextField', [], {})
        },
        u'movie.mpaa': {
            'Meta': {'object_name': 'MPAA'},
            'explanation': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'meaning': ('django.db.models.fields.TextField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        u'movie.presentation': {
            'Meta': {'object_name': 'Presentation'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'slug': ('django.db.models.fields.SlugField', [], {'default': "'null'", 'max_length': '20'})
        },
        u'movie.version': {
            'Meta': {'unique_together': "(('movie', 'presentation'),)", 'object_name': 'Version'},
            'available_theaters': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['facility.MovieTheater']", 'symmetrical': 'False', 'blank': 'True'}),
            'begin_date': ('django.db.models.fields.DateField', [], {}),
            'end_date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'movie': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['movie.Movie']"}),
            'presentation': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['movie.Presentation']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '110', 'blank': 'True'})
        }
    }

    complete_apps = ['movie']