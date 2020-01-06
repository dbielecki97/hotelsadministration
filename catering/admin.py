from django.contrib import admin

from catering.models import Food, Catering, Category, FoodQuantity

admin.site.register(Food)
admin.site.register(Category)
admin.site.register(FoodQuantity)


class FoodQuantityTabular(admin.TabularInline):
    model = FoodQuantity
    extra = 0
    fields = ('foodItem', 'quantity',)


@admin.register(Catering)
class CateringAdmin(admin.ModelAdmin):
    inlines = (FoodQuantityTabular,)
