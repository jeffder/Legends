# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Game.is_manual_result'
        db.add_column('main_game', 'is_manual_result',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Game.is_manual_result'
        db.delete_column('main_game', 'is_manual_result')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80', 'unique': 'True'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'to': "orm['auth.Permission']", 'symmetrical': 'False'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'object_name': 'Permission', 'unique_together': "(('content_type', 'codename'),)"},
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
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'to': "orm['auth.Group']", 'symmetrical': 'False', 'related_name': "'user_set'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'to': "orm['auth.Permission']", 'symmetrical': 'False', 'related_name': "'user_set'"}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '30', 'unique': 'True'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'db_table': "'django_content_type'", 'object_name': 'ContentType', 'unique_together': "(('app_label', 'model'),)"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'main.aflladder': {
            'Meta': {'db_table': "'main_afl_ladder'", 'object_name': 'AFLLadder'},
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
            'Meta': {'db_table': "'main_brownlow_ladder'", 'object_name': 'BrownlowLadder'},
            'avg_score': ('django.db.models.fields.FloatField', [], {'default': '0', 'null': 'True'}),
            'club': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Club']", 'related_name': "'brownlowladders'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'max_score': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True'}),
            'min_score': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True'}),
            'nothing': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'position': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'previous_position': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'rank_1': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'rank_2': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'rank_3': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'rank_4': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'rank_5': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'round': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Round']", 'related_name': "'brownlowladders'"}),
            'score': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'strike_rate': ('django.db.models.fields.FloatField', [], {'default': '0', 'null': 'True'})
        },
        'main.bye': {
            'Meta': {'ordering': "('-round__season', 'round', 'club')", 'object_name': 'Bye'},
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
            'Meta': {'ordering': "['name']", 'object_name': 'Club'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'nickname': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'related_name': "'clubs'", 'unique': 'True'})
        },
        'main.coach': {
            'Meta': {'ordering': "['-season', 'club', 'last_name', 'first_name']", 'object_name': 'Coach'},
            'club': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Club']", 'related_name': "'coaches'"}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True'}),
            'has_paid_fees': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_assistant': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True'}),
            'season': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Season']", 'related_name': "'coaches'"})
        },
        'main.colemanladder': {
            'Meta': {'db_table': "'main_coleman_ladder'", 'object_name': 'ColemanLadder'},
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
            'Meta': {'db_table': "'main_crowds_ladder'", 'object_name': 'CrowdsLadder'},
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
            'Meta': {'ordering': "('-round__season', 'round', 'game_date', 'afl_home')", 'object_name': 'Game'},
            'afl_away': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Club']", 'related_name': "'afl_game_away'"}),
            'afl_away_score': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'afl_home': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Club']", 'related_name': "'afl_game_home'"}),
            'afl_home_score': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'crowd': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'finals_game': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'game_date': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'null': 'True'}),
            'ground': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Ground']", 'related_name': "'games'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_manual_result': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
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
            'Meta': {'ordering': "['name']", 'object_name': 'Ground'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'main.legendsladder': {
            'Meta': {'db_table': "'main_legends_ladder'", 'object_name': 'LegendsLadder'},
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
            'Meta': {'db_table': "'main_margins_ladder'", 'object_name': 'MarginsLadder'},
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
            'Meta': {'db_table': "'main_past_brownlow_ladder'", 'object_name': 'PastBrownlowLadder'},
            'avg_score': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'club': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Club']", 'related_name': "'pastbrownlowladders'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'position': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True'}),
            'score': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'season': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Season']", 'related_name': "'past_pastbrownlowladders'"})
        },
        'main.pastcategorywinner': {
            'Meta': {'ordering': "('-season__season', 'category', 'club')", 'db_table': "'main_past_category_winner'", 'object_name': 'PastCategoryWinner'},
            'category': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'club': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Club']", 'null': 'True', 'related_name': "'past_category_winners'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'season': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Season']", 'related_name': "'past_category_winners'"})
        },
        'main.pastcoach': {
            'Meta': {'ordering': "['-season', 'club', 'last_name', 'first_name']", 'db_table': "'main_past_coach'", 'object_name': 'PastCoach'},
            'club': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Club']", 'related_name': "'past_coaches'"}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True'}),
            'season': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Season']", 'related_name': "'past_coaches'"})
        },
        'main.pastcolemanladder': {
            'Meta': {'db_table': "'main_past_coleman_ladder'", 'object_name': 'PastColemanLadder'},
            'avg_score': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'club': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Club']", 'related_name': "'pastcolemanladders'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'position': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True'}),
            'score': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'season': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Season']", 'related_name': "'past_pastcolemanladders'"})
        },
        'main.pastcrowdsladder': {
            'Meta': {'db_table': "'main_past_crowds_ladder'", 'object_name': 'PastCrowdsLadder'},
            'avg_score': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'club': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Club']", 'related_name': "'pastcrowdsladders'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'position': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True'}),
            'score': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'season': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Season']", 'related_name': "'past_pastcrowdsladders'"})
        },
        'main.pastlegendsladder': {
            'Meta': {'db_table': "'main_past_legends_ladder'", 'object_name': 'PastLegendsLadder'},
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
            'Meta': {'db_table': "'main_past_margins_ladder'", 'object_name': 'PastMarginsLadder'},
            'avg_score': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'club': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Club']", 'related_name': "'pastmarginsladders'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'position': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True'}),
            'score': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'season': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Season']", 'related_name': "'past_pastmarginsladders'"})
        },
        'main.player': {
            'Meta': {'ordering': "['-season', 'club', 'last_name', 'initial', 'first_name']", 'object_name': 'Player'},
            'club': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Club']", 'related_name': "'players'"}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'initial': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '1', 'null': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'season': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Season']", 'related_name': "'players'"}),
            'supercoach_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30', 'null': 'True'})
        },
        'main.round': {
            'Meta': {'ordering': "('season', 'start_time')", 'object_name': 'Round'},
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
            'Meta': {'ordering': "['-season']", 'object_name': 'Season'},
            'has_full_data': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'has_no_data': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'season': ('django.db.models.fields.IntegerField', [], {})
        },
        'main.streakladder': {
            'Meta': {'ordering': "['wins', 'draws', '-losses', 'club']", 'db_table': "'main_streak_ladder'", 'object_name': 'StreakLadder'},
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
            'Meta': {'db_table': "'main_supercoach_ranking'", 'object_name': 'SupercoachRanking'},
            'game': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Game']", 'related_name': "'supercoach_rankings'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'player': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Player']", 'related_name': "'supercoach_rankings'"}),
            'ranking': ('django.db.models.fields.IntegerField', [], {})
        },
        'main.supercoachtip': {
            'Meta': {'ordering': "('player__last_name', 'player__initial', 'player__first_name')", 'db_table': "'main_supercoach_tip'", 'object_name': 'SupercoachTip'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'player': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Player']", 'null': 'True', 'related_name': "'supercoach_tips'"}),
            'score': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True'}),
            'tip': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Tip']", 'related_name': "'supercoach_tips'"})
        },
        'main.tip': {
            'Meta': {'ordering': "('-game', 'club')", 'object_name': 'Tip'},
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
            'winner': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Club']", 'null': 'True', 'related_name': "'tip_winners'"}),
            'winners_score': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['main']