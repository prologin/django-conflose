from django import forms
from django.db import models
from django.contrib import admin
import conflose


class CSSEditorWidget(forms.Textarea):
    class Media:
        js = (
            'conflose/js/editor.js',
            'conflose/vendor/ace.js',
            'conflose/vendor/ext-themelist.js',
            'conflose/vendor/ext-language_tools.js',
            'conflose/vendor/mode-django.js',
        )

    def render(self, name, value, attrs=None, **kwargs):
        textarea = super().render(name, value, attrs, **kwargs)
        html = '''
        <div>
          <div style="display: none;">{textarea}</div>
          <div id="editor_{name}" style="width: 800px; height: 500px;"
          >{value}</div>
        </div>
        '''.format(
            textarea=textarea, name=name, value=value
        )
        return html


class ConfloseAdmin(admin.ModelAdmin):
    list_display = ['name']
    formfield_overrides = {models.TextField: {'widget': CSSEditorWidget}}


class UserConfloseAdmin(admin.ModelAdmin):
    autocomplete_fields = ['user']
    list_display = ['user', 'conflose']


admin.site.register(conflose.models.Conflose, ConfloseAdmin)
admin.site.register(conflose.models.UserConflose, UserConfloseAdmin)
