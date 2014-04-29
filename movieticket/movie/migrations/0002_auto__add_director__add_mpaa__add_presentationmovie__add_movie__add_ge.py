# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Director'
        db.create_table(u'movie_director', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'movie', ['Director'])

        # Adding model 'MPAA'
        db.create_table(u'movie_mpaa', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('meaning', self.gf('django.db.models.fields.TextField')()),
            ('explanation', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'movie', ['MPAA'])

        # Adding model 'PresentationMovie'
        db.create_table(u'movie_presentationmovie', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('begin_date', self.gf('django.db.models.fields.DateField')()),
            ('end_date', self.gf('django.db.models.fields.DateField')()),
            ('presentation', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['movie.Presentation'])),
            ('movie', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['movie.Movie'])),
        ))
        db.send_create_signal(u'movie', ['PresentationMovie'])

        # Adding model 'Movie'
        db.create_table(u'movie_movie', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('trailer', self.gf('django.db.models.fields.TextField')()),
            ('poster', self.gf('django.db.models.fields.TextField')()),
            ('summary', self.gf('django.db.models.fields.TextField')()),
            ('length', self.gf('django.db.models.fields.IntegerField')()),
            ('company', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['movie.Company'])),
            ('MPAA', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['movie.MPAA'])),
        ))
        db.send_create_signal(u'movie', ['Movie'])

        # Adding M2M table for field genre on 'Movie'
        m2m_table_name = db.shorten_name(u'movie_movie_genre')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('movie', models.ForeignKey(orm[u'movie.movie'], null=False)),
            ('genre', models.ForeignKey(orm[u'movie.genre'], null=False))
        ))
        db.create_unique(m2m_table_name, ['movie_id', 'genre_id'])

        # Adding model 'Genre'
        db.create_table(u'movie_genre', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'movie', ['Genre'])

        # Adding model 'Actor'
        db.create_table(u'movie_actor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'movie', ['Actor'])

        # Adding model 'Company'
        db.create_table(u'movie_company', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'movie', ['Company'])

        # Adding model 'Presentation'
        db.create_table(u'movie_presentation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'movie', ['Presentation'])


    def backwards(self, orm):
        # Deleting model 'Director'
        db.delete_table(u'movie_director')

        # Deleting model 'MPAA'
        db.delete_table(u'movie_mpaa')

        # Deleting model 'PresentationMovie'
        db.delete_table(u'movie_presentationmovie')

        # Deleting model 'Movie'
        db.delete_table(u'movie_movie')

        # Removing M2M table for field genre on 'Movie'
        db.delete_table(db.shorten_name(u'movie_movie_genre'))

        # Deleting model 'Genre'
        db.delete_table(u'movie_genre')

        # Deleting model 'Actor'
        db.delete_table(u'movie_actor')

        # Deleting model 'Company'
        db.delete_table(u'movie_company')

        # Deleting model 'Presentation'
        db.delete_table(u'movie_presentation')


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
            'company': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['movie.Company']"}),
            'genre': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['movie.Genre']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'length': ('django.db.models.fields.IntegerField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'poster': ('django.db.models.fields.TextField', [], {}),
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
        u'movie.presentationmovie': {
            'Meta': {'object_name': 'PresentationMovie'},
            'begin_date': ('django.db.models.fields.DateField', [], {}),
            'end_date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'movie': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['movie.Movie']"}),
            'presentation': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['movie.Presentation']"})
        }
    }

    complete_apps = ['movie']