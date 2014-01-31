# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing unique constraint on 'Evaluacion', fields ['articulo', 'evaluador']
        db.delete_unique(u'modulo_clei_evaluacion', ['articulo_id', 'evaluador_id'])

        # Deleting model 'Evento'
        db.delete_table(u'modulo_clei_evento')

        # Deleting model 'Articulo'
        db.delete_table(u'modulo_clei_articulo')

        # Removing M2M table for field autores on 'Articulo'
        db.delete_table(db.shorten_name(u'modulo_clei_articulo_autores'))

        # Removing M2M table for field topicos on 'Articulo'
        db.delete_table(db.shorten_name(u'modulo_clei_articulo_topicos'))

        # Deleting model 'Charla'
        db.delete_table(u'modulo_clei_charla')

        # Deleting model 'Clausura'
        db.delete_table(u'modulo_clei_clausura')

        # Deleting model 'Apertura'
        db.delete_table(u'modulo_clei_apertura')

        # Deleting model 'Evaluacion'
        db.delete_table(u'modulo_clei_evaluacion')

        # Deleting model 'Social'
        db.delete_table(u'modulo_clei_social')

        # Deleting model 'Lugar'
        db.delete_table(u'modulo_clei_lugar')

        # Deleting model 'Ponencia'
        db.delete_table(u'modulo_clei_ponencia')

        # Removing M2M table for field articulos on 'Ponencia'
        db.delete_table(db.shorten_name(u'modulo_clei_ponencia_articulos'))

        # Deleting field 'Inscripcion.tipo'
        db.delete_column(u'modulo_clei_inscripcion', 'tipo')

        # Deleting field 'Inscripcion.telf'
        db.delete_column(u'modulo_clei_inscripcion', 'telf')

        # Deleting field 'Inscripcion.pagWeb'
        db.delete_column(u'modulo_clei_inscripcion', 'pagWeb')

        # Deleting field 'Inscripcion.dirPostal'
        db.delete_column(u'modulo_clei_inscripcion', 'dirPostal')

        # Adding field 'Inscripcion.costo'
        db.add_column(u'modulo_clei_inscripcion', 'costo',
                      self.gf('django.db.models.fields.FloatField')(default='148148'),
                      keep_default=False)


        # Changing field 'Inscripcion.fecha'
        db.alter_column(u'modulo_clei_inscripcion', 'fecha', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True))
        # Adding unique constraint on 'Inscripcion', fields ['clei', 'persona']
        db.create_unique(u'modulo_clei_inscripcion', ['clei_id', 'persona_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'Inscripcion', fields ['clei', 'persona']
        db.delete_unique(u'modulo_clei_inscripcion', ['clei_id', 'persona_id'])

        # Adding model 'Evento'
        db.create_table(u'modulo_clei_evento', (
            ('lugar', self.gf('django.db.models.fields.related.ForeignKey')(related_name='eventos', to=orm['modulo_clei.Lugar'])),
            ('fecha', self.gf('django.db.models.fields.DateTimeField')()),
            ('horaFin', self.gf('django.db.models.fields.TimeField')()),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=60)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('horaInicio', self.gf('django.db.models.fields.TimeField')()),
        ))
        db.send_create_signal(u'modulo_clei', ['Evento'])

        # Adding model 'Articulo'
        db.create_table(u'modulo_clei_articulo', (
            ('status', self.gf('django.db.models.fields.IntegerField')(default=3)),
            ('clei', self.gf('django.db.models.fields.related.ForeignKey')(related_name='articulos', null=True, to=orm['modulo_clei.CLEI'], blank=True)),
            ('pclaves', self.gf('django.db.models.fields.TextField')(max_length=60)),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=60)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'modulo_clei', ['Articulo'])

        # Adding M2M table for field autores on 'Articulo'
        m2m_table_name = db.shorten_name(u'modulo_clei_articulo_autores')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('articulo', models.ForeignKey(orm[u'modulo_clei.articulo'], null=False)),
            ('persona', models.ForeignKey(orm[u'personas.persona'], null=False))
        ))
        db.create_unique(m2m_table_name, ['articulo_id', 'persona_id'])

        # Adding M2M table for field topicos on 'Articulo'
        m2m_table_name = db.shorten_name(u'modulo_clei_articulo_topicos')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('articulo', models.ForeignKey(orm[u'modulo_clei.articulo'], null=False)),
            ('topico', models.ForeignKey(orm[u'modulo_clei.topico'], null=False))
        ))
        db.create_unique(m2m_table_name, ['articulo_id', 'topico_id'])

        # Adding model 'Charla'
        db.create_table(u'modulo_clei_charla', (
            ('moderador', self.gf('django.db.models.fields.related.ForeignKey')(related_name='charlas_moderadas', to=orm['personas.Persona'])),
            (u'evento_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['modulo_clei.Evento'], unique=True, primary_key=True)),
            ('presentador', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['personas.Persona'])),
        ))
        db.send_create_signal(u'modulo_clei', ['Charla'])

        # Adding model 'Clausura'
        db.create_table(u'modulo_clei_clausura', (
            (u'evento_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['modulo_clei.Evento'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'modulo_clei', ['Clausura'])

        # Adding model 'Apertura'
        db.create_table(u'modulo_clei_apertura', (
            (u'evento_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['modulo_clei.Evento'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'modulo_clei', ['Apertura'])

        # Adding model 'Evaluacion'
        db.create_table(u'modulo_clei_evaluacion', (
            ('nota', self.gf('django.db.models.fields.IntegerField')()),
            ('evaluador', self.gf('django.db.models.fields.related.ForeignKey')(related_name='evaluaciones', to=orm['personas.Persona'])),
            ('articulo', self.gf('django.db.models.fields.related.ForeignKey')(related_name='correcciones', to=orm['modulo_clei.Articulo'])),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'modulo_clei', ['Evaluacion'])

        # Adding unique constraint on 'Evaluacion', fields ['articulo', 'evaluador']
        db.create_unique(u'modulo_clei_evaluacion', ['articulo_id', 'evaluador_id'])

        # Adding model 'Social'
        db.create_table(u'modulo_clei_social', (
            (u'evento_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['modulo_clei.Evento'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'modulo_clei', ['Social'])

        # Adding model 'Lugar'
        db.create_table(u'modulo_clei_lugar', (
            ('ubicacion', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('capacidad', self.gf('django.db.models.fields.IntegerField')()),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=60)),
        ))
        db.send_create_signal(u'modulo_clei', ['Lugar'])

        # Adding model 'Ponencia'
        db.create_table(u'modulo_clei_ponencia', (
            ('moderador', self.gf('django.db.models.fields.related.ForeignKey')(related_name='ponencias_moderadas', to=orm['personas.Persona'])),
            (u'evento_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['modulo_clei.Evento'], unique=True, primary_key=True)),
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

        # Adding field 'Inscripcion.tipo'
        db.add_column(u'modulo_clei_inscripcion', 'tipo',
                      self.gf('django.db.models.fields.IntegerField')(default=1),
                      keep_default=False)

        # Adding field 'Inscripcion.telf'
        db.add_column(u'modulo_clei_inscripcion', 'telf',
                      self.gf('django.db.models.fields.IntegerField')(default=319498198),
                      keep_default=False)

        # Adding field 'Inscripcion.pagWeb'
        db.add_column(u'modulo_clei_inscripcion', 'pagWeb',
                      self.gf('django.db.models.fields.URLField')(default='', max_length=60),
                      keep_default=False)

        # Adding field 'Inscripcion.dirPostal'
        db.add_column(u'modulo_clei_inscripcion', 'dirPostal',
                      self.gf('django.db.models.fields.CharField')(default='adgjkgj', max_length=60),
                      keep_default=False)

        # Deleting field 'Inscripcion.costo'
        db.delete_column(u'modulo_clei_inscripcion', 'costo')


        # Changing field 'Inscripcion.fecha'
        db.alter_column(u'modulo_clei_inscripcion', 'fecha', self.gf('django.db.models.fields.DateTimeField')())

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
            'fecha': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'persona': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'inscripciones'", 'to': u"orm['personas.Persona']"})
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