# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Ticket'
        db.create_table(u'ticket_ticket', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('price', self.gf('django.db.models.fields.IntegerField')()),
            ('row', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('column', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('date_sold', self.gf('django.db.models.fields.DateField')()),
            ('ticket_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ticket.TicketType'])),
            ('schedule', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ticket.Schedule'])),
        ))
        db.send_create_signal(u'ticket', ['Ticket'])

        # Adding model 'TicketType'
        db.create_table(u'ticket_tickettype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=40)),
        ))
        db.send_create_signal(u'ticket', ['TicketType'])


    def backwards(self, orm):
        # Deleting model 'Ticket'
        db.delete_table(u'ticket_ticket')

        # Deleting model 'TicketType'
        db.delete_table(u'ticket_tickettype')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
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
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100', 'blank': 'True'}),
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
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '20', 'blank': 'True'})
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
        },
        u'ticket.schedule': {
            'Meta': {'object_name': 'Schedule'},
            'begin_time': ('django.db.models.fields.TimeField', [], {}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['users.CustomUser']"}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'end_time': ('django.db.models.fields.TimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'movie': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['movie.Version']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'room': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['facility.CinemaRoom']"})
        },
        u'ticket.ticket': {
            'Meta': {'object_name': 'Ticket'},
            'column': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'date_sold': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'price': ('django.db.models.fields.IntegerField', [], {}),
            'row': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'schedule': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ticket.Schedule']"}),
            'ticket_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ticket.TicketType']"})
        },
        u'ticket.tickettype': {
            'Meta': {'object_name': 'TicketType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        u'users.customuser': {
            'Meta': {'object_name': 'CustomUser'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'card_id': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 5, 27, 0, 0)'}),
            'date_of_birth': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '255'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'tel': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"})
        }
    }

    complete_apps = ['ticket']