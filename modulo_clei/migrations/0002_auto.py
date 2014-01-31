# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing M2M table for field miembros on 'CP'
        db.delete_table(db.shorten_name(u'modulo_clei_cp_miembros'))


    def backwards(self, orm):
        # Adding M2M table for field miembros on 'CP'
        m2m_table_name = db.shorten_name(u'modulo_clei_cp_miembros')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('cp', models.ForeignKey(orm[u'modulo_clei.cp'], null=False)),
            ('miembrocp', models.ForeignKey(orm[u'personas.miembrocp'], null=False))
        ))
        db.create_unique(m2m_table_name, ['cp_id', 'miembrocp_id'])


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
        u'modulo_clei.apertura': {
            'Meta': {'object_name': 'Apertura', '_ormbases': [u'modulo_clei.Evento']},
            u'evento_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['modulo_clei.Evento']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'modulo_clei.articulo': {
            'Meta': {'object_name': 'Articulo'},
            'autores': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['personas.Persona']", 'symmetrical': 'False'}),
            'clei': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'articulos'", 'to': u"orm['modulo_clei.CLEI']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pclaves': ('django.db.models.fields.TextField', [], {'max_length': '60'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '3'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'topicos': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['modulo_clei.Topico']", 'symmetrical': 'False'})
        },
        u'modulo_clei.charla': {
            'Meta': {'object_name': 'Charla', '_ormbases': [u'modulo_clei.Evento']},
            u'evento_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['modulo_clei.Evento']", 'unique': 'True', 'primary_key': 'True'}),
            'moderador': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'charlas_moderadas'", 'to': u"orm['personas.Persona']"}),
            'presentador': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['personas.Persona']"})
        },
        u'modulo_clei.clausura': {
            'Meta': {'object_name': 'Clausura', '_ormbases': [u'modulo_clei.Evento']},
            u'evento_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['modulo_clei.Evento']", 'unique': 'True', 'primary_key': 'True'})
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
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'modulo_clei.evaluacion': {
            'Meta': {'unique_together': "(('articulo', 'evaluador'),)", 'object_name': 'Evaluacion'},
            'articulo': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'correcciones'", 'to': u"orm['modulo_clei.Articulo']"}),
            'evaluador': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'evaluaciones'", 'to': u"orm['personas.Persona']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nota': ('django.db.models.fields.IntegerField', [], {})
        },
        u'modulo_clei.evento': {
            'Meta': {'object_name': 'Evento'},
            'fecha': ('django.db.models.fields.DateTimeField', [], {}),
            'horaFin': ('django.db.models.fields.TimeField', [], {}),
            'horaInicio': ('django.db.models.fields.TimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lugar': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'eventos'", 'to': u"orm['modulo_clei.Lugar']"}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        },
        u'modulo_clei.inscripcion': {
            'Meta': {'object_name': 'Inscripcion'},
            'clei': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'inscripciones'", 'to': u"orm['modulo_clei.CLEI']"}),
            'dirPostal': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'fecha': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pagWeb': ('django.db.models.fields.URLField', [], {'max_length': '60'}),
            'persona': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'inscripciones'", 'to': u"orm['personas.Persona']"}),
            'telf': ('django.db.models.fields.IntegerField', [], {}),
            'tipo': ('django.db.models.fields.IntegerField', [], {})
        },
        u'modulo_clei.lugar': {
            'Meta': {'object_name': 'Lugar'},
            'capacidad': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'ubicacion': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        },
        u'modulo_clei.ponencia': {
            'Meta': {'object_name': 'Ponencia', '_ormbases': [u'modulo_clei.Evento']},
            'articulos': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['modulo_clei.Articulo']", 'symmetrical': 'False'}),
            u'evento_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['modulo_clei.Evento']", 'unique': 'True', 'primary_key': 'True'}),
            'moderador': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'ponencias_moderadas'", 'to': u"orm['personas.Persona']"}),
            'ponente': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['personas.Persona']"})
        },
        u'modulo_clei.social': {
            'Meta': {'object_name': 'Social', '_ormbases': [u'modulo_clei.Evento']},
            u'evento_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['modulo_clei.Evento']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'modulo_clei.topico': {
            'Meta': {'object_name': 'Topico'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        },
        u'personas.persona': {
            'Meta': {'object_name': 'Persona', '_ormbases': [u'auth.User']},
            'apellido': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'experticies': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['modulo_clei.Topico']", 'symmetrical': 'False'}),
            'institucion': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'pais': ('django_countries.fields.CountryField', [], {'max_length': '2'}),
            u'user_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True', 'primary_key': 'True'})
        }
    }

    complete_apps = ['modulo_clei']