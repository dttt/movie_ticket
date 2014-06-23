# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Topic'
        db.create_table(u'faq_topic', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('text', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'faq', ['Topic'])

        # Adding model 'Question'
        db.create_table(u'faq_question', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('text', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('topic', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['faq.Topic'])),
        ))
        db.send_create_signal(u'faq', ['Question'])

        # Adding model 'Answer'
        db.create_table(u'faq_answer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('question', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['faq.Question'], unique=True)),
        ))
        db.send_create_signal(u'faq', ['Answer'])


    def backwards(self, orm):
        # Deleting model 'Topic'
        db.delete_table(u'faq_topic')

        # Deleting model 'Question'
        db.delete_table(u'faq_question')

        # Deleting model 'Answer'
        db.delete_table(u'faq_answer')


    models = {
        u'faq.answer': {
            'Meta': {'object_name': 'Answer'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['faq.Question']", 'unique': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {})
        },
        u'faq.question': {
            'Meta': {'object_name': 'Question'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'topic': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['faq.Topic']"})
        },
        u'faq.topic': {
            'Meta': {'object_name': 'Topic'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['faq']