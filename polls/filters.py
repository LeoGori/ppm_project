import django_filters

from .models import Table


class TableFilter(django_filters.FilterSet):
    class Meta:
        model = Table
        fields = ['speech_text']
