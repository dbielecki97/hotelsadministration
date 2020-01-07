import django_filters
from django import forms

from catering.models import Food, Category


class FoodListFilter(django_filters.FilterSet):
    food_type = django_filters.filters.ModelMultipleChoiceFilter(
        queryset=Category.objects.all(),
        label='Kategoria',
        widget=forms.CheckboxSelectMultiple(),
    )

    price__gt = django_filters.NumberFilter(field_name='price', lookup_expr='gt', label='Cena większa niż')
    price__lt = django_filters.NumberFilter(field_name='price', lookup_expr='lt', label='Cena mniejsza niż')
    name = django_filters.CharFilter(field_name='name', lookup_expr='contains', label='Nazwa zawiera')

    class Meta:
        model = Food
        fields = ('name', 'food_type', 'price__lt', 'price__gt',)
