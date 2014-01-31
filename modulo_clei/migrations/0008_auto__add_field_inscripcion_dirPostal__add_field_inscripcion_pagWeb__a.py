# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Inscripcion.dirPostal'
        db.add_column(u'modulo_clei_inscripcion', 'dirPostal',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=60),
                      keep_default=False)

        # Adding field 'Inscripcion.pagWeb'
        db.add_column(u'modulo_clei_inscripcion', 'pagWeb',
                      self.gf('django.db.models.fields.URLField')(default='', max_length=60),
                      keep_default=False)

        # Adding field 'Inscripcion.telf'
        db.add_column(u'modulo_clei_inscripcion', 'telf',
                      self.gf('django.db.models.fields.IntegerField')(default=35189581839),
                      keep_default=False)

        # Adding field 'Inscripcion.tipo'
        db.add_column(u'modulo_clei_inscripcion', 'tipo',
                      self.gf('django.db.models.fields.IntegerField')(default=15),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Inscripcion.dirPostal'
        db.delete_column(u'modulo_clei_inscripcion', 'dirPostal')

        # Deleting field 'Inscripcion.pagWeb'
        db.delete_column(u'modulo_clei_inscripcion', 'pagWeb')

        # Deleting field 'Inscripcion.telf'
        db.delete_column(u'modulo_clei_inscripcion', 'telf')

        # Deleting field 'Inscripcion.tipo'
        db.delete_column(u'modulo_clei_inscripcion', 'tipo')


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
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'modulo_clei.clei': {
            'Meta': {'object_name': 'CLEI'},
            'fechaInicio': ('django.db.models.fields.DateTimeField', [], {}),
            'fechaInscripcion': ('django.db.models.fields.DateTimeField', [], {}),
            'fechaInscripcionDescuento': ('django.db.models.fields.DateTimeField', [], {}),
            'fechaNotificacion': ('django.db.models.fields.DateTimeField', [], {}),
            'fechaTopeArticulo': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tarifaNormal': ('django.db.models.fields.FloatField', [], {}),
            'tarifaReducida': ('django.db.models.fields.FloatField', [], {}),
            'topicos': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'cleis'", 'symmetrical': 'False', 'to': u"orm['modulo_clei.Topico']"})
        },
        u'modulo_clei.cp': {
            'Meta': {'object_name': 'CP'},
            'clei': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'cp'", 'unique': 'True', 'to': u"orm['modulo_clei.CLEI']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'miembros': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['personas.Persona']", 'symmetrical': 'False'})
        },
        u'modulo_clei.inscripcion': {
            'Meta': {'unique_together': "(('clei', 'persona'),)", 'object_name': 'Inscripcion'},
            'clei': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'inscripciones'", 'to': u"orm['modulo_clei.CLEI']"}),
            'costo': ('django.db.models.fields.FloatField', [], {}),
            'dirPostal': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'fecha': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pagWeb': ('django.db.models.fields.URLField', [], {'max_length': '60'}),
            'persona': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'inscripciones'", 'to': u"orm['personas.Persona']"}),
            'telf': ('django.db.models.fields.IntegerField', [], {}),
            'tipo': ('django.db.models.fields.IntegerField', [], {})
        },
        u'modulo_clei.topico': {
            'Meta': {'object_name': 'Topico'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        },
        u'personas.persona': {
            'Meta': {'object_name': 'Persona', '_ormbases': [u'auth.User']},
            'apellido': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'dirPostal': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'experticies': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['modulo_clei.Topico']", 'symmetrical': 'False'}),
            'institucion': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'pagWeb': ('django.db.models.fields.URLField', [], {'max_length': '60'}),
            'pais': ('django_countries.fields.CountryField', [], {'max_length': '2'}),
            'telf': ('django.db.models.fields.IntegerField', [], {}),
            u'user_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True', 'primary_key': 'True'})
        }
    }

    complete_apps = ['modulo_clei']