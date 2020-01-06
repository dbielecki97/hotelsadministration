import django_filters

from catering.models import Food, Category


class FoodListFilter(django_filters.FilterSet):
    food_type = django_filters.filters.ModelMultipleChoiceFilter(
        queryset=Category.objects.all(),
        label='Typ',
    )

    price__gt = django_filters.NumberFilter(field_name='price', lookup_expr='gt', label='Cena większa niż')
    price__lt = django_filters.NumberFilter(field_name='price', lookup_expr='lt', label='Cena mniejsza niż')
    name = django_filters.CharFilter(field_name='name', lookup_expr='contains', label='Wyszukaj')

    class Meta:
        model = Food
        fields = ('name', 'food_type', 'price__lt', 'price__gt')
