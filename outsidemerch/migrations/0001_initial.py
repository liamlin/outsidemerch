# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Stage'
        db.create_table(u'outsidemerch_stage', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=120)),
        ))
        db.send_create_signal(u'outsidemerch', ['Stage'])

        # Adding model 'Event'
        db.create_table(u'outsidemerch_event', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('time', self.gf('django.db.models.fields.DateTimeField')()),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('stage', self.gf('django.db.models.fields.related.ForeignKey')(related_name='events', to=orm['outsidemerch.Stage'])),
        ))
        db.send_create_signal(u'outsidemerch', ['Event'])

        # Adding model 'Artist'
        db.create_table(u'outsidemerch_artist', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=120)),
        ))
        db.send_create_signal(u'outsidemerch', ['Artist'])

        # Adding M2M table for field event on 'Artist'
        m2m_table_name = db.shorten_name(u'outsidemerch_artist_event')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('artist', models.ForeignKey(orm[u'outsidemerch.artist'], null=False)),
            ('event', models.ForeignKey(orm[u'outsidemerch.event'], null=False))
        ))
        db.create_unique(m2m_table_name, ['artist_id', 'event_id'])

        # Adding model 'Store'
        db.create_table(u'outsidemerch_store', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('artist', self.gf('django.db.models.fields.related.ForeignKey')(related_name='store', to=orm['outsidemerch.Artist'])),
        ))
        db.send_create_signal(u'outsidemerch', ['Store'])

        # Adding model 'Item'
        db.create_table(u'outsidemerch_item', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('price', self.gf('django.db.models.fields.FloatField')()),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('store', self.gf('django.db.models.fields.related.ForeignKey')(related_name='items', to=orm['outsidemerch.Store'])),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('created_time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'outsidemerch', ['Item'])


    def backwards(self, orm):
        # Deleting model 'Stage'
        db.delete_table(u'outsidemerch_stage')

        # Deleting model 'Event'
        db.delete_table(u'outsidemerch_event')

        # Deleting model 'Artist'
        db.delete_table(u'outsidemerch_artist')

        # Removing M2M table for field event on 'Artist'
        db.delete_table(db.shorten_name(u'outsidemerch_artist_event'))

        # Deleting model 'Store'
        db.delete_table(u'outsidemerch_store')

        # Deleting model 'Item'
        db.delete_table(u'outsidemerch_item')


    models = {
        u'outsidemerch.artist': {
            'Meta': {'object_name': 'Artist'},
            'event': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'artists'", 'symmetrical': 'False', 'to': u"orm['outsidemerch.Event']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '120'})
        },
        u'outsidemerch.event': {
            'Meta': {'object_name': 'Event'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'stage': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'events'", 'to': u"orm['outsidemerch.Stage']"}),
            'time': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'outsidemerch.item': {
            'Meta': {'object_name': 'Item'},
            'created_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'price': ('django.db.models.fields.FloatField', [], {}),
            'store': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'items'", 'to': u"orm['outsidemerch.Store']"})
        },
        u'outsidemerch.stage': {
            'Meta': {'object_name': 'Stage'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '120'})
        },
        u'outsidemerch.store': {
            'Meta': {'object_name': 'Store'},
            'artist': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'store'", 'to': u"orm['outsidemerch.Artist']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '120'})
        }
    }

    complete_apps = ['outsidemerch']