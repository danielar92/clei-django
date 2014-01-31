# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Topico'
        db.create_table(u'modulo_clei_topico', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=60)),
        ))
        db.send_create_signal(u'modulo_clei', ['Topico'])

        # Adding model 'CLEI'
        db.create_table(u'modulo_clei_clei', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fechaInscripcionDescuento', self.gf('django.db.models.fields.DateTimeField')()),
            ('fechaInscripcion', self.gf('django.db.models.fields.DateTimeField')()),
            ('fechaTopeArticulo', self.gf('django.db.models.fields.DateTimeField')()),
            ('fechaNotificacion', self.gf('django.db.models.fields.DateTimeField')()),
            ('tarifaReducida', self.gf('django.db.models.fields.FloatField')()),
            ('tarifaNormal', self.gf('django.db.models.fields.FloatField')()),
            ('fechaInicio', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'modulo_clei', ['CLEI'])

        # Adding M2M table for field topicos on 'CLEI'
        m2m_table_name = db.shorten_name(u'modulo_clei_clei_topicos')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('clei', models.ForeignKey(orm[u'modulo_clei.clei'], null=False)),
            ('topico', models.ForeignKey(orm[u'modulo_clei.topico'], null=False))
        ))
        db.create_unique(m2m_table_name, ['clei_id', 'topico_id'])

        # Adding model 'CP'
        db.create_table(u'modulo_clei_cp', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('clei', self.gf('django.db.models.fields.related.OneToOneField')(related_name='cp', unique=True, to=orm['modulo_clei.CLEI'])),
        ))
        db.send_create_signal(u'modulo_clei', ['CP'])

        # Adding M2M table for field miembros on 'CP'
        m2m_table_name = db.shorten_name(u'modulo_clei_cp_miembros')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('cp', models.ForeignKey(orm[u'modulo_clei.cp'], null=False)),
            ('miembrocp', models.ForeignKey(orm[u'personas.miembrocp'], null=False))
        ))
        db.create_unique(m2m_table_name, ['cp_id', 'miembrocp_id'])

        # Adding model 'Inscripcion'
        db.create_table(u'modulo_clei_inscripcion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('dirPostal', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('pagWeb', self.gf('django.db.models.fields.URLField')(max_length=60)),
            ('telf', self.gf('django.db.models.fields.IntegerField')()),
            ('tipo', self.gf('django.db.models.fields.IntegerField')()),
            ('fecha', self.gf('django.db.models.fields.DateTimeField')()),
            ('clei', self.gf('django.db.models.fields.related.ForeignKey')(related_name='inscripciones', to=orm['modulo_clei.CLEI'])),
            ('persona', self.gf('django.db.models.fields.related.ForeignKey')(related_name='inscripciones', to=orm['personas.Persona'])),
        ))
        db.send_create_signal(u'modulo_clei', ['Inscripcion'])

        # Adding model 'Articulo'
        db.create_table(u'modulo_clei_articulo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('pclaves', self.gf('django.db.models.fields.TextField')(max_length=60)),
            ('status', self.gf('django.db.models.fields.IntegerField')(default=3)),
            ('clei', self.gf('django.db.models.fields.related.ForeignKey')(related_name='articulos', to=orm['modulo_clei.CLEI'])),
        ))
        db.send_create_signal(u'modulo_clei', ['Articulo'])

        # Adding M2M table for field autores on 'Articulo'
        m2m_table_name = db.shorten_name(u'modulo_clei_articulo_autores')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('articulo', models.ForeignKey(orm[u'modulo_clei.articulo'], null=False)),
            ('autor', models.ForeignKey(orm[u'personas.autor'], null=False))
        ))
        db.create_unique(m2m_table_name, ['articulo_id', 'autor_id'])

        # Adding M2M table for field topicos on 'Articulo'
        m2m_table_name = db.shorten_name(u'modulo_clei_articulo_topicos')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('articulo', models.ForeignKey(orm[u'modulo_clei.articulo'], null=False)),
            ('topico', models.ForeignKey(orm[u'modulo_clei.topico'], null=False))
        ))
        db.create_unique(m2m_table_name, ['articulo_id', 'topico_id'])

        # Adding model 'Evaluacion'
        db.create_table(u'modulo_clei_evaluacion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('articulo', self.gf('django.db.models.fields.related.ForeignKey')(related_name='correcciones', to=orm['modulo_clei.Articulo'])),
            ('evaluador', self.gf('django.db.models.fields.related.ForeignKey')(related_name='evaluaciones', to=orm['personas.Persona'])),
            ('nota', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'modulo_clei', ['Evaluacion'])

        # Adding unique constraint on 'Evaluacion', fields ['articulo', 'evaluador']
        db.create_unique(u'modulo_clei_evaluacion', ['articulo_id', 'evaluador_id'])

        # Adding model 'Lugar'
        db.create_table(u'modulo_clei_lugar', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('ubicacion', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('capacidad', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'modulo_clei', ['Lugar'])

        # Adding model 'Evento'
        db.create_table(u'modulo_clei_evento', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('fecha', self.gf('django.db.models.fields.DateTimeField')()),
            ('horaInicio', self.gf('django.db.models.fields.TimeField')()),
            ('horaFin', self.gf('django.db.models.fields.TimeField')()),
            ('lugar', self.gf('django.db.models.fields.related.ForeignKey')(related_name='eventos', to=orm['modulo_clei.Lugar'])),
        ))
        db.send_create_signal(u'modulo_clei', ['Evento'])

        # Adding model 'Ponencia'
        db.create_table(u'modulo_clei_ponencia', (
            (u'evento_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['modulo_clei.Evento'], unique=True, primary_key=True)),
            ('moderador', self.gf('django.db.models.fields.related.ForeignKey')(related_name='ponencias_moderadas', to=orm['personas.Persona'])),
            ('ponente', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['personas.Persona'])),
        ))
        db.send_create_signal(u'modulo_clei', ['Ponencia'])

        # Adding M2M table for field articulos on 'Ponencia'
        m2m_table_name = db.shorten_name(u'modulo_clei_ponencia_articulos')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('ponencia', models.ForeignKey(orm[u'modulo_clei.ponencia'], null=False)),
            ('articulo', models.ForeignKey(orm[u'modulo_clei.articulo'], null=False))
        ))
        db.create_unique(m2m_table_name, ['ponencia_id', 'articulo_id'])

        # Adding model 'Charla'
        db.create_table(u'modulo_clei_charla', (
            (u'evento_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['modulo_clei.Evento'], unique=True, primary_key=True)),
            ('moderador', self.gf('django.db.models.fields.related.ForeignKey')(related_name='charlas_moderadas', to=orm['personas.Persona'])),
            ('presentador', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['personas.Persona'])),
        ))
        db.send_create_signal(u'modulo_clei', ['Charla'])

        # Adding model 'Social'
        db.create_table(u'modulo_clei_social', (
            (u'evento_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['modulo_clei.Evento'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'modulo_clei', ['Social'])

        # Adding model 'Apertura'
        db.create_table(u'modulo_clei_apertura', (
            (u'evento_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['modulo_clei.Evento'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'modulo_clei', ['Apertura'])

        # Adding model 'Clausura'
        db.create_table(u'modulo_clei_clausura', (
            (u'evento_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['modulo_clei.Evento'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'modulo_clei', ['Clausura'])


    def backwards(self, orm):
        # Removing unique constraint on 'Evaluacion', fields ['articulo', 'evaluador']
        db.delete_unique(u'modulo_clei_evaluacion', ['articulo_id', 'evaluador_id'])

        # Deleting model 'Topico'
        db.delete_table(u'modulo_clei_topico')

        # Deleting model 'CLEI'
        db.delete_table(u'modulo_clei_clei')

        # Removing M2M table for field topicos on 'CLEI'
        db.delete_table(db.shorten_name(u'modulo_clei_clei_topicos'))

        # Deleting model 'CP'
        db.delete_table(u'modulo_clei_cp')

        # Removing M2M table for field miembros on 'CP'
        db.delete_table(db.shorten_name(u'modulo_clei_cp_miembros'))

        # Deleting model 'Inscripcion'
        db.delete_table(u'modulo_clei_inscripcion')

        # Deleting model 'Articulo'
        db.delete_table(u'modulo_clei_articulo')

        # Removing M2M table for field autores on 'Articulo'
        db.delete_table(db.shorten_name(u'modulo_clei_articulo_autores'))

        # Removing M2M table for field topicos on 'Articulo'
        db.delete_table(db.shorten_name(u'modulo_clei_articulo_topicos'))

        # Deleting model 'Evaluacion'
        db.delete_table(u'modulo_clei_evaluacion')

        # Deleting model 'Lugar'
        db.delete_table(u'modulo_clei_lugar')

        # Deleting model 'Evento'
        db.delete_table(u'modulo_clei_evento')

        # Deleting model 'Ponencia'
        db.delete_table(u'modulo_clei_ponencia')

        # Removing M2M table for field articulos on 'Ponencia'
        db.delete_table(db.shorten_name(u'modulo_clei_ponencia_articulos'))

        # Deleting model 'Charla'
        db.delete_table(u'modulo_clei_charla')

        # Deleting model 'Social'
        db.delete_table(u'modulo_clei_social')

        # Deleting model 'Apertura'
        db.delete_table(u'modulo_clei_apertura')

        # Deleting model 'Clausura'
        db.delete_table(u'modulo_clei_clausura')


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
            'autores': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['personas.Autor']", 'symmetrical': 'False'}),
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
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'miembros': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['personas.MiembroCP']", 'symmetrical': 'False'})
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
        u'personas.autor': {
            'Meta': {'object_name': 'Autor', '_ormbases': [u'personas.Persona']},
            'pais': ('django_countries.fields.CountryField', [], {'max_length': '2'}),
            u'persona_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['personas.Persona']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'personas.miembrocp': {
            'Meta': {'object_name': 'MiembroCP', '_ormbases': [u'personas.Persona']},
            'experticies': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['modulo_clei.Topico']", 'symmetrical': 'False'}),
            u'persona_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['personas.Persona']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'personas.persona': {
            'Meta': {'object_name': 'Persona', '_ormbases': [u'auth.User']},
            'apellido': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'institucion': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            u'user_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True', 'primary_key': 'True'})
        }
    }

    complete_apps = ['modulo_clei']