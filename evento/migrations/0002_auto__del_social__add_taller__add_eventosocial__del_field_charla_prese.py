# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Social'
        db.delete_table(u'evento_social')

        # Adding model 'Taller'
        db.create_table(u'evento_taller', (
            (u'evento_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['evento.Evento'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'evento', ['Taller'])

        # Adding model 'EventoSocial'
        db.create_table(u'evento_eventosocial', (
            (u'evento_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['evento.Evento'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'evento', ['EventoSocial'])

        # Deleting field 'Charla.presentador'
        db.delete_column(u'evento_charla', 'presentador_id')

        # Adding field 'Charla.charlista'
        db.add_column(u'evento_charla', 'charlista',
                      self.gf('django.db.models.fields.related.ForeignKey')(related_name='charlista_charla', null=True, to=orm['personas.Persona']),
                      keep_default=False)


        # Changing field 'Charla.moderador'
        db.alter_column(u'evento_charla', 'moderador_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['personas.Persona']))
        # Adding M2M table for field trabajos on 'Ponencia'
        m2m_table_name = db.shorten_name(u'evento_ponencia_trabajos')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('ponencia', models.ForeignKey(orm[u'evento.ponencia'], null=False)),
            ('articulo', models.ForeignKey(orm[u'articulo.articulo'], null=False))
        ))
        db.create_unique(m2m_table_name, ['ponencia_id', 'articulo_id'])


        # Changing field 'Ponencia.moderador'
        db.alter_column(u'evento_ponencia', 'moderador_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['personas.Persona']))

        # Changing field 'Ponencia.ponente'
        db.alter_column(u'evento_ponencia', 'ponente_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['personas.Persona']))

        # Changing field 'Lugar.ubicacion'
        db.alter_column(u'evento_lugar', 'ubicacion', self.gf('django.db.models.fields.TextField')(max_length=140))

        # Changing field 'Lugar.nombre'
        db.alter_column(u'evento_lugar', 'nombre', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'Lugar.capacidad'
        db.alter_column(u'evento_lugar', 'capacidad', self.gf('django.db.models.fields.PositiveIntegerField')())
        # Deleting field 'Evento.horaInicio'
        db.delete_column(u'evento_evento', 'horaInicio')

        # Adding field 'Evento.horaIni'
        db.add_column(u'evento_evento', 'horaIni',
                      self.gf('django.db.models.fields.TimeField')(null=True),
                      keep_default=False)


        # Changing field 'Evento.nombre'
        db.alter_column(u'evento_evento', 'nombre', self.gf('django.db.models.fields.CharField')(max_length=80))

        # Changing field 'Evento.fecha'
        db.alter_column(u'evento_evento', 'fecha', self.gf('django.db.models.fields.DateField')())

        # Changing field 'Evento.horaFin'
        db.alter_column(u'evento_evento', 'horaFin', self.gf('django.db.models.fields.TimeField')(null=True))

    def backwards(self, orm):
        # Adding model 'Social'
        db.create_table(u'evento_social', (
            (u'evento_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['evento.Evento'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'evento', ['Social'])

        # Deleting model 'Taller'
        db.delete_table(u'evento_taller')

        # Deleting model 'EventoSocial'
        db.delete_table(u'evento_eventosocial')

        # Adding field 'Charla.presentador'
        db.add_column(u'evento_charla', 'presentador',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['personas.Persona']),
                      keep_default=False)

        # Deleting field 'Charla.charlista'
        db.delete_column(u'evento_charla', 'charlista_id')


        # Changing field 'Charla.moderador'
        db.alter_column(u'evento_charla', 'moderador_id', self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['personas.Persona']))
        # Removing M2M table for field trabajos on 'Ponencia'
        db.delete_table(db.shorten_name(u'evento_ponencia_trabajos'))


        # Changing field 'Ponencia.moderador'
        db.alter_column(u'evento_ponencia', 'moderador_id', self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['personas.Persona']))

        # Changing field 'Ponencia.ponente'
        db.alter_column(u'evento_ponencia', 'ponente_id', self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['personas.Persona']))

        # Changing field 'Lugar.ubicacion'
        db.alter_column(u'evento_lugar', 'ubicacion', self.gf('django.db.models.fields.CharField')(max_length=60))

        # Changing field 'Lugar.nombre'
        db.alter_column(u'evento_lugar', 'nombre', self.gf('django.db.models.fields.CharField')(max_length=60))

        # Changing field 'Lugar.capacidad'
        db.alter_column(u'evento_lugar', 'capacidad', self.gf('django.db.models.fields.IntegerField')())
        # Adding field 'Evento.horaInicio'
        db.add_column(u'evento_evento', 'horaInicio',
                      self.gf('django.db.models.fields.TimeField')(default=0),
                      keep_default=False)

        # Deleting field 'Evento.horaIni'
        db.delete_column(u'evento_evento', 'horaIni')


        # Changing field 'Evento.nombre'
        db.alter_column(u'evento_evento', 'nombre', self.gf('django.db.models.fields.CharField')(max_length=60))

        # Changing field 'Evento.fecha'
        db.alter_column(u'evento_evento', 'fecha', self.gf('django.db.models.fields.DateTimeField')())

        # Changing field 'Evento.horaFin'
        db.alter_column(u'evento_evento', 'horaFin', self.gf('django.db.models.fields.TimeField')(default=0))

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
        u'evento.apertura': {
            'Meta': {'object_name': 'Apertura', '_ormbases': [u'evento.Evento']},
            u'evento_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['evento.Evento']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'evento.charla': {
            'Meta': {'object_name': 'Charla', '_ormbases': [u'evento.Evento']},
            'charlista': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'charlista_charla'", 'null': 'True', 'to': u"orm['personas.Persona']"}),
            u'evento_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['evento.Evento']", 'unique': 'True', 'primary_key': 'True'}),
            'moderador': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'moderador_charla'", 'null': 'True', 'to': u"orm['personas.Persona']"})
        },
        u'evento.clausura': {
            'Meta': {'object_name': 'Clausura', '_ormbases': [u'evento.Evento']},
            u'evento_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['evento.Evento']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'evento.evento': {
            'Meta': {'object_name': 'Evento'},
            'fecha': ('django.db.models.fields.DateField', [], {}),
            'horaFin': ('django.db.models.fields.TimeField', [], {'null': 'True'}),
            'horaIni': ('django.db.models.fields.TimeField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lugar': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['evento.Lugar']"}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '80'})
        },
        u'evento.eventosocial': {
            'Meta': {'object_name': 'EventoSocial', '_ormbases': [u'evento.Evento']},
            u'evento_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['evento.Evento']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'evento.lugar': {
            'Meta': {'object_name': 'Lugar'},
            'capacidad': ('django.db.models.fields.PositiveIntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'ubicacion': ('django.db.models.fields.TextField', [], {'max_length': '140'})
        },
        u'evento.ponencia': {
            'Meta': {'object_name': 'Ponencia', '_ormbases': [u'evento.Evento']},
            'articulos': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['articulo.Articulo']", 'symmetrical': 'False'}),
            u'evento_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['evento.Evento']", 'unique': 'True', 'primary_key': 'True'}),
            'moderador': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'moderador_ponencia'", 'null': 'True', 'to': u"orm['personas.Persona']"}),
            'ponente': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'ponente_ponencia'", 'null': 'True', 'to': u"orm['personas.Persona']"}),
            'trabajos': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'trabajos_ponencia'", 'null': 'True', 'to': u"orm['articulo.Articulo']"})
        },
        u'evento.taller': {
            'Meta': {'object_name': 'Taller', '_ormbases': [u'evento.Evento']},
            u'evento_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['evento.Evento']", 'unique': 'True', 'primary_key': 'True'})
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

    complete_apps = ['evento']