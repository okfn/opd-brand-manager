# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'BrandOwner.owner_link'
        db.alter_column(u'brand_owner', u'OWNER_LINK', self.gf('django.db.models.fields.URLField')(max_length=255, null=True, db_column=u'OWNER_LINK'))

        # Changing field 'BrandOwner.owner_wiki_en'
        db.alter_column(u'brand_owner', u'OWNER_WIKI_EN', self.gf('django.db.models.fields.URLField')(max_length=255, null=True, db_column=u'OWNER_WIKI_EN'))

    def backwards(self, orm):

        # Changing field 'BrandOwner.owner_link'
        db.alter_column(u'brand_owner', u'OWNER_LINK', self.gf('django.db.models.fields.CharField')(default='', max_length=255, db_column=u'OWNER_LINK'))

        # Changing field 'BrandOwner.owner_wiki_en'
        db.alter_column(u'brand_owner', u'OWNER_WIKI_EN', self.gf('django.db.models.fields.CharField')(default='', max_length=255, db_column=u'OWNER_WIKI_EN'))

    models = {
        u'brand.brand': {
            'Meta': {'ordering': "[u'brand_nm']", 'unique_together': "((u'brand_nm', u'owner_cd'),)", 'object_name': 'Brand', 'db_table': "u'brand'"},
            'brand_link': ('django.db.models.fields.URLField', [], {'max_length': '255', 'null': 'True', 'db_column': "u'BRAND_LINK'", 'blank': 'True'}),
            'brand_logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'db_column': "u'BRAND_LOGO'", 'blank': 'True'}),
            'brand_nm': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'BRAND_NM'"}),
            'brand_type_cd': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['brand.BrandType']", 'db_column': "u'BRAND_TYPE_CD'"}),
            'bsin': ('django.db.models.fields.CharField', [], {'max_length': '6', 'primary_key': 'True', 'db_column': "u'BSIN'"}),
            'comments': ('django.db.models.fields.TextField', [], {'null': 'True', 'db_column': "u'COMMENTS'", 'blank': 'True'}),
            'flag_delete': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_column': "u'FLAG_DELETE'"}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'db_column': "u'LAST_MODIFIED'", 'blank': 'True'}),
            'owner_cd': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['brand.BrandOwner']", 'null': 'True', 'db_column': "u'OWNER_CD'", 'blank': 'True'})
        },
        u'brand.brandowner': {
            'Meta': {'ordering': "[u'owner_nm']", 'object_name': 'BrandOwner', 'db_table': "u'brand_owner'"},
            'owner_cd': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'OWNER_CD'"}),
            'owner_link': ('django.db.models.fields.URLField', [], {'max_length': '255', 'null': 'True', 'db_column': "u'OWNER_LINK'", 'blank': 'True'}),
            'owner_nm': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'OWNER_NM'"}),
            'owner_wiki_en': ('django.db.models.fields.URLField', [], {'max_length': '255', 'null': 'True', 'db_column': "u'OWNER_WIKI_EN'", 'blank': 'True'})
        },
        u'brand.brandtype': {
            'Meta': {'object_name': 'BrandType', 'db_table': "u'brand_type'"},
            'brand_type_cd': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'BRAND_TYPE_CD'"}),
            'brand_type_nm': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "u'BRAND_TYPE_NM'"})
        }
    }

    complete_apps = ['brand']