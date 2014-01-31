# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Articulo'
        db.create_table(u'articulo_articulo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('pclaves', self.gf('django.db.models.fields.TextField')(max_length=60)),
            ('status', self.gf('django.db.models.fields.IntegerField')(default=3)),
            ('clei', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='articulos', null=True, to=orm['modulo_clei.CLEI'])),
        ))
        db.send_create_signal(u'articulo', ['Articulo'])

        # Adding M2M table for field autores on 'Articulo'
        m2m_table_name = db.shorten_name(u'articulo_articulo_autores')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('articulo', models.ForeignKey(orm[u'articulo.articulo'], null=False)),
            ('persona', models.ForeignKey(orm[u'personas.persona'], null=False))
        ))
        db.create_unique(m2m_table_name, ['articulo_id', 'persona_id'])

        # Adding M2M table for field topicos on 'Articulo'
        m2m_table_name = db.shorten_name(u'articulo_articulo_topicos')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('articulo', models.ForeignKey(orm[u'articulo.articulo'], null=False)),
            ('topico', models.ForeignKey(orm[u'modulo_clei.topico'], null=False))
        ))
        db.create_unique(m2m_table_name, ['articulo_id', 'topico_id'])

        # Adding model 'Evaluacion'
        db.create_table(u'articulo_evaluacion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('articulo', self.gf('django.db.models.fields.related.ForeignKey')(related_name='correcciones', to=orm['articulo.Articulo'])),
            ('evaluador', self.gf('django.db.models.fields.related.ForeignKey')(related_name='evaluaciones', to=orm['personas.Persona'])),
            ('nota', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'articulo', ['Evaluacion'])

        # Adding unique constraint on 'Evaluacion', fields ['articulo', 'evaluador']
        db.create_unique(u'articulo_evaluacion', ['articulo_id', 'evaluador_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'Evaluacion', fields ['articulo', 'evaluador']
        db.delete_unique(u'articulo_evaluacion', ['articulo_id', 'evaluador_id'])

        # Deleting model 'Articulo'
        db.delete_table(u'articulo_articulo')

        # Removing M2M table for field autores on 'Articulo'
        db.delete_table(db.shorten_name(u'articulo_articulo_autores'))

        # Removing M2M table for field topicos on 'Articulo'
        db.delete_table(db.shorten_name(u'articulo_articulo_topicos'))

        # Deleting model 'Evaluacion'
        db.delete_table(u'articulo_evaluacion')


    models = {
        u'articulo.articulo': {
            'Meta': {'object_name': 'Articulo'},
            'autores': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'articulos'", 'symmetrical': 'False', 'to': u"orm['personas.Persona']"}),
            'clei': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'articulos'", 'null': 'True', 'to': u"orm['modulo_clei.CLEI']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pclaves': ('django.db.models.fields.TextField', [], {'max_length': '60'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '3'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'topicos': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['modulo_clei.Topico']", 'symmetrical': 'False'})
        },
        u'articulo.evaluacion': {
            'Meta': {'unique_together': "(('articulo', 'evaluador'),)", 'object_name': 'Evaluacion'},
            'articulo': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'correcciones'", 'to': u"orm['articulo.Articulo']"}),
            'evaluador': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'evaluaciones'", 'to': u"orm['personas.Persona']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nota': ('django.db.models.fields.IntegerField', [], {})
        },
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

    complete_apps = ['articulo']