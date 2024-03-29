from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from .models import Article, Tag, Scope


# class ScopeInLineFormset(BaseInlineFormSet):
#     def clean(self):
#         super(ScopeInLineFormset, self).clean()
#         is_main_checked = 0
#         is_unique_checked = []
#         for form in self.forms:
#             # print(form.cleaned_data)
#             if not form.is_valid():
#                 return
#             if form.cleaned_data and not form.cleaned_data.get('DELETE'):
#                 if form.cleaned_data['is_main']:
#                     is_main_checked += 1
#                 is_unique_checked.append(form.cleaned_data['tag'])
#         if len(is_unique_checked) != len(set(is_unique_checked)):
#             raise ValidationError('Один раздел не может быть указан более одного раза')
#         if is_main_checked > 1:
#             raise ValidationError('Основным может быть только один раздел')
#         if is_main_checked < 1:
#             raise ValidationError('Укажите основной раздел')


class ScopeInLine(admin.TabularInline):
    model = Scope
    # formset = ScopeInLineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInLine, ]


@admin.register(Tag)
class ArticleAdmin(admin.ModelAdmin):
    pass
