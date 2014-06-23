# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Question.text'
        db.alter_column(u'faq_question', 'text', self.gf('django.db.models.fields.CharField')(max_length=100))

    def backwards(self, orm):

        # Changing field 'Question.text'
        db.alter_column(u'faq_question', 'text', self.gf('django.db.models.fields.CharField')(max_length=10))

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
            'text': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'topic': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['faq.Topic']"})
        },
        u'faq.topic': {
            'Meta': {'object_name': 'Topic'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['faq']