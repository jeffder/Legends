# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'PastCategoryWinner'
        db.create_table('main_past_category_winner', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('category', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('club', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Club'], related_name='past_category_winners', null=True)),
            ('season', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Season'], related_name='past_category_winners')),
        ))
        db.send_create_signal('main', ['PastCategoryWinner'])

        # Adding model 'AFLLadder'
        db.create_table('main_afl_ladder', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('club', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Club'], related_name='aflladders')),
            ('position', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('previous_position', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('round', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Round'], related_name='aflladders')),
            ('played', self.gf('django.db.models.fields.IntegerField')(default=0, null=True)),
            ('win', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('draw', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('loss', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('score_for', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('score_against', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('points', self.gf('django.db.models.fields.IntegerField')(default=0, null=True)),
            ('percentage', self.gf('django.db.models.fields.FloatField')(default=0, null=True)),
        ))
        db.send_create_signal('main', ['AFLLadder'])

        # Adding model 'PastColemanLadder'
        db.create_table('main_past_coleman_ladder', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('club', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Club'], related_name='pastcolemanladders')),
            ('avg_score', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('position', self.gf('django.db.models.fields.IntegerField')(default=0, null=True)),
            ('score', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('season', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Season'], related_name='past_pastcolemanladders')),
        ))
        db.send_create_signal('main', ['PastColemanLadder'])

        # Adding model 'PastBrownlowLadder'
        db.create_table('main_past_brownlow_ladder', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('club', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Club'], related_name='pastbrownlowladders')),
            ('avg_score', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('position', self.gf('django.db.models.fields.IntegerField')(default=0, null=True)),
            ('score', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('season', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Season'], related_name='past_pastbrownlowladders')),
        ))
        db.send_create_signal('main', ['PastBrownlowLadder'])

        # Adding model 'LegendsLadder'
        db.create_table('main_legends_ladder', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('club', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Club'], related_name='legendsladders')),
            ('position', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('previous_position', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('round', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Round'], related_name='legendsladders')),
            ('played', self.gf('django.db.models.fields.IntegerField')(default=0, null=True)),
            ('win', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('draw', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('loss', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('score_for', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('score_against', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('points', self.gf('django.db.models.fields.IntegerField')(default=0, null=True)),
            ('percentage', self.gf('django.db.models.fields.FloatField')(default=0, null=True)),
            ('bye_for', self.gf('django.db.models.fields.IntegerField')(default=0, null=True)),
            ('total_for', self.gf('django.db.models.fields.IntegerField')(default=0, null=True)),
            ('max_for', self.gf('django.db.models.fields.IntegerField')(default=0, null=True)),
            ('min_for', self.gf('django.db.models.fields.IntegerField')(default=0, null=True)),
            ('avg_for', self.gf('django.db.models.fields.FloatField')(default=0, null=True)),
            ('max_against', self.gf('django.db.models.fields.IntegerField')(default=0, null=True)),
            ('min_against', self.gf('django.db.models.fields.IntegerField')(default=0, null=True)),
            ('avg_against', self.gf('django.db.models.fields.FloatField')(default=0, null=True)),
        ))
        db.send_create_signal('main', ['LegendsLadder'])

        # Adding model 'BrownlowLadder'
        db.create_table('main_brownlow_ladder', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('club', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Club'], related_name='brownlowladders')),
            ('position', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('previous_position', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('round', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Round'], related_name='brownlowladders')),
            ('score', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('max_score', self.gf('django.db.models.fields.IntegerField')(default=0, null=True)),
            ('min_score', self.gf('django.db.models.fields.IntegerField')(default=0, null=True)),
            ('avg_score', self.gf('django.db.models.fields.FloatField')(default=0, null=True)),
            ('strike_rate', self.gf('django.db.models.fields.FloatField')(default=0, null=True)),
            ('five', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('four', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('three', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('two', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('one', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('nothing', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('main', ['BrownlowLadder'])

        # Adding model 'PastCrowdsLadder'
        db.create_table('main_past_crowds_ladder', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('club', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Club'], related_name='pastcrowdsladders')),
            ('avg_score', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('position', self.gf('django.db.models.fields.IntegerField')(default=0, null=True)),
            ('score', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('season', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Season'], related_name='past_pastcrowdsladders')),
        ))
        db.send_create_signal('main', ['PastCrowdsLadder'])

        # Adding model 'MarginsLadder'
        db.create_table('main_margins_ladder', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('club', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Club'], related_name='marginsladders')),
            ('position', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('previous_position', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('round', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Round'], related_name='marginsladders')),
            ('score', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('max_score', self.gf('django.db.models.fields.IntegerField')(default=0, null=True)),
            ('min_score', self.gf('django.db.models.fields.IntegerField')(default=0, null=True)),
            ('avg_score', self.gf('django.db.models.fields.FloatField')(default=0, null=True)),
            ('strike_rate', self.gf('django.db.models.fields.FloatField')(default=0, null=True)),
            ('exact', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('one', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('two', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('three', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('four', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('five', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('other', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('nothing', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('bonus_strike_rate', self.gf('django.db.models.fields.FloatField')(default=0, null=True)),
        ))
        db.send_create_signal('main', ['MarginsLadder'])

        # Adding model 'StreakLadder'
        db.create_table('main_streak_ladder', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('club', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Club'], related_name='streak_ladders')),
            ('losses', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('position', self.gf('django.db.models.fields.IntegerField')(default=0, null=True)),
            ('previous_position', self.gf('django.db.models.fields.IntegerField')(default=0, null=True)),
            ('round', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Round'], related_name='streak_ladders')),
            ('streak', self.gf('django.db.models.fields.CharField')(default='', max_length=30)),
            ('draws', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('wins', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('main', ['StreakLadder'])

        # Adding model 'CrowdsLadder'
        db.create_table('main_crowds_ladder', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('club', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Club'], related_name='crowdsladders')),
            ('position', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('previous_position', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('round', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Round'], related_name='crowdsladders')),
            ('score', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('max_score', self.gf('django.db.models.fields.IntegerField')(default=0, null=True)),
            ('min_score', self.gf('django.db.models.fields.IntegerField')(default=0, null=True)),
            ('avg_score', self.gf('django.db.models.fields.FloatField')(default=0, null=True)),
            ('strike_rate', self.gf('django.db.models.fields.FloatField')(default=0, null=True)),
            ('exact', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('one', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('two', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('three', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('four', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('nothing', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('bonus_strike_rate', self.gf('django.db.models.fields.FloatField')(default=0, null=True)),
        ))
        db.send_create_signal('main', ['CrowdsLadder'])

        # Adding model 'PastLegendsLadder'
        db.create_table('main_past_legends_ladder', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('club', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Club'], related_name='pastlegendsladders')),
            ('avg_score', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('position', self.gf('django.db.models.fields.IntegerField')(default=0, null=True)),
            ('score', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('season', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Season'], related_name='past_pastlegendsladders')),
            ('played', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('win', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('draw', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('loss', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('points_for', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('points_against', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('avg_points_for', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('avg_points_against', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('percentage', self.gf('django.db.models.fields.FloatField')(default=0)),
        ))
        db.send_create_signal('main', ['PastLegendsLadder'])

        # Adding model 'PastCoach'
        db.create_table('main_past_coach', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('club', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Club'], related_name='past_coaches')),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=30, null=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=30, null=True)),
            ('season', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Season'], related_name='past_coaches')),
        ))
        db.send_create_signal('main', ['PastCoach'])

        # Adding model 'ColemanLadder'
        db.create_table('main_coleman_ladder', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('club', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Club'], related_name='colemanladders')),
            ('position', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('previous_position', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('round', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Round'], related_name='colemanladders')),
            ('score', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('max_score', self.gf('django.db.models.fields.IntegerField')(default=0, null=True)),
            ('min_score', self.gf('django.db.models.fields.IntegerField')(default=0, null=True)),
            ('avg_score', self.gf('django.db.models.fields.FloatField')(default=0, null=True)),
            ('strike_rate', self.gf('django.db.models.fields.FloatField')(default=0, null=True)),
            ('bonus', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('nine', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('eight', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('seven', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('six', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('five', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('four', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('three', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('two', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('one', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('nothing', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('winners', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('bonus_strike_rate', self.gf('django.db.models.fields.FloatField')(default=0, null=True)),
        ))
        db.send_create_signal('main', ['ColemanLadder'])

        # Adding model 'PastMarginsLadder'
        db.create_table('main_past_margins_ladder', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('club', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Club'], related_name='pastmarginsladders')),
            ('avg_score', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('position', self.gf('django.db.models.fields.IntegerField')(default=0, null=True)),
            ('score', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('season', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Season'], related_name='past_pastmarginsladders')),
        ))
        db.send_create_signal('main', ['PastMarginsLadder'])


    def backwards(self, orm):
        # Deleting model 'PastCategoryWinner'
        db.delete_table('main_past_category_winner')

        # Deleting model 'AFLLadder'
        db.delete_table('main_afl_ladder')

        # Deleting model 'PastColemanLadder'
        db.delete_table('main_past_coleman_ladder')

        # Deleting model 'PastBrownlowLadder'
        db.delete_table('main_past_brownlow_ladder')

        # Deleting model 'LegendsLadder'
        db.delete_table('main_legends_ladder')

        # Deleting model 'BrownlowLadder'
        db.delete_table('main_brownlow_ladder')

        # Deleting model 'PastCrowdsLadder'
        db.delete_table('main_past_crowds_ladder')

        # Deleting model 'MarginsLadder'
        db.delete_table('main_margins_ladder')

        # Deleting model 'StreakLadder'
        db.delete_table('main_streak_ladder')

        # Deleting model 'CrowdsLadder'
        db.delete_table('main_crowds_ladder')

        # Deleting model 'PastLegendsLadder'
        db.delete_table('main_past_legends_ladder')

        # Deleting model 'PastCoach'
        db.delete_table('main_past_coach')

        # Deleting model 'ColemanLadder'
        db.delete_table('main_coleman_ladder')

        # Deleting model 'PastMarginsLadder'
        db.delete_table('main_past_margins_ladder')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'blank': 'True', 'symmetrical': 'False'})
        },
        'auth.permission': {
            'Meta': {'object_name': 'Permission', 'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)"},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'blank': 'True', 'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'blank': 'True', 'related_name': "'user_set'", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'blank': 'True', 'related_name': "'user_set'", 'symmetrical': 'False'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'object_name': 'ContentType', 'db_table': "'django_content_type'", 'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'main.aflladder': {
            'Meta': {'object_name': 'AFLLadder', 'db_table': "'main_afl_ladder'"},
            'club': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Club']", 'related_name': "'aflladders'"}),
            'draw': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'loss': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'percentage': ('django.db.models.fields.FloatField', [], {'default': '0', 'null': 'True'}),
            'played': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True'}),
            'points': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True'}),
            'position': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'previous_position': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'round': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Round']", 'related_name': "'aflladders'"}),
            'score_against': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'score_for': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'win': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'main.brownlowladder': {
            'Meta': {'object_name': 'BrownlowLadder', 'db_table': "'main_brownlow_ladder'"},
            'avg_score': ('django.db.models.fields.FloatField', [], {'default': '0', 'null': 'True'}),
            'club': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Club']", 'related_name': "'brownlowladders'"}),
            'five': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'four': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'max_score': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True'}),
            'min_score': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True'}),
            'nothing': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'one': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'position': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'previous_position': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'round': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Round']", 'related_name': "'brownlowladders'"}),
            'score': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'strike_rate': ('django.db.models.fields.FloatField', [], {'default': '0', 'null': 'True'}),
            'three': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'two': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'main.bye': {
            'Meta': {'object_name': 'Bye', 'ordering': "('-round__season', 'round', 'club')"},
            'club': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Club']", 'related_name': "'byes'"}),
            'crowds_score': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'margins_score': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'round': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Round']", 'related_name': "'byes'"}),
            'score': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'supercoach_score': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'winners_bonus': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'winners_score': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'main.club': {
            'Meta': {'object_name': 'Club', 'ordering': "['name']"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'nickname': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'unique': 'True', 'related_name': "'clubs'", 'to': "orm['auth.User']"})
        },
        'main.coach': {
            'Meta': {'object_name': 'Coach', 'ordering': "['-season', 'club', 'last_name', 'first_name']"},
            'club': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Club']", 'related_name': "'coaches'"}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True'}),
            'has_paid_fees': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_assistant': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True'}),
            'season': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Season']", 'related_name': "'coaches'"})
        },
        'main.colemanladder': {
            'Meta': {'object_name': 'ColemanLadder', 'db_table': "'main_coleman_ladder'"},
            'avg_score': ('django.db.models.fields.FloatField', [], {'default': '0', 'null': 'True'}),
            'bonus': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'bonus_strike_rate': ('django.db.models.fields.FloatField', [], {'default': '0', 'null': 'True'}),
            'club': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Club']", 'related_name': "'colemanladders'"}),
            'eight': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'five': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'four': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'max_score': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True'}),
            'min_score': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True'}),
            'nine': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'nothing': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'one': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'position': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'previous_position': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'round': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Round']", 'related_name': "'colemanladders'"}),
            'score': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'seven': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'six': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'strike_rate': ('django.db.models.fields.FloatField', [], {'default': '0', 'null': 'True'}),
            'three': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'two': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'winners': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'main.crowdsladder': {
            'Meta': {'object_name': 'CrowdsLadder', 'db_table': "'main_crowds_ladder'"},
            'avg_score': ('django.db.models.fields.FloatField', [], {'default': '0', 'null': 'True'}),
            'bonus_strike_rate': ('django.db.models.fields.FloatField', [], {'default': '0', 'null': 'True'}),
            'club': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Club']", 'related_name': "'crowdsladders'"}),
            'exact': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'four': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'max_score': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True'}),
            'min_score': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True'}),
            'nothing': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'one': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'position': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'previous_position': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'round': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Round']", 'related_name': "'crowdsladders'"}),
            'score': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'strike_rate': ('django.db.models.fields.FloatField', [], {'default': '0', 'null': 'True'}),
            'three': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'two': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'main.game': {
            'Meta': {'object_name': 'Game', 'ordering': "('-round__season', 'round', 'game_date', 'afl_home')"},
            'afl_away': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Club']", 'related_name': "'afl_game_away'"}),
            'afl_away_score': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'afl_home': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Club']", 'related_name': "'afl_game_home'"}),
            'afl_home_score': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'crowd': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'finals_game': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'game_date': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'null': 'True'}),
            'ground': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Ground']", 'related_name': "'games'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'legends_away': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Club']", 'related_name': "'legends_game_away'"}),
            'legends_away_crowds_score': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'legends_away_margins_score': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'legends_away_score': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'legends_away_supercoach_score': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'legends_away_winners_bonus': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'legends_away_winners_score': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'legends_home': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Club']", 'related_name': "'legends_game_home'"}),
            'legends_home_crowds_score': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'legends_home_margins_score': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'legends_home_score': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'legends_home_supercoach_score': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'legends_home_winners_bonus': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'legends_home_winners_score': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'round': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Round']", 'related_name': "'games'"}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'tipping_deadline': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'null': 'True'})
        },
        'main.ground': {
            'Meta': {'object_name': 'Ground', 'ordering': "['name']"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'main.legendsladder': {
            'Meta': {'object_name': 'LegendsLadder', 'db_table': "'main_legends_ladder'"},
            'avg_against': ('django.db.models.fields.FloatField', [], {'default': '0', 'null': 'True'}),
            'avg_for': ('django.db.models.fields.FloatField', [], {'default': '0', 'null': 'True'}),
            'bye_for': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True'}),
            'club': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Club']", 'related_name': "'legendsladders'"}),
            'draw': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'loss': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'max_against': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True'}),
            'max_for': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True'}),
            'min_against': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True'}),
            'min_for': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True'}),
            'percentage': ('django.db.models.fields.FloatField', [], {'default': '0', 'null': 'True'}),
            'played': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True'}),
            'points': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True'}),
            'position': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'previous_position': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'round': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Round']", 'related_name': "'legendsladders'"}),
            'score_against': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'score_for': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'total_for': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True'}),
            'win': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'main.marginsladder': {
            'Meta': {'object_name': 'MarginsLadder', 'db_table': "'main_margins_ladder'"},
            'avg_score': ('django.db.models.fields.FloatField', [], {'default': '0', 'null': 'True'}),
            'bonus_strike_rate': ('django.db.models.fields.FloatField', [], {'default': '0', 'null': 'True'}),
            'club': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Club']", 'related_name': "'marginsladders'"}),
            'exact': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'five': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'four': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'max_score': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True'}),
            'min_score': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True'}),
            'nothing': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'one': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'other': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'position': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'previous_position': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'round': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Round']", 'related_name': "'marginsladders'"}),
            'score': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'strike_rate': ('django.db.models.fields.FloatField', [], {'default': '0', 'null': 'True'}),
            'three': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'two': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'main.pastbrownlowladder': {
            'Meta': {'object_name': 'PastBrownlowLadder', 'db_table': "'main_past_brownlow_ladder'"},
            'avg_score': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'club': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Club']", 'related_name': "'pastbrownlowladders'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'position': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True'}),
            'score': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'season': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Season']", 'related_name': "'past_pastbrownlowladders'"})
        },
        'main.pastcategorywinner': {
            'Meta': {'object_name': 'PastCategoryWinner', 'db_table': "'main_past_category_winner'", 'ordering': "('-season', 'category', 'club')"},
            'category': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'club': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Club']", 'related_name': "'past_category_winners'", 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'season': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Season']", 'related_name': "'past_category_winners'"})
        },
        'main.pastcoach': {
            'Meta': {'object_name': 'PastCoach', 'db_table': "'main_past_coach'", 'ordering': "['-season', 'club', 'last_name', 'first_name']"},
            'club': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Club']", 'related_name': "'past_coaches'"}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True'}),
            'season': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Season']", 'related_name': "'past_coaches'"})
        },
        'main.pastcolemanladder': {
            'Meta': {'object_name': 'PastColemanLadder', 'db_table': "'main_past_coleman_ladder'"},
            'avg_score': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'club': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Club']", 'related_name': "'pastcolemanladders'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'position': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True'}),
            'score': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'season': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Season']", 'related_name': "'past_pastcolemanladders'"})
        },
        'main.pastcrowdsladder': {
            'Meta': {'object_name': 'PastCrowdsLadder', 'db_table': "'main_past_crowds_ladder'"},
            'avg_score': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'club': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Club']", 'related_name': "'pastcrowdsladders'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'position': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True'}),
            'score': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'season': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Season']", 'related_name': "'past_pastcrowdsladders'"})
        },
        'main.pastlegendsladder': {
            'Meta': {'object_name': 'PastLegendsLadder', 'db_table': "'main_past_legends_ladder'"},
            'avg_points_against': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'avg_points_for': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'avg_score': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'club': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Club']", 'related_name': "'pastlegendsladders'"}),
            'draw': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'loss': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'percentage': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'played': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'points_against': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'points_for': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'position': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True'}),
            'score': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'season': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Season']", 'related_name': "'past_pastlegendsladders'"}),
            'win': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'main.pastmarginsladder': {
            'Meta': {'object_name': 'PastMarginsLadder', 'db_table': "'main_past_margins_ladder'"},
            'avg_score': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'club': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Club']", 'related_name': "'pastmarginsladders'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'position': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True'}),
            'score': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'season': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Season']", 'related_name': "'past_pastmarginsladders'"})
        },
        'main.player': {
            'Meta': {'object_name': 'Player', 'ordering': "['-season', 'club', 'last_name', 'initial', 'first_name']"},
            'club': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Club']", 'related_name': "'players'"}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'initial': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '1', 'null': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'season': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Season']", 'related_name': "'players'"}),
            'supercoach_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30', 'null': 'True'})
        },
        'main.round': {
            'Meta': {'object_name': 'Round', 'ordering': "('-season', 'start_time')"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_finals': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'num_bogs': ('django.db.models.fields.IntegerField', [], {}),
            'num_games': ('django.db.models.fields.IntegerField', [], {}),
            'season': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Season']", 'related_name': "'rounds'"}),
            'start_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'tipping_deadline': ('django.db.models.fields.DateTimeField', [], {'null': 'True'})
        },
        'main.season': {
            'Meta': {'object_name': 'Season', 'ordering': "['-season']"},
            'has_full_data': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'has_no_data': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'season': ('django.db.models.fields.IntegerField', [], {})
        },
        'main.streakladder': {
            'Meta': {'object_name': 'StreakLadder', 'db_table': "'main_streak_ladder'", 'ordering': "['wins', 'draws', '-losses', 'club']"},
            'club': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Club']", 'related_name': "'streak_ladders'"}),
            'draws': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'losses': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'position': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True'}),
            'previous_position': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True'}),
            'round': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Round']", 'related_name': "'streak_ladders'"}),
            'streak': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30'}),
            'wins': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'main.supercoachranking': {
            'Meta': {'object_name': 'SupercoachRanking', 'db_table': "'main_supercoach_ranking'"},
            'game': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Game']", 'related_name': "'supercoach_rankings'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'player': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Player']", 'related_name': "'supercoach_rankings'"}),
            'ranking': ('django.db.models.fields.IntegerField', [], {})
        },
        'main.supercoachtip': {
            'Meta': {'object_name': 'SupercoachTip', 'db_table': "'main_supercoach_tip'", 'ordering': "('player__last_name', 'player__initial', 'player__first_name')"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'player': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Player']", 'related_name': "'supercoach_tips'", 'null': 'True'}),
            'tip': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Tip']", 'related_name': "'supercoach_tips'"})
        },
        'main.tip': {
            'Meta': {'object_name': 'Tip', 'ordering': "('-game', 'club')"},
            'club': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Club']", 'related_name': "'tips'"}),
            'crowd': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'crowds_score': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'game': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Game']", 'related_name': "'tips'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_default': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'margin': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'margins_score': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'score': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'supercoach_score': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'winner': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Club']", 'related_name': "'tip_winners'", 'null': 'True'}),
            'winners_score': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['main']