# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Movie.director'
        db.add_column(u'movie_movie', 'director',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['movie.Director']),
                      keep_default=False)

        # Adding M2M table for field actors on 'Movie'
        m2m_table_name = db.shorten_name(u'movie_movie_actors')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('movie', models.ForeignKey(orm[u'movie.movie'], null=False)),
            ('actor', models.ForeignKey(orm[u'movie.actor'], null=False))
        ))
        db.create_unique(m2m_table_name, ['movie_id', 'actor_id'])


    def backwards(self, orm):
        # Deleting field 'Movie.director'
        db.delete_column(u'movie_movie', 'director_id')

        # Removing M2M table for field actors on 'Movie'
        db.delete_table(db.shorten_name(u'movie_movie_actors'))


    models = {
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
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'movie.version': {
            'Meta': {'object_name': 'Version'},
            'begin_date': ('django.db.models.fields.DateField', [], {}),
            'end_date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'movie': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['movie.Movie']"}),
            'presentation': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['movie.Presentation']"})
        }
    }

    complete_apps = ['movie']