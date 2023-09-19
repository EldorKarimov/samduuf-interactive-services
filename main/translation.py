from modeltranslation.translator import register, TranslationOptions
from .models import Leader, Appeal, Answer

@register(Leader)
class LeaderTranslationOptions(TranslationOptions):
    fields = ('position', )

@register(Appeal)
class AppealTranslationOptions(TranslationOptions):
    fields = ('type_application', )