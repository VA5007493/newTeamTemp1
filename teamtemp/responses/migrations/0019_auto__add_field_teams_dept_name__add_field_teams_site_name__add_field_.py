# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Teams.dept_name'
        db.add_column(u'responses_teams', 'dept_name',
                      self.gf('django.db.models.fields.CharField')(max_length=64, null=True),
                      keep_default=False)

        # Adding field 'Teams.site_name'
        db.add_column(u'responses_teams', 'site_name',
                      self.gf('django.db.models.fields.CharField')(max_length=64, null=True),
                      keep_default=False)

        # Adding field 'Teams.region_name'
        db.add_column(u'responses_teams', 'region_name',
                      self.gf('django.db.models.fields.CharField')(max_length=64, null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Teams.dept_name'
        db.delete_column(u'responses_teams', 'dept_name')

        # Deleting field 'Teams.site_name'
        db.delete_column(u'responses_teams', 'site_name')

        # Deleting field 'Teams.region_name'
        db.delete_column(u'responses_teams', 'region_name')


    models = {
        u'responses.teamresponsehistory': {
            'Meta': {'object_name': 'TeamResponseHistory'},
            'archive_date': ('django.db.models.fields.DateTimeField', [], {}),
            'average_score': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '5'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'request': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['responses.TeamTemperature']"}),
            'responder_count': ('django.db.models.fields.IntegerField', [], {}),
            'team_name': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True'}),
            'word_list': ('django.db.models.fields.CharField', [], {'max_length': '5000'})
        },
        u'responses.teams': {
            'Meta': {'object_name': 'Teams'},
            'dept_name': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'region_name': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True'}),
            'request': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['responses.TeamTemperature']"}),
            'site_name': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True'}),
            'team_name': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True'})
        },
        u'responses.teamtemperature': {
            'Meta': {'object_name': 'TeamTemperature'},
            'archive_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'archive_schedule': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'creation_date': ('django.db.models.fields.DateField', [], {}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['responses.User']"}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '8', 'primary_key': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'survey_type': ('django.db.models.fields.CharField', [], {'default': "'TEAMTEMP'", 'max_length': '20'})
        },
        u'responses.temperatureresponse': {
            'Meta': {'object_name': 'TemperatureResponse'},
            'archive_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'archived': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'request': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['responses.TeamTemperature']"}),
            'responder': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['responses.User']"}),
            'response_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'score': ('django.db.models.fields.IntegerField', [], {}),
            'team_name': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True'}),
            'word': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        },
        u'responses.user': {
            'Meta': {'object_name': 'User'},
            'id': ('django.db.models.fields.CharField', [], {'max_length': '8', 'primary_key': 'True'})
        },
        u'responses.wordcloudimage': {
            'Meta': {'object_name': 'WordCloudImage'},
            'creation_date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_url': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'word_list': ('django.db.models.fields.CharField', [], {'max_length': '5000'})
        }
    }

    complete_apps = ['responses']